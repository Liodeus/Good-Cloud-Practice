# gce_firewallrule_log

## Background

Firewall Rules Logging allows you to audit, verify, and analyze the effects of your firewall rules.
Firewall rules logging must be activated.

## Fix

```shell
gcloud compute firewall-rules update NAME --enable-logging --logging-metadata=LOGGING_METADATA
```

## References

- [Firewall Rules Logging overview](https://cloud.google.com/vpc/docs/firewall-rules-logging)
- [Using Firewall Rules Logging](https://cloud.google.com/vpc/docs/using-firewall-rules-logging)
