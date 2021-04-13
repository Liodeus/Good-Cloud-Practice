# clouddns_rsasha1

## Background

When enabling DNSSEC for a managed zone, or creating a managed zone with DNSSEC, you can select the DNSSEC signing algorithms and the denial-of-existence type.

Weak Algorithm SHA1 is forbidden on CloudDNS DNSSec

Changing the DNSSEC settings is only effective for a managed zone if DNSSEC is not already enabled. If there is a need to change the settings for a managed zone where it has been enabled, turn DNSSEC off and then re-enable it with different settings.

KSK Key Signing Key
ZSK Zone Signing Key

**WARNING** RSASHA1 is disable by default. Use the quotas request process to be whitelisted (on exception), Then customize the scope of this rule using exclusions.

## Fix

```shell
gcloud dns managed-zones update ZONE_NAME --dnssec-state off

gcloud dns managed-zones update ZONE_NAME --dnssec-state on --ksk-algorithm KSK_ALGORITHM --ksk-key-length KSK_KEY_LENGTH --zsk-algorithm ZSK_ALGORITHM - -zsk-key-length ZSK_KEY_LENGTH --denial-of-existence DENIAL_OF_EXISTENCE
```

## References

- [DNSSEC Advanced signing options](https://cloud.google.com/dns/dnssec-advanced#advanced_signing_options)
