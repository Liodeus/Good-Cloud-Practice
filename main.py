from functions.security_check_functions import *
import argparse


command_lines = {
	"DNS": {
		"DNSSEC": [
			"gcloud dns managed-zones list --uri",
			"gcloud dns managed-zones describe"
		]
	}
}


def main(REPORT):
	dnssec_rsasha1(command_lines["DNS"]["DNSSEC"], report=REPORT)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--report', action="store_true", help='Enable report mode')
	args = parser.parse_args()

	if args.report:
		REPORT = True
	else:
		REPORT = False

	main(REPORT)
