# cloudsql_backup

## Background

CloudSQL instances must have a backup schedule.

Backups help you restore lost data to your Cloud SQL instance. You can also restore an instance that is having problems from a backup. Enable automated backups for any instance that contains necessary data. Backups protect your data from loss or damage.

Enabling automated backups, along with **binary logging**, is also required for some operations, such as clone, replica creation and Point-in-time recovery.

## Fix

```shell
gcloud sql instances patch [INSTANCE_NAME] --backup-start-time [HH:MM]
gcloud sql instances patch [INSTANCE_NAME] --enable-bin-log
```

## References

- [Overview of backups](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups)
- [FAQ/Backup and Recovery](https://cloud.google.com/sql/faq#backup-and-recovery)
- [Point-in-time recovery](https://cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr)
- [Enabling binary logs](https://cloud.google.com/sql/docs/mysql/backup-recovery/pitr#enablingpitr)
- [Creating and managing on-demand and automatic backups](https://cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#gcloud)
