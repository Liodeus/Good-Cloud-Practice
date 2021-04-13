# monitor_gcf_runtime gcf_runtime

## Background

Cloud Functions supports multiple language runtimes.

Deprecated runtimes no longer receive bugfixes or security patches and may expose vulnerabilities.
Using obsolete runtimes creates technical debt and should be avoided.

So, only non-deprecated and sanctionned runtimes are allowed.

## Fix

This setting cannot be changed after the cloud function creation, you must delete it and re-deploy it with an approved runtime (*).
*: this may require porting the code to another programming language

## References

- [Cloud Functions Execution Environment](https://cloud.google.com/functions/docs/concepts/exec)
