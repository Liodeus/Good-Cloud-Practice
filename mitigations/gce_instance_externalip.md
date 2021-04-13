# gce_instance_externalip

## Background

Avoid public IP addresses on Compute engine instances (VMs) significantly reduces the attack surface.

External IPs for GCE VMs are forbidden.

Instances without a IP addresses can be accessed from the internal network (VPN, Interconnect) or using IAP tunnels, or behing load balancers.

## Fix

```shell
gcloud compute instances delete-access-config INSTANCE_NAME --zone=ZONE -- access-config-name "ACCESS_CONFIG_NAME"
```

## References

- [Unassigning a static external IP address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#unassign_ip)
- [Connecting to instances](https://cloud.google.com/compute/docs/instances/connecting-to-instance)
- [Connecting to instances that do not have external IP addresses](https://cloud.google.com/compute/docs/instances/connecting-advanced#sshbetweeninstances)
- [Connecting to instances using advanced methods](https://cloud.google.com/compute/docs/instances/connecting-advanced)
- [Backend services overview](https://cloud.google.com/load-balancing/docs/backend-service#backends_and_external_ip_addresses)
- [IAP tunnels - overview of TCP forwarding](https://cloud.google.com/iap/docs/tcp-forwarding-overview)
