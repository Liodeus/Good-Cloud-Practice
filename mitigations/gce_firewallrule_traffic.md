# gce_firewallrule_traffic

## Background

Firewall rules apply to both outgoing (egress) and incoming (ingress) traffic in the network. Firewall rules control traffic even if it is entirely within the network, including communication among VM instances.

Firewall rules allowing source range 0.0.0.0/0 are forbidden.

## Fix

```shell
gcloud compute firewall-rules delete [FIREWALL-RULE-NAME]
```

## References

- [VPC firewall rules overview](https://cloud.google.com/vpc/docs/firewalls)
- [Using firewall rules](https://cloud.google.com/vpc/docs/using-firewalls)
