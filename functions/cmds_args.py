from functions.clouddns_checks import *
from functions.cloudsql_checks import *
from functions.gae_checks import *
from functions.gce_checks import *
from functions.bq_checks import *
from functions.gcf_checks import *
from functions.gcf_checks import *
from functions.gcs_checks import *
from functions.kms_checks import *
from functions.report.report import *
from concurrent.futures import ThreadPoolExecutor, as_completed


command_lines = {
	"BQ": {
		"DATASET_LOCATION": [
			"bq ls",
			"bq show --format=prettyjson "
		]
	},
	"DNS": {
		"DNSSEC": [
			"gcloud dns managed-zones list --uri",
			"gcloud dns managed-zones describe"
		],
		"RSASHA1": [
			"gcloud dns managed-zones list --uri",
			"gcloud dns managed-zones describe"
		]
	},
	"GAE": {
		"ENV_SECRET": [
			"gcloud app versions list",
			"gcloud app versions describe --service="
		],
		"MAX_VERSION": [
			"gcloud app versions list"
		],
		"LOCATION": [
			"gcloud app describe"
		],
		"RUNTIME": [
			"gcloud app versions list",
			"gcloud app versions describe --service="
		],
	},
	"GCE": {
		"DISK_LOCATION": [
			# "gcloud compute disks list --format=\"value(name.basename(),LOCATION.basename())\""
			"gcloud compute disks list",
		],
		"FIREWALLRULE_LOG": [
			"gcloud compute firewall-rules list --format=json"
		],
		"INSTANCE_EXTERNALIP": [
			# "gcloud compute instances list --format=\"value(name.basename(), ZONE.basename(), EXTERNAL_IP.basename())\""
			"gcloud compute instances list"
		],
		"INSTANCE_LOCATION": [
			# "gcloud compute instances list --format=\"value(name.basename(), ZONE.basename(), EXTERNAL_IP.basename())\""
			"gcloud compute instances list"
		],
		"INSTANCE_SERVICE": [
			# "gcloud compute instances list --format=\"value(name.basename(), ZONE.basename(), EXTERNAL_IP.basename())\""
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"IP_FORWARDING": [
			# "gcloud compute instances list --format=\"value(name.basename(), ZONE.basename(), EXTERNAL_IP.basename())\""
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"NETWORK_NAME": [
			# "gcloud compute instances list --format=\"value(name.basename(), ZONE.basename(), EXTERNAL_IP.basename())\""
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"SHIELDED_ISNTANCES": [
			# "gcloud compute instances list --format=\"value(name.basename(), ZONE.basename(), EXTERNAL_IP.basename())\""
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"NAT_LOCATION": [
			# "gcloud compute routers list --format=\"value(name.basename(), REGION.basename())\""
			"gcloud compute routers list"
		],
		"FIREWALLRULE_TRAFFIC": [
			# "gcloud compute firewall-rules list --format=\"value(name.basename(),logConfig.basename())\""
			"gcloud compute firewall-rules list --format=json"
		],
		"NAT_LOG": [
			# "gcloud compute routers list --format=\"value(name.basename(), REGION.basename())\""
			"gcloud compute routers list",
			# "gcloud compute routers nats list --router nat-router-web --region=us-central1 --format=\"value(name.basename())\""
			"gcloud compute routers nats list --router",
			# "gcloud compute routers nats describe nat-us-central-webservice --router nat-router-web --region=us-central1 --format=\"value(logConfig.basename())\""
			"gcloud compute routers nats describe"
		],
		"HTTPS_SSL_PROXY": [
			# "gcloud compute target-https-proxies list --format=\"value(name.basename())\""
			"gcloud compute target-https-proxies list",
			# "gcloud compute target-https-proxies describe webserver-https-lb-target-proxy-2 --format=\"value(sslPolicy.basename())\""
			"gcloud compute target-https-proxies describe"
		],
		"SSL_SSL_PROXY": [
			# "gcloud compute target-ssl-proxies list --format=\"value(name.basename())\""
			"gcloud compute target-ssl-proxies list",
			# "gcloud compute target-ssl-proxies describe webserver-https-lb-target-proxy-2 --format=\"value(sslPolicy.basename())\""
			"gcloud compute target-ssl-proxies describe"
		]
	},
	"GCF": {
		"ENV_SECRET": [
			# "gcloud functions list --format=\"value(name.basename(), REGION.basename())\""
			"gcloud functions list",
			# "gcloud functions describe --region=us-central1 function-1 --format=\"value(environmentVariables.basename())\""
			"gcloud functions describe --region="
		],
		"LOCATION": [
			# "gcloud functions list --format=\"value(name.basename(), REGION.basename())\""
			"gcloud functions list",
		],
		"RUNTIME": [
			# "gcloud functions list --format=\"value(name.basename(), REGION.basename())\""
			"gcloud functions list",
			# "gcloud functions describe --region=us-central1 function-1 --format=\"value(runtime.basename())\""
			"gcloud functions describe --region="
		],
		"SERVICE_ACCOUNT": [
			# "gcloud functions list --format=\"value(name.basename(), REGION.basename())\""
			"gcloud functions list",
			# "gcloud functions describe --region=us-central1 function-1 --format=\"value(serviceAccountEmail.basename())\""
			"gcloud functions describe --region="
		],
	},
	"CLOUDSQL": {
		"BACKUP": [
			"gcloud sql instances list",
			"gcloud sql instances describe "
		],
		"BACKUP_LOCATION": [
			"gcloud sql instances list",
			"gcloud sql instances describe "
		],
		"LOCATION": [
			"gcloud sql instances list"
		],
		"MAINTENANCE": [
			"gcloud sql instances list",
			"gcloud sql instances describe "
		],
	},
	"GCS": {
		"LOCATION": [
			"gsutil ls",
			"gsutil ls -L -b"
		],
	},
	"KMS": {
		"ROTATION_PERIOD": [
			# "gcloud kms locations list --format=\"value(location_id.basename())\""
			"gcloud kms locations list",
			# "gcloud kms keyrings list --location=asia-east1 --format=\"value(name.basename()\)""
			"gcloud kms keyrings list --location=",
			# "gcloud kms keys list --keyring=test --location=global --format=\"value(name)\""
			"gcloud kms keys list --keyring",
			# "gcloud kms keys describe projects/mystic-sun-309920/locations/asia-east1/keyRings/test2/cryptoKeys/test2 --format=\"value(rotationPeriod)\""
			"gcloud kms keys describe"
		],
	}
}


def launch(REPORT, speed, projects_list=[]):
	thr_list = []
	date_of_scan, report_folder_name = create_folders()

	global_heights = {
		"severity": [],
		"types": []
	}
	
	get_vuln_number()
	user = print_current_user()
	for project in projects_list:
		lock = threading.Lock()
		if change_project(project):
			functions = {
				kms_max_rotation_period: (command_lines["KMS"]["ROTATION_PERIOD"], REPORT, lock, project), # very long to run
				gce_instance_externalip: (command_lines["GCE"]["INSTANCE_EXTERNALIP"], REPORT, lock, project),
				gce_instance_location: (command_lines["GCE"]["INSTANCE_EXTERNALIP"], REPORT, lock, project),
				gce_instance_service_account: (command_lines["GCE"]["INSTANCE_SERVICE"], REPORT, lock, project),
				gce_ip_forwarding: (command_lines["GCE"]["IP_FORWARDING"], REPORT, lock, project),
				gce_network_name: (command_lines["GCE"]["NETWORK_NAME"], REPORT, lock, project),
				gce_shielded_instances: (command_lines["GCE"]["INSTANCE_SERVICE"], REPORT, lock, project),
				gae_runtime: (command_lines["GAE"]["RUNTIME"], REPORT, lock, project),
				gae_env_secret: (command_lines["GAE"]["ENV_SECRET"], REPORT, lock, project),
				clouddns_dnssec: (command_lines["DNS"]["DNSSEC"], REPORT, lock, project),
				clouddns_rsasha1: (command_lines["DNS"]["RSASHA1"], REPORT, lock, project),
				gae_max_version: (command_lines["GAE"]["MAX_VERSION"], REPORT, lock, project),
				gae_location: (command_lines["GAE"]["LOCATION"], REPORT, lock, project),
				gce_disk_location: (command_lines["GCE"]["DISK_LOCATION"], REPORT, lock, project),
				gce_firewallrule_log: (command_lines["GCE"]["FIREWALLRULE_LOG"], REPORT, lock, project),
				bq_dataset_location: (command_lines["BQ"]["DATASET_LOCATION"], REPORT, lock, project),
				gcf_env_secret: (command_lines["GCF"]["ENV_SECRET"], REPORT, lock, project),
				gcf_location: (command_lines["GCF"]["LOCATION"], REPORT, lock, project),
				gcf_runtime: (command_lines["GCF"]["RUNTIME"], REPORT, lock, project),
				gcf_service_account: (command_lines["GCF"]["SERVICE_ACCOUNT"], REPORT, lock, project),
				cloudsql_backup: (command_lines["CLOUDSQL"]["BACKUP"], REPORT, lock, project),
				cloudsql_backup_location: (command_lines["CLOUDSQL"]["BACKUP_LOCATION"], REPORT, lock, project),
				cloudsql_location: (command_lines["CLOUDSQL"]["LOCATION"], REPORT, lock, project),
				cloudsql_maintenance: (command_lines["CLOUDSQL"]["MAINTENANCE"], REPORT, lock, project),
				gce_router_nat_location: (command_lines["GCE"]["NAT_LOCATION"], REPORT, lock, project),
				gcs_storage_location: (command_lines["GCS"]["LOCATION"], REPORT, lock, project),
				gce_firewallrule_traffic: (command_lines["GCE"]["FIREWALLRULE_TRAFFIC"], REPORT, lock, project),
				gce_router_nat_log: (command_lines["GCE"]["NAT_LOG"], REPORT, lock, project),
				gce_target_https_proxy_ssl_policy: (command_lines["GCE"]["HTTPS_SSL_PROXY"], REPORT, lock, project),
				gce_target_ssl_proxy_ssl_policy: (command_lines["GCE"]["SSL_SSL_PROXY"], REPORT, lock, project),
			}
			with ThreadPoolExecutor(max_workers=speed) as executor:
				futures = {executor.submit(function, *parameters) for function, parameters in functions.items()}

				# for f in as_completed(futures):
				# 	f.result()

			height_severity, height_types = print_non_compliance_summary()
			global_heights["severity"].append(height_severity)
			global_heights["types"].append(height_types)
			genereta_graph_by_severity(height_severity, project, report_folder_name, True)
			genereta_graph_by_types(height_types, project, report_folder_name, True)

	if len(global_heights["severity"]) > 1:
		genereta_graph_by_severity([sum(x) for x in zip(*global_heights["severity"])], project, report_folder_name, False)
		genereta_graph_by_types([sum(x) for x in zip(*global_heights["types"])], project, report_folder_name, False)

	generate_html(date_of_scan, user, report_folder_name, global_heights)
	print(f"The report is here : {report_folder_name}/report.html")


def get_vuln_number():
	"""
		Print the number of checks
	"""
	for key, value in command_lines.items():
		if len(key) < 8:
			print(f"{key} checks :\t\t {len(value)}")
		else:
			print(f"{key} checks :\t {len(value)}")
	print()
