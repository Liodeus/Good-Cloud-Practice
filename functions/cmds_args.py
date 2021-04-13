from functions.dns_checks import *
from functions.gae_checks import *
from functions.gce_checks import *
from functions.bq_checks import *
from functions.gcf_checks import *
import threading


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
	}
}


def launch(REPORT, projects_list=[]):
	thr_list = []

	get_vuln_number()
	print_current_user()
	for project in projects_list:
		if change_project(project):
			functions = {
				gce_instance_externalip: (command_lines["GCE"]["INSTANCE_EXTERNALIP"], REPORT),
				gce_instance_location: (command_lines["GCE"]["INSTANCE_EXTERNALIP"], REPORT),
				gce_instance_service_account: (command_lines["GCE"]["INSTANCE_SERVICE"], REPORT),
				gce_ip_forwarding: (command_lines["GCE"]["IP_FORWARDING"], REPORT),
				gce_network_name: (command_lines["GCE"]["NETWORK_NAME"], REPORT),
				gce_shielded_instances: (command_lines["GCE"]["INSTANCE_SERVICE"], REPORT),
				gae_runtime: (command_lines["GAE"]["RUNTIME"], REPORT),
				gae_env_secret: (command_lines["GAE"]["ENV_SECRET"], REPORT),
				clouddns_dnssec: (command_lines["DNS"]["DNSSEC"], REPORT),
				clouddns_rsasha1: (command_lines["DNS"]["RSASHA1"], REPORT),
				gae_max_version: (command_lines["GAE"]["MAX_VERSION"], REPORT),
				gae_location: (command_lines["GAE"]["LOCATION"], REPORT),
				gce_disk_location: (command_lines["GCE"]["DISK_LOCATION"], REPORT),
				gce_firewallrule_log: (command_lines["GCE"]["FIREWALLRULE_LOG"], REPORT),
				bq_dataset_location: (command_lines["BQ"]["DATASET_LOCATION"], REPORT),
				gcf_env_secret: (command_lines["GCF"]["ENV_SECRET"], REPORT),
				gcf_location: (command_lines["GCF"]["LOCATION"], REPORT),
				gcf_runtime: (command_lines["GCF"]["RUNTIME"], REPORT),
				gcf_service_account: (command_lines["GCF"]["SERVICE_ACCOUNT"], REPORT),
			}

			for function, parameters in functions.items():
				thr = threading.Thread(target=function, args=parameters)
				thr_list.append(thr)
				thr.start()

			for index, thread in enumerate(thr_list):
				thread.join()

			print_non_compliance_summary()


def get_vuln_number():
	"""
		Print the number of checks
	"""
	for key, value in command_lines.items():
		print(f"{key} checks :\t {len(value)}")
	print()
