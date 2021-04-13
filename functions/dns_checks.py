from functions.misc_functions import *


def clouddns_dnssec(cmd_list, report="False", severity="Major", mitigation_name="clouddns_dnssec.md"):
	"""
		Test for DNSSEC security
	"""
	datas = exec_cmd(cmd_list[0]).split()

	if datas[0] == "API":
		print(f"DNSSEC check : {Fore.RED}x{Style.RESET_ALL}")
		print("\tAPI [dns.googleapis.com] not enabled\n")
		print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
		sys.exit()

	if datas[0] == "Listed":
		print(f"DNSSEC check : {Fore.GREEN}✓{Style.RESET_ALL}\n")
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
		report_print("DNSSEC check", dnssec_results, report, mitigation_name, severity)


def clouddns_rsasha1(cmd_list, report="False", severity="Critical", mitigation_name="clouddns_rsasha1.md"):
	"""
		Test for DNSSEC RSASHA1 weak algorithm
	"""
	datas = exec_cmd(cmd_list[0]).split()

	if datas[0] == "API":
		print("clouddns rsasha1 check : x")
		print("\tAPI [dns.googleapis.com] not enabled\n")
		print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
		sys.exit()

	managed_zones = [x.split('/')[-1] for x in datas]

	managed_zones_results = {}
	for zone in managed_zones:
		managed_zones_results[zone] = exec_cmd(f"{cmd_list[1]} {zone}")

	rsasha1_results = {}
	for key, value in managed_zones_results.items():
		if "algorithm: RSASHA1" in value:
			rsasha1_results[key] = "RSASHA1"

	# Print report for RSASHA1
	report_print("clouddns rsasha1 check", rsasha1_results, report, mitigation_name, severity)
