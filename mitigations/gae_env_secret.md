# gae_env_secrets

## Background

Google AppEngine can use environment variables, defined its app.yaml configuration file.
These variables are not secret, and can be accessed in multiple way.
Sensitive information should not be avaible in application source code, but stored securily and accessed when required.

## Fix

Use Google Secret Manager to store sensitive information and use code in your application to acces it. Secret Manager Client libraries exist for all GAE runtime environment.

## References

- [Cloud Secret Manager](https://cloud.google.com/secret-manager/docs)
- [Using Secret Manager Client library](https://cloud.google.com/secret-manager/docs/reference/libraries#using_the_client_library)
