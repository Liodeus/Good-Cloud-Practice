# cloudsql_backup_location

## Background

Cloud SQL backup instances location have to comply with data soveriegnty regulation

## Fix

```shell
gcloud sql instances patch [INSTANCE_NAME] --backup-location=eu
```

## References

- [Data sovereignty](https://en.wikipedia.org/wiki/Data_sovereignty)
- [GDPR General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
- [Setting a custom location for backups](https://cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#gcloud_2)
- [Custom backup locations](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups#custom-backup-location)
