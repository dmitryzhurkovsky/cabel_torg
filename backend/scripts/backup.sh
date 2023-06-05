#!/bin/bash
PROJECT_DIR=/root/cabel_torg
DATA_DIR=/data
LOGS_DIR=$DATA_DIR/logs
BACKUPS_DIR=$DATA_DIR/backups
DOCKER_BACKUPS_DIR=/backups  # It's used for indicating a folder in a ocker container.
LOG_FILE=$LOGS_DIR/cabel_torg_backup_process.log

# Create the backup and logs directories.
mkdir -p $BACKUPS_DIR
mkdir -p $LOGS_DIR

# Get env variables
source $PROJECT_DIR/backend/.env

# Get current datetime
date=$(date "+%Y-%m-%d")

#echo "Start logging process in $date" > $LOG_FILE
PGPASSWORD=$POSTGRES_PASSWORD docker-compose exec -T db mkdir -p $DOCKER_BACKUPS_DIR
PGPASSWORD=$POSTGRES_PASSWORD docker-compose exec -T db pg_dump -U $POSTGRES_USER -d $POSTGRES_DB -f "$DOCKER_BACKUPS_DIR/${date}_backup.sql"
echo "Database backup has been created on ${date}" >> $LOG_FILE

rsync -a --stats --exclude="backups" --exclude="logs" "$DATA_DIR/" "$BACKUPS_DIR/"
echo "Data was copied on ${date}" >> $LOG_FILE

find $BACKUPS_DIR -name '*_backup.sql' -type f -mtime +5 -delete
echo "Old backup files were deleted" >> $LOG_FILE