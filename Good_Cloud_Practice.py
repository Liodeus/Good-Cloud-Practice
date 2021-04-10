from functions.dns_checks import *
from functions.gae_checks import *
from functions.gce_checks import *
import threading
import argparse
import time
import sys


command_lines = {
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
	}
}


def launch(REPORT, projects_list=[]):
	thr_list = []
	print(f"Current user : {get_current_user()}\n")
	for project in projects_list:
		change_project(project)
		functions = {
			gce_instance_externalip: (command_lines["GCE"]["INSTANCE_EXTERNALIP"], REPORT),
			gce_instance_location: (command_lines["GCE"]["INSTANCE_EXTERNALIP"], REPORT),
			gce_instance_service_account: (command_lines["GCE"]["INSTANCE_SERVICE"], REPORT),
			gce_ip_forwarding: (command_lines["GCE"]["IP_FORWARDING"], REPORT),
			gce_network_name: (command_lines["GCE"]["NETWORK_NAME"], REPORT),
			gce_shielded_instances: (command_lines["GCE"]["INSTANCE_SERVICE"], REPORT),
			gae_runtime: (command_lines["GAE"]["RUNTIME"], REPORT),
			gae_env_secret: (command_lines["GAE"]["ENV_SECRET"], REPORT),
			dnssec: (command_lines["DNS"]["DNSSEC"], REPORT),
			rsasha1: (command_lines["DNS"]["RSASHA1"], REPORT),
			gae_max_version: (command_lines["GAE"]["MAX_VERSION"], REPORT),
			gae_location: (command_lines["GAE"]["LOCATION"], REPORT),
			gce_disk_location: (command_lines["GCE"]["DISK_LOCATION"], REPORT),
			gce_firewallrule_log: (command_lines["GCE"]["FIREWALLRULE_LOG"], REPORT),
		}

		for function, parameters in functions.items():
			thr = threading.Thread(target=function, args=parameters)
			thr_list.append(thr)
			thr.start()

		for index, thread in enumerate(thr_list):
			thread.join()


def main(REPORT, project_id=None):
	t0 = time.time()
	projects_list = get_project_list()

	if project_id == None:
		launch(REPORT, projects_list)
	elif project_id in projects_list:
		launch(REPORT, [project_id])
	else:
		print(f"You do not appear to have access to project [{project_id}] or it does not exist.")
		sys.exit()


	print(f"\nThe scan took {round(time.time()-t0)} secondes.")


if __name__ == "__main__":
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--report", action="store_true", help='Enable report mode')
	parser.add_argument( "-lp", "--list_projects", action="store_true", help='List projects')
	parser.add_argument("-lu", "--list_users", action="store_true", help='List users')
	parser.add_argument("--project_id", required=False, help='Do the checks on this project-id')
	args = parser.parse_args()

	if args.list_projects:
		list_projects()
	elif args.list_users:
		list_users()

	try:
		main(args.report, args.project_id)
	except KeyboardInterrupt:
		print("CTRL+C")
		sys.exit()