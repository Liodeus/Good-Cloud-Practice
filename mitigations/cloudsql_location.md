# cloudsql_location

## Background

Cloud SQL instances location have to comply with data soveriegnty regulation

## Fix

Cloud SQL instances cannot be moved. Create a new instance in a compliant location, move data, delete the non compliant dataset.

```shell
gcloud sql export sql [INSTANCE_NAME] gs://[BUCKET_NAME]/sqldumpfile.gz \
                              --database=[DATABASE_NAME] --offload
  
gcloud sql instances create INSTANCE_NAME --tier=MACHINE_TYPE --region=REGION

gcloud sql import sql [INSTANCE_NAME] gs://[BUCKET_NAME]/[IMPORT_FILE_NAME] \
                            --database=[DATABASE_NAME]

gcloud sql instances delete [INSTANCE_NAME]
```

## References

- [Data sovereignty](https://en.wikipedia.org/wiki/Data_sovereignty)
- [GDPR General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
- [Cloud SQL Instance location](https://cloud.google.com/sql/docs/mysql/locations)
- [Exporting data from Cloud SQL](https://cloud.google.com/sql/docs/mysql/import-export/exporting)
- [Cloud SQL Creating instances](https://cloud.google.com/sql/docs/mysql/create-instance)
- [Importing data into Cloud SQL](https://cloud.google.com/sql/docs/mysql/import-export/importing)
- [Cloud SQL Deleting instances](https://cloud.google.com/sql/docs/mysql/delete-instance)
