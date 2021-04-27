# gce_target_https_proxy_ssl_policy

## Background

HTTPS Proxy Load Balancer should have a SSL Policy defined.
SSL policies give you the ability to control the features of SSL that your SSL proxy load balancer or external HTTP(S) load balancer negotiates with clients, such has minimal SSL/TLS version or available ciphers.
It is therefore required to define a SSL Policy (with any settings) to ensure that the issue of TLS version and vulnerabilities was reviewed and handled by the asset owner.

## Fix

```shell
# Define a SSL Policy
gcloud compute ssl-policies create NAME --profile MODERN --min-tls-version 1.2

# Attach the policy to your Target SSL Proxy
gcloud compute target-https-proxies update NAME --ssl-policy SSL_POLICY_NAME
```

## References

- [SSL policies overview](https://cloud.google.com/load-balancing/docs/ssl-policies-concepts)
- [Using SSL Policies](https://cloud.google.com/load-balancing/docs/use-ssl-policies)