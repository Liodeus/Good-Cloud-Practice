from functions.clouddns_checks import *
from functions.cloudsql_checks import *
from functions.gae_checks import *
from functions.gce_checks import *
from functions.bq_checks import *
from functions.gcf_checks import *
from functions.gcf_checks import *
from functions.gcs_checks import *
from functions.report.report import *


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
			"gcloud compute disks list",
		],
		"FIREWALLRULE_LOG": [
			"gcloud compute firewall-rules list --format=json"
		],
		"INSTANCE_EXTERNALIP": [
			"gcloud compute instances list"
		],
		"INSTANCE_LOCATION": [
			"gcloud compute instances list"
		],
		"INSTANCE_SERVICE": [
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"IP_FORWARDING": [
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"NETWORK_NAME": [
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"SHIELDED_ISNTANCES": [
			"gcloud compute instances list",
			"gcloud compute instances describe --zone="
		],
		"NAT_LOCATION": [
			"gcloud compute routers list"
		]
	},
	"GCF": {
		"ENV_SECRET": [
			"gcloud functions list",
			"gcloud functions describe --region="
		],
		"LOCATION": [
			"gcloud functions list",
		],
		"RUNTIME": [
			"gcloud functions list",
			"gcloud functions describe --region="
		],
		"SERVICE_ACCOUNT": [
			"gcloud functions list",
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
	}
}


def launch(REPORT, projects_list=[]):
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
			}

			for function, parameters in functions.items():
				thr = threading.Thread(target=function, args=parameters)
				thr_list.append(thr)
				thr.start()

			for index, thread in enumerate(thr_list):
				thread.join()

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
