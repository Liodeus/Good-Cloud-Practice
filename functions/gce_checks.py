from functions.misc_functions import *
import json

def gce_firewallrule_log(cmd_list, report="False", severity="Medium", mitigation_name="gce_firewallrule_log_mitigation.json"):
	"""
		Test if firewall rule are enable
	"""
	datas = json.loads(exec_cmd(cmd_list[0]))

	firewall_rule_enable = {
		"ON": {},
		"OFF": {}
	}
	
	for data in datas:
		state = data["logConfig"]["enable"]
		name = data["name"]

		if not state:
			firewall_rule_enable["OFF"][name] = state
		else:
			firewall_rule_enable["ON"][name] = state

	if firewall_rule_enable["OFF"]:
		print("GCE firewallrule_log : x")
		print("\tInformation :")
		print(f"\t\tGoogle Compute Engine firewallrule log not enable :")
		for rule in firewall_rule_enable["OFF"]:
			print(f"\t\t\t{rule} -> Not enable")

		# Print report for gce_firewallrule_log
		print_report(report, mitigation_name)

	else:
		print("GCE firewallrule log : ✓\n")
		print("*************************\n")


def gce_disk_location(cmd_list, report="False", severity="Major", mitigation_name="gce_disk_location_mitigation.json"):
	"""
		Test for disk location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')

	if "ERROR:" in datas[0]:
		print("GCE disk location check : x")
		print("\tAn error occured")
		print(f"\t\t{' '.join(datas)}")
		print("*************************\n")
		sys.exit()


	disk_location_result = {}
	for data in datas[1:-1]:
		tmp = data.split()
		name = tmp[0]
		location = tmp[1]
		if "europe" not in location:
			disk_location_result[name] = location

	# Print report for gce_disk_location
	if disk_location_result:
		print("GCE disk location check : x")
		print("\tInformation :")
		print(f"\t\tGoogle Compute Engine disk location :")
		for key, value in disk_location_result.items():
			print(f"\t\t\t{key} : {value}")

		# Print report for gce_disk_location
		print_report(report, mitigation_name)

	else:
		print("GCE disk location : ✓\n")
		print("*************************\n")


def gce_instance_externalip(cmd_list, report="False", severity="Major", mitigation_name="gce_instance_externalip_mitigation.json"):
	"""
		Test for external ip on GCE instance
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]
	
	external_ip_result = {}
	for data in datas:
		tmp = data.split()
		name = tmp[0]
		external_ip = tmp[4]

		if external_ip != "TERMINATED":
			external_ip_result[name] = external_ip


	# Print report for gce_instance_externalip
	if external_ip_result:
		print("GCE instance external ip check : x")
		print("\tInformation :")
		print(f"\t\tGoogle Compute Engine instance external ip :")
		for key, value in external_ip_result.items():
			print(f"\t\t\t{key} : {value}")

		# Print report for gce_instance_externalip
		print_report(report, mitigation_name)

	else:
		print("GCE instance external ip : ✓\n")
		print("*************************\n")



def gce_instance_location(cmd_list, report="False", severity="Major", mitigation_name="gce_instance_location_mitigation.json"):
	"""
		Test for instance location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]

	location_result = {}
	for data in datas:
		tmp = data.split()
		name = tmp[0]
		location = tmp[1]
		if "europe" not in location:
			location_result[name] = location
	
	# Print report for gce_disk_location
	if location_result:
		print("GCE instance location check : x")
		print("\tInformation :")
		print(f"\t\tGoogle Compute Engine instance location :")
		for key, value in location_result.items():
			print(f"\t\t\t{key} : {value}")

		# Print report for gce_instance_location
		print_report(report, mitigation_name)

	else:
		print("GCE instance location : ✓\n")
		print("*************************\n")

