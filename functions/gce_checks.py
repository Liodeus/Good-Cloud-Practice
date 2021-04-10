from functions.misc_functions import *


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

	# Print report for gce_firewallrule_log
	report_print("GCE firewallrule_log ", firewall_rule_enable["OFF"], report, mitigation_name, severity)


def gce_disk_location(cmd_list, report="False", severity="Major", mitigation_name="gce_disk_location_mitigation.json"):
	"""
		Test for disk location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')

	if "ERROR:" in datas[0]:
		print("GCE disk location check : x")
		print("\tAn error occured")
		print(f"\t\t{' '.join(datas)}")
		print("**************************************************\n")
		sys.exit()

	disk_location_result = {}
	for data in datas[1:-1]:
		tmp = data.split()
		name = tmp[0]
		location = tmp[1]
		if "europe" not in location:
			disk_location_result[name] = location

	# Print report for gce_disk_location
	report_print("GCE disk location", disk_location_result, report, mitigation_name, severity)


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
	report_print("GCE instance external ip", external_ip_result, report, mitigation_name, severity)


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
	report_print("GCE instance location", location_result, report, mitigation_name, severity)


def gce_instance_service_account(cmd_list, report="False", severity="Major", mitigation_name="gce_instance_service_account_mitigation.json"):
	"""
		Test for instance default account
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]

	location_result = {}
	for data in datas:
		tmp = data.split()
		name = tmp[0]
		location = tmp[1]
		location_result[name] = location
	
	services_account = {}
	for name, location in location_result.items():
		yaml_datas = yaml.load(exec_cmd(f"{cmd_list[1]}{location} {name}"), Loader=yaml.FullLoader)

		email = yaml_datas["serviceAccounts"][0]["email"]

		if re.match("[0-9]*-compute@developer.gserviceaccount.com", email):
			services_account[name] = email

	# Print report for gce_instance_service_account
	report_print("GCE instance service account", services_account, report, mitigation_name, severity)


def gce_ip_forwarding(cmd_list, report="False", severity="Critical", mitigation_name="gce_ip_forwarding_mitigation.json"):
	"""
		Test for 
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]

	location_result = {}
	for data in datas:
		tmp = data.split()
		name = tmp[0]
		location = tmp[1]
		location_result[name] = location
	
	services_account = {}
	for name, location in location_result.items():
		yaml_datas = yaml.load(exec_cmd(f"{cmd_list[1]}{location} {name}"), Loader=yaml.FullLoader)

		forward = yaml_datas["canIpForward"]

		if not forward:
			services_account[name] = forward

	# Print report for gce_instance_service_account
	report_print("GCE instance IP forwarding", services_account, report, mitigation_name, severity)
		

def gce_network_name(cmd_list, report="False", severity="Major", mitigation_name="gce_network_name_mitigation.json"):
	"""
		Test for 
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]

	location_result = {}
	for data in datas:
		tmp = data.split()
		name = tmp[0]
		location = tmp[1]
		location_result[name] = location
	
	network_default = {}
	for name, location in location_result.items():
		yaml_datas = yaml.load(exec_cmd(f"{cmd_list[1]}{location} {name}"), Loader=yaml.FullLoader)

		network = yaml_datas["networkInterfaces"][0]["network"].split('/')[-1]

		if network == "default":
			network_default[name] = network

	# Print report for gce_network_name
	report_print("GCE instance instance default network", network_default, report, mitigation_name, severity)


def gce_shielded_instances(cmd_list, report="False", severity="Minor", mitigation_name="gce_shielded_instances_mitigation.json"):
	"""
		Test if enableIntegrityMonitoring, enableSecureBoot,enableVtpm are enable on GCE instances
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]

	location_result = {}
	for data in datas:
		tmp = data.split()
		name = tmp[0]
		location = tmp[1]
		location_result[name] = location
	
	shield_result = {}
	for name, location in location_result.items():
		yaml_datas = yaml.load(exec_cmd(f"{cmd_list[1]}{location} {name}"), Loader=yaml.FullLoader)

		shield_config = yaml_datas["shieldedInstanceConfig"]
		for value in shield_config.values():
			if not value:
				shield_result[name] = shield_config
				break

	# Print report for gce_shielded_instances
	report_print("GCE instance shielding", shield_result, report, mitigation_name, severity)
