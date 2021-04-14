# gcf_env_secrets

## Background

Google CloudFunctions can use environment variables.
These variables are not secret, and can be accessed in multiple way.
Sensitive information should not be avaible in function source code, but stored securily and accessed when required.

## Fix

Use Google Secret Manager to store sensitive information and use code in your function to acces it. Secret Manager Client libraries exist for all GCF runtime environment.

## References

- [Cloud Secret Manager](https://cloud.google.com/secret-manager/docs)
- [Using Secret Manager Client library](https://cloud.google.com/secret-manager/docs/reference/libraries#using_the_client_library)
