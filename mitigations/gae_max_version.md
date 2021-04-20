# gae_max_version

## Background

Multiple versions of your application can be deployed on App Engine. Traffic can be split beetween vesions to test a new release and than make it effective. Old versions that are not more needed should be deleted to keep the environment clean and avoid mistakes.

When you have specified two or more versions for splitting, you must choose whether to split traffic.

GAE applications' services should not have more than 2 versions.

## Fix

```shell
gcloud app versions list
gcloud app services describe
gcloud app services set-traffic --splits=
gcloud app versions delete VERSIONS
```

## References

- [Deploying Versions of Your App to App Engine](https://cloud.google.com/appengine/docs/admin-api/deploying-apps)
- [gcloud app versions](https://cloud.google.com/sdk/gcloud/reference/app/versions)
- [gcloud app services](https://cloud.google.com/sdk/gcloud/reference/app/services)
