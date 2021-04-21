# gce_instance_service_account

## Background

GCE Instances use service accounts to run.

Per default, an instance uses the service account {project_number}-compute@developer.gserviceaccount.com. This service account is the compute engine service account for the project, who by default has the Editor role on the project.

This means that by default, every instance in the project runs with editor rights on the projects. Should an instance be compromized, malicious activity would have editor role : all data in the project could be accessible (data leak risk), new ressources could be created (financial risk) or illegal activity could be carried out (liability risk).

## Fix

```shell
# Create a specfic service account for your instance
gcloud iam service-accounts create SERVICE_ACCOUNT_ID --description="DESCRIPTION" --display-name="DISPLAY_NAME"

# Grant only required roles to service accounts !!! Example with minimal rights !!!
gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com" --role="roles/monitoring.metricWriter"

gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com" --role="roles/logging.logWriter"

# Update your instance to use the new service account
gcloud compute instances set-service-account [INSTANCE_NAME] --service-account SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com
```

## References

- [Service Accounts guide for Compute Engine](https://cloud.google.com/compute/docs/access/service-accounts)
- [Creating a service account](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount)
- [Granting access](https://cloud.google.com/iam/docs/granting-changing-revoking-access#granting_access_to_a_service_account_for_a_resource)
- [Changing the service account for a running instance](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes)
