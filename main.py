from functions.dns_checks import *
from functions.gae_checks import *
from functions.misc_functions import get_project_list
import argparse


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
	}
}

def launch(REPORT, projects_list=[]):
	for project in projects_list:
		change_project(project)
		dnssec(command_lines["DNS"]["DNSSEC"], report=REPORT)
		rsasha1(command_lines["DNS"]["RSASHA1"], report=REPORT)
		gae_env_secret(command_lines["GAE"]["ENV_SECRET"], report=REPORT)
		gae_max_version(command_lines["GAE"]["MAX_VERSION"], report=REPORT)
		gae_location(command_lines["GAE"]["LOCATION"], report=REPORT)
		gae_runtime(command_lines["GAE"]["RUNTIME"], report=REPORT)


def main(REPORT, project_id=None):
	projects_list = get_project_list()

	if project_id == None:
		launch(REPORT, projects_list)
	elif project_id in projects_list:
		launch(REPORT, [project_id])
	else:
		print(f"You do not appear to have access to project [{project_id}] or it does not exist.")
		exit()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--report', action="store_true", help='Enable report mode')
	parser.add_argument('--list_projects', "-lp", action="store_true", help='List projects')
	parser.add_argument('--list_users', "-lu", action="store_true", help='List users')
	parser.add_argument('--project_id', required=False, help='Do the checks on this project-id')
	args = parser.parse_args()

	if args.list_projects:
		list_projects()
	elif args.list_users:
		list_users()
	main(args.report, args.project_id)

