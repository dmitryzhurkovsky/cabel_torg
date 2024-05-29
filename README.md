# Cabel Torg 
## Description
It's a web application that provides an e-commerce site is integrated with 1C Bookkeeping.

The frontend application for customers provides an opportunity to simplify interaction with the seller of goods 
and allows them to perform all operations without visiting the shop.
The admin panel for service users simplifies working with users' requests, setting up discounts, changing requisites, 
updating news, and working with orders.

The web application is hosted on the following domain - https://cabel-torg.by.

## Team
* Backend, parser, devops - dmitryzhurkovsky@gmail.com(https://github.com/dmitryzhurkovsky).
* Frontend - kiselmen@rambler.ru/1813390@gmail.com(https://github.com/kiselmen), luter195@gmail.com(https://github.com/ronald13).
* Product owner, stakeholder, ba, qa - luter195@gmail.com(https://github.com/ronald13).

## Main components and technical overview
Docker and Docker Compose are used for the dockerization of the application. Dockerfiles for each service are placed 
in the `build` folder of each service.

### Backend application
* Python 3.11.
* FastAPI framework is used for building a REST. 
* JWT tokens are used for authentication and authorization.
* Postgres is used as the database.
* SQLAlchemy is used as an ORM.
* Alembic is used as a migration tool.
* The main commands are kept in the Makefile.

### Parser
Automation with 1C is done through the following flow:
1. Upload `import_01.xml`, `offers_01.xml` and images to the required folders.
   * `import_01.xml` and `offers_01.xml` are uploaded via SCP using the following command:
      ```shell
      scp import0_1 offers0_1.xml service_user@ip_address_of_service:/data/parser_files/.
      ```
   * Images are uploaded via SCP using the following command:
      ```shell
      scp -r import_files/. service_user@ip_address_of_service:/data/site_media/images/.
      ```
2. The parser server checks import_01.xml and offers_01.xml every n minutes (can be changed in an .env file). 
3. If there are any changes in these files, they will be recognized by the parser, and the parsing process will start 
automatically.
4. A service user is notified if any exceptions are raised. The service user can be changed in an .env file.

### Frontend
* Node 18.14.1.
* VueJS is used for the admin dashboard.
* NuxtJS is used for customer's application.

### Reverse proxy
Nginx is used as a reverse proxy to redirect requests to the frontend application, 
the admin dashboard and the backend API. Additionally, Nginx is used as a tool for sharing static files and images and 
for setting up an HTTPS connection in conjugation with Certbot.

### Delivery agent
Postfix is used for sending notifications. 
To ensure legitimate email authenticates properly SPF, DKIM and DMARK were used. 

To check why messages aren't sent `mxtoolbox.com/emailhealth` was used.


### Certbot
To generate an SSL certificate for a new domain, follow these steps:

1. Go to project folder
    ```bash
    cd cabel_torg
    ```
2. Launch the script located in `reverse_proxy` folder. **In dialog window use 'n' answer.**:
    ```bash
    ./reverse_proxy/init-letsencrypt.sh
    ```
   

3. If there any errors before step 2 you should do the following:
   * Edit the `reverse_proxy/prod.conf`
   * Replace `listen 443 ssl` -> `listen 443`
   * Comment lines started from: `ssl_dhparam ...`, `ssl_certificate ...`, `ssl_certificate_key ...`. There should be 2 places for each value.
   * When the script is finished return everything back and execute the following command:
      ```bash
      git restore reverse_proxy/prod.conf && docker compose up --build -d reverse_proxy
      ```
To get more information about it use the following source:
https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

### Backups
`Crontab` and `backend/scripts/backup.sh` script are used to backup all data.
To configurate it follow the following instruction:

```text
0 0 * * * /root/cabel_torg/backend/scripts/backup.sh
```

All backups are kept in /backups.

### CI/CD processes
Github actions and a self-hosted runner are used for this purpose. 
The config file is kept in `.github/workflows/main.yaml` and there is deploy stage only there.

To get more detail about self-hosted runners follow this links 
https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners

There are 2 actions:
* deploy - is used after each merge in main.
* rebuild-without-cache - can be launched manually and build containers without a cache

### Docker configuration
To optimise space usage and reduce size of logs:
```shell
vim /etc/docker/daemon.json
```
Set up max size of logs for each containers and count of files.
```json
{
  "log-driver": "json-file",
  "log-opts": {"max-size": "500m", "max-file": "3"}
}
```

To clean up logs use the following command:
```shell
sudo sh -c 'truncate -s 0 /var/lib/docker/containers/*/*-json.log
'```
