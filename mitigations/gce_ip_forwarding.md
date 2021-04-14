# gce_ip_forwarding

## Background

GCE Instances should not enable IP Forwarding.

IP Forwarding is a network feature that permits VM intances to forward network traffic between network interfaces and/or networks.
Unless specifically required by a use case, and fully backed-up by firewall and routing configuration no VM instance should enable it, as it can contribute to a successfull network attack.

## Fix

This setting cannot be changed after the instance creation, you must delete it and created a new instance.

## References

- [IP forwarding for instances](https://cloud.google.com/vpc/docs/using-routes#canipforward)
