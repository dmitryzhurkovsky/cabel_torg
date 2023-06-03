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
To get more information about it use the following source:
https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71


## Backups

`Crontab` and `backend/scripts/backup.sh` script are used to backup all data.
To configurate it follow the following instruction:

```text
0 0 * * * /root/cabel_torg/backend/scripts/backup.sh
```


## CI/CD processes

Github actions and a self-hosted runner are used for this purpose. 
The config file is kept in `.github/workflows/main.yaml` and there is deploy stage only there.

To get more detail about self-hosted runners follow this links 
https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners


