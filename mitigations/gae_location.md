# gae_location to_be_adapted

## Background

App Engine application location have to comply with data soveriegnty regulation

## Fix

There is only one GAE application per GCP project. The location is choosen at the time GAE is enable on the project an cannot be changed. A GAE application cannot be deleted. A project can be deleted.

```shell
gcloud projects create
gcloud app create [--region=REGION]
gcloud projects delete
```

## References

- [Data sovereignty](https://en.wikipedia.org/wiki/Data_sovereignty)
- [GDPR General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
- [App Engine location](https://cloud.google.com/about/locations#europe)
- [Setting up your Google Cloud project for App Engine](https://cloud.google.com/appengine/docs/standard/go/console)
