# kms_max_rotation_period

## Background

Google Cloud Key Management Service stores cryptographic keys in a hierarchical structure designed for useful and elegant access control management.

The format for the rotation schedule depends on the client library that is used. For the gcloud command-line tool, the next rotation time must be in ISO or RFC3339 format, and the rotation period must be in the form INTEGER[UNIT], where units can be one of seconds (s), minutes (m), hours (h) or days (d).

Warning:

- Key rotation does NOT re-encrypt already encrypted data with the newly generated key version. If you suspect unauthorized use of a key, you should re-encrypt the data protected by that key and then disable or schedule destruction of the prior key version.

KMS keys must have a rotation period of a 100 days max.

## Fix

```shell
gcloud kms keys update new --keyring=KEY_RING --location=LOCATION --next-rotation-time=NEXT_ROTATION_TIME --rotation-period=ROTATION_PERIOD
```

## References

- [KMS Key rotation](https://cloud.google.com/kms/docs/key-rotation#frequency_of_key_rotation)
- [KMS Re-encrypting data](https://cloud.google.com/kms/docs/re-encrypt-data)