#!/bin/bash
date=date=$(date '+%Y-%m-%d')
source backend/env.prod

echo "Start logging process in $date\n" > /var/log/cabel_torg_backup.log

BACKUP_FILE="${date}_backup.sql"

pg_dump -U $DB_USERNAME -W $DB_NAME > $BACKUP_FILE
echo "Database has been done on ${date}" >> /var/log/cabel_torg_backup.log

cp -r /root/cabel_torg/data/* /root/dumped_data/
echo "Data was copied ${date}" >> /var/log/cabel_torg_backup.log