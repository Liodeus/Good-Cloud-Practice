# bq_dataset_location to_be_adapted

## Background

Biqquery datasets location have to comply with data soveriegnty regulation

## Fix

Bigquery datasets cannot be moved. Create a new dataset in a compliant location, move data, delete the non compliant dataset.

```shell
bq --location=location mk \
--dataset \
--default_table_expiration integer1 \
--default_partition_expiration integer2 \
--description description \
project_id:dataset

bq ls --filter labels.key:value \
--max_results integer \
--format=prettyjson \
--project_id project_id

bq mk --transfer_config --project_id=PROJECT_ID --data_source=DATA_SOURCE --target_dataset=DATASET --display_name=NAME --params='PARAMETERS'

bq rm -r -f -d project_id:dataset
```

## References

- [Data sovereignty](https://en.wikipedia.org/wiki/Data_sovereignty)
- [GDPR General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
- [BQ dataset locations](https://cloud.google.com/bigquery/docs/locations)
- [BQ creating datasets](https://cloud.google.com/bigquery/docs/datasets)
- [BQ copying datasets](https://cloud.google.com/bigquery/docs/copying-datasets)
- [BQ managing datasets](https://cloud.google.com/bigquery/docs/managing-datasets#deleting_datasets)
