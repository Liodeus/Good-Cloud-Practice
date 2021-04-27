# gce_router_nat_log

## Background

GCE Cloud Router / Cloud NAT must log ALL requests

For accountability issues and to help troubleshooting, Cloud Router's NATs should have logging enabled and log all events, translations AND errors.

## Fix

```shell
gcloud compute routers nats update NAT_GATEWAY --router=ROUTER_NAME --region=REGION --log-filter=ALL
```

## References

- [Cloud NAT, Using Logging and Monitoring](https://cloud.google.com/nat/docs/monitoring)
