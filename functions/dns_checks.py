from functions.misc_functions import *


def dnssec(cmd_list, report="False", severity="Major", mitigation_name="dnssec_mitigation.json"):
	"""
		Test for DNSSEC security
	"""
	datas = exec_cmd(cmd_list[0]).split()

	if datas[0] == "API":
		print("DNSSEC check : x")
		print("\tAPI [dns.googleapis.com] not enabled\n")
		print("*************************\n")
		sys.exit()

	if datas[0] == "Listed":
		print("DNSSEC check : ✓\n")
		print("*************************\n")
	else:
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

		# Print report for DNSSEC
		if dnssec_results["off"]:
			print("DNSSEC check : x")
			print("\tInformation :")
			str_tmp = "\t\t\t".join(f"{x}\n" for x in dnssec_results["off"])
			print(f"\t\tDNSSEC has not been enabled for : \n\t\t\t{str_tmp}")

			# Print report for DNSSEC
			print_report(report, mitigation_name)

		else:
			print("DNSSEC check : ✓\n")
			print("*************************\n")


def rsasha1(cmd_list, report="False", severity="Critical", mitigation_name="rsasha1_mitigation.json"):
	"""
		Test for DNSSEC RSASHA1 weak algorithm
	"""
	datas = exec_cmd(cmd_list[0]).split()

	if datas[0] == "API":
		print("RSASHA1 check : x")
		print("\tAPI [dns.googleapis.com] not enabled\n")
		print("*************************\n")
		sys.exit()

	managed_zones = [x.split('/')[-1] for x in datas]

	managed_zones_results = {}
	for zone in managed_zones:
		managed_zones_results[zone] = exec_cmd(f"{cmd_list[1]} {zone}")

	# RSASHA1 check
	rsasha1_results = {"off": [], "on": []}
	for zone, result in managed_zones_results.items():
		if "algorithm: RSASHA1" in result:
			rsasha1_results["on"].append(zone)
		else:
			rsasha1_results["off"].append(zone)

	# Print report for RSASHA1
	if rsasha1_results["on"]:
		print("RSASHA1 check : ✓\n")
		print("\tInformation :")
		str_tmp = ", ".join(x for x in rsasha1_results["on"])
		print(f"\t\tDNSSEC has weak RSASHA1 algorithm enabled : {str_tmp}\n")

		# Print report for RSASHA1
		print_report(report, mitigation_name)

	else:
		print("RSASHA1 check : ✓\n")
		print("*************************\n")