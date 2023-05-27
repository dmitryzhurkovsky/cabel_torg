# Cabel Torg

## Certbot 

To generate an SSL certificate for a new domain, follow these steps:

1. Ensure that the following folders are empty:
   - `data/certbot/conf`
   - `data/certbot/www`

   If they contain any files, clean out these folders before proceeding.

2. Open the `reverse_proxy/prod.conf` file and comment out the following line:
    ```nginx
    #return 301 https://cabel-torg.by$request_uri; 
    ```
3. In the `docker-compose.yaml` file, locate the command:
    ```shell
    certonly --webroot -w /var/www/certbot
    ```
    Replace the `-d` argument with the valid domain name(s) you want to generate the certificate for. 
    You can specify multiple domains using the `-d` flag like this:
    ```commandline
    -d domain1 -d domain2
    ```
4. Launch the script located in `reverse_proxy/`:
    ```bash
    ./reverse_proxy/init-letsencrypt.sh
    ```
   It's possible that `init-letsencrypt.sh` should be in a root folder of the project. If there are any problems with 
   paths move it to the root folder.
5. Open the `reverse_proxy/prod.conf` file and uncomment out the following line:
    ```nginx
    #return 301 https://cabel-torg.by$request_uri; 
    ```