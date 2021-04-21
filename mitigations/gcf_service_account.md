# gcf_service_account

## Background

Cloud Functions use service accounts to run.

Per default, a Cloud Function uses the service account {project-id}@@appspot.gserviceaccount.com. This service account is the app engine default service account for the project, who by default has the Editor role on the project.

This means that by default, every Cloud Function in the project runs with editor rights on the project. Should an Function be compromised, malicious activity would have editor role : all data in the project could be accessible (data leak risk), new ressources could be created (financial risk) or illegal activity could be carried out (liability risk).

## Fix

```shell
# Create a specfic service account for your instance
gcloud iam service-accounts create SERVICE_ACCOUNT_ID --description="DESCRIPTION" --display-name="DISPLAY_NAME"

# Grant only required roles to service accounts !!! Exemple for BQ streaming :
gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com" --role="roles/bigquery.dataEditor"

# Even better, you can create a Custom Role for your Cloud Function, see https://cloud.google.com/iam/docs/creating-custom-roles
# Deploy your Cloud Function using new service account
gcloud functions deploy FUNCTION_NAME --service-account SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com
```

## References

- [Service Accounts guide for Compute Engine](https://cloud.google.com/compute/docs/access/service-accounts)
- [Creating a service account](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount)
- [Granting access](https://cloud.google.com/iam/docs/granting-changing-revoking-access#granting_access_to_a_service_account_for_a_resource)
- [Creating Custom Roles](https://cloud.google.com/iam/docs/creating-custom-roles)
- [Function identity](https://cloud.google.com/functions/docs/securing/function-identity)
