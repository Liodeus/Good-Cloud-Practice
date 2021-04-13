# monitor_gce_network_name no_default_network

## Background

Default networks should not exists in projects.
The "default" network comes with default firewall rules that allow access from internet to all assets on ports 80 and 443.
The "default" network is also created with the "auto mode" option, which creates a subnetwork in all existing GCP zones.

## Fix

[Delete the network](https://cloud.google.com/vpc/docs/using-vpc#deleting_a_network)

## References

- [GCE VPC Networks](https://cloud.google.com/vpc/docs/vpc)
