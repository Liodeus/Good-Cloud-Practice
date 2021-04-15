from functions.misc_functions import *


def clouddns_dnssec(cmd_list, report="False", lock="", severity="Major", mitigation_name="clouddns_dnssec.md"):
	"""
		Test for DNSSEC security
	"""
	datas = exec_cmd(cmd_list[0]).split()

	if datas[0] == "API":
		error_api_not_enabled(lock, "Cloud DNS DNSSEC", "API [dns.googleapis.com] not enabled")

	if datas[0] == "Listed":
		lock.acquire()
		print(f"Cloud DNS DNSSEC check : {Fore.GREEN}✓{Style.RESET_ALL}\n")
		lock.release()
		print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
	else:
		managed_zones = [x.split('/')[-1] for x in datas]

		managed_zones_results = {}
		for zone in managed_zones:
			managed_zones_results[zone] = exec_cmd(f"{cmd_list[1]} {zone}")

		# DNSSEC check
		dnssec_results = {}
		for zone, result in managed_zones_results.items():
			if "state: off" in result or "state" not in result:
				dnssec_results[zone] = "OFF"

		# Print report for DNSSEC
		report_print("Cloud DNS DNSSEC check", dnssec_results, report, mitigation_name, severity, lock)


def clouddns_rsasha1(cmd_list, report="False", lock="", severity="Critical", mitigation_name="clouddns_rsasha1.md"):
	"""
		Test for DNSSEC RSASHA1 weak algorithm
	"""
	datas = exec_cmd(cmd_list[0]).split()

	if datas[0] == "API":
		error_api_not_enabled(lock, "Cloud DNS RSASHA1", "API [dns.googleapis.com] not enabled")

	managed_zones = [x.split('/')[-1] for x in datas]

	managed_zones_results = {}
	for zone in managed_zones:
		managed_zones_results[zone] = exec_cmd(f"{cmd_list[1]} {zone}")

	rsasha1_results = {}
	for key, value in managed_zones_results.items():
		if "algorithm: RSASHA1" in value:
			rsasha1_results[key] = "RSASHA1"

	# Print report for RSASHA1
	report_print("Cloud DNS RSASHA1 check", rsasha1_results, report, mitigation_name, severity, lock)
