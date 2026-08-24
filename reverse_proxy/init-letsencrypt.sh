#!/bin/bash
#
# Bootstrap Let's Encrypt certificates for a FRESH deployment.
#
# WARNING - READ BEFORE RUNNING
#
# On a server that is already serving traffic you almost certainly do NOT need
# this script. Certificates renew by themselves: the certbot container runs
# `certbot renew` every 12h, and reverse_proxy reloads nginx every 6h to pick
# up the new files.
#
# This script previously deleted /data/certbot/conf outright and fetched its
# TLS parameters from URLs that now return 404, writing the string
# "404: Not Found" into options-ssl-nginx.conf and ssl-dhparams.pem. That took
# the production site down twice on 2026-08-24. It no longer deletes live data
# and no longer depends on those URLs.
#
# Run from the project root:  ./reverse_proxy/init-letsencrypt.sh

set -euo pipefail

domains=(cabel-torg.by www.cabel-torg.by admin.cabel-torg.by)
rsa_key_size=4096
data_path="/data/certbot"
email="dmitryzhurkovsky@gmail.com"
staging=0        # 1 = use the staging CA while testing, does not count against limits
force_renewal=0  # keep 0: Let's Encrypt allows only 5 issuances per domain set per week

primary="${domains[0]}"

# Compose v2 ("docker compose") with a fallback to the v1 binary name.
compose() {
  if docker compose version >/dev/null 2>&1; then
    docker compose "$@"
  else
    docker-compose "$@"
  fi
}

if ! docker info >/dev/null 2>&1; then
  echo "Error: docker is not available." >&2
  exit 1
fi

### Refuse to clobber a working certificate unless explicitly told to.
if [ -d "$data_path/conf/live/$primary" ]; then
  echo
  echo "!!! A certificate for $primary already exists in $data_path/conf/live."
  echo "!!! It renews automatically - running this script is almost certainly a mistake."
  echo "!!! Continuing will request a brand new certificate and counts against the"
  echo "!!! Let's Encrypt limit of 5 issuances per week for this domain set."
  echo
  read -r -p "Type REPLACE (all caps) to continue anyway: " decision
  if [ "$decision" != "REPLACE" ]; then
    echo "Aborted, nothing was changed."
    exit 0
  fi
fi

mkdir -p "$data_path/conf" "$data_path/www"

### TLS parameters, written locally - no network fetch, nothing to 404.
if [ ! -s "$data_path/conf/options-ssl-nginx.conf" ]; then
  echo "### Writing options-ssl-nginx.conf ..."
  cat > "$data_path/conf/options-ssl-nginx.conf" <<'NGINX_SSL_OPTIONS'
# Contents are based on https://ssl-config.mozilla.org (intermediate profile).

ssl_session_cache shared:le_nginx_SSL:10m;
ssl_session_timeout 1440m;
ssl_session_tickets off;

ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;

ssl_ciphers "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305";
NGINX_SSL_OPTIONS
else
  echo "### options-ssl-nginx.conf already present, keeping it."
fi

if [ ! -s "$data_path/conf/ssl-dhparams.pem" ]; then
  echo "### Extracting ssl-dhparams.pem from the certbot image ..."
  docker run --rm --entrypoint cat certbot/certbot \
    /opt/certbot/src/certbot/certbot/ssl-dhparams.pem \
    > "$data_path/conf/ssl-dhparams.pem"
else
  echo "### ssl-dhparams.pem already present, keeping it."
fi

# Both files are included by nginx; a truncated or error-page version is fatal.
for f in "$data_path/conf/options-ssl-nginx.conf" "$data_path/conf/ssl-dhparams.pem"; do
  if [ ! -s "$f" ] || [ "$(wc -c < "$f")" -lt 100 ] || grep -qi "not found\|<html" "$f"; then
    echo "Error: $f looks invalid - refusing to continue and break nginx." >&2
    exit 1
  fi
done

### Dummy certificate so nginx can start before the real one exists.
if [ ! -d "$data_path/conf/live/$primary" ]; then
  echo "### Creating dummy certificate for $primary ..."
  path="/etc/letsencrypt/live/$primary"
  mkdir -p "$data_path/conf/live/$primary"
  compose run --rm --entrypoint "\
    openssl req -x509 -nodes -newkey rsa:$rsa_key_size -days 1 \
      -keyout '$path/privkey.pem' \
      -out '$path/fullchain.pem' \
      -subj '/CN=localhost'" certbot

  echo "### Starting nginx ..."
  compose up --force-recreate -d reverse_proxy

  echo "### Removing dummy certificate ..."
  compose run --rm --entrypoint "\
    rm -Rf /etc/letsencrypt/live/$primary && \
    rm -Rf /etc/letsencrypt/archive/$primary && \
    rm -Rf /etc/letsencrypt/renewal/$primary.conf" certbot
else
  echo "### Ensuring nginx is up ..."
  compose up -d reverse_proxy
fi

### Request the real certificate over the webroot nginx already serves.
domain_args=""
for domain in "${domains[@]}"; do
  domain_args="$domain_args -d $domain"
done

case "$email" in
  "") email_arg="--register-unsafely-without-email" ;;
  *)  email_arg="--email $email" ;;
esac

staging_arg=""
if [ "$staging" != "0" ]; then staging_arg="--staging"; fi

force_arg=""
if [ "$force_renewal" != "0" ]; then force_arg="--force-renewal"; fi

echo "### Requesting Let's Encrypt certificate for ${domains[*]} ..."
compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $email_arg \
    $domain_args \
    --rsa-key-size $rsa_key_size \
    --agree-tos \
    --non-interactive \
    $force_arg" certbot

echo "### Reloading nginx ..."
compose exec reverse_proxy nginx -s reload

echo "### Done. Verify renewal works:  docker exec prod_certbot certbot renew --dry-run"
