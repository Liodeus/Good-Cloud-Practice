from functions.misc_functions import *


def dnssec_rsasha1(cmd_list, report="False", severity_dnssec="Major", severity_rsasha1="Critical", mitigation_name_dnssec="dnssec_mitigation.json", mitigation_name_rsasha1="rsasha1_mitigation.json"):
	"""
		Test for DNSSEC and RSASHA1 security
	"""
	datas = exec_cmd(cmd_list[0]).split()
	managed_zones = [x.split('/')[-1] for x in datas]

	managed_zones_results = {}
	for zone in managed_zones:
		managed_zones_results[zone] = exec_cmd(f"{cmd_list[1]} {zone}")

	# DNSSEC check
	dnssec_results = {"off": [], "on": []}
	for zone, result in managed_zones_results.items():
		if "state: off" in result or "state" not in result:
			dnssec_results["off"].append(zone)
		else:
			dnssec_results["on"].append(zone)

	# RSASHA1 check
	rsasha1_results = {"off": [], "on": []}
	for zone, result in managed_zones_results.items():
		if "algorithm: RSASHA1" in result:
			rsasha1_results["on"].append(zone)
		else:
			rsasha1_results["off"].append(zone)

	# Print report for DNSSEC
	if dnssec_results["off"]:
		print("Information :")
		str_tmp = ", ".join(x for x in dnssec_results["off"])
		print(f"\tDNSSEC has not been enabled for : {str_tmp}\n")

		if report:
			mitigation = read_mitigation(mitigation_name_dnssec)
			pretty_print_mitigation(mitigation)
	else:
		print("DNSSEC check : ✓")

	# Print report for RSASHA1
	if rsasha1_results["on"]:
		print("Information :")
		str_tmp = ", ".join(x for x in rsasha1_results["on"])
		print(f"\tDNSSEC has weak RSASHA1 algorithm enabled : {str_tmp}\n")

		if report:
			mitigation = read_mitigation(mitigation_name_rsasha1)
			pretty_print_mitigation(mitigation)
	else:
		print("RSASHA1 check : ✓")