# monitor_gce_shielded_instances gce_shielded_instances

## Background

GCE Instances should enable "Shielded VM" options.

Shielded VM offers verifiable integrity of your Compute Engine VM instances, so you can be confident your instances haven't been compromised by boot- or kernel-level malware or rootkits. Shielded VM's verifiable integrity is achieved through the use of Secure Boot, virtual trusted platform module (vTPM)-enabled Measured Boot, and integrity monitoring.

## Fix

Verify that the Operating System Image of your VM supports the shielded VM dfeature on :
[Operating System details](https://cloud.google.com/compute/docs/images/os-details#general-info)

Then :

```shell
gcloud compute instances stop VM_NAME
gcloud compute instances update VM_NAME \
    --shielded-vtpm \
    --shielded-integrity-monitoring
gcloud compute instances stop VM_NAME
```

If your VM does not support Shielded VM options, you should recreate it with another OS that supports it.

## References

- [GCE Shielded Instances](https://cloud.google.com/security/shielded-cloud/shielded-vm)
- [Modify Shielded VM Options](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm)
