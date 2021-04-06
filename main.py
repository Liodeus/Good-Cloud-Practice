from functions.dns_checks import *
from functions.gae_checks import *
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
		]
	}
}


def main(REPORT):
	dnssec(command_lines["DNS"]["DNSSEC"], report=REPORT)
	rsasha1(command_lines["DNS"]["RSASHA1"], report=REPORT)
	gae_env_secret(command_lines["GAE"]["ENV_SECRET"], report=REPORT)
	gae_max_version(command_lines["GAE"]["MAX_VERSION"], report=REPORT)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--report', action="store_true", help='Enable report mode')
	args = parser.parse_args()

	if args.report:
		REPORT = True
	else:
		REPORT = False

	main(REPORT)
