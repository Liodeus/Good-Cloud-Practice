from functions.gce_misc_functions import *


def gce_firewallrule_log(cmd_list, report="False", severity="Medium", mitigation_name="gce_firewallrule_log_mitigation.json"):
	"""
		Test if firewall rule are enable
	"""
	firewall_rule_enable = gce_reduce(cmd_list, "gce_firewallrule_log")

	# Print report for gce_firewallrule_log
	report_print("GCE firewallrule_log ", firewall_rule_enable, report, mitigation_name, severity)


def gce_disk_location(cmd_list, report="False", severity="Major", mitigation_name="gce_disk_location_mitigation.json"):
	"""
		Test for disk location compliance to GDPR
	"""
	disk_location_result = gce_reduce(cmd_list, "gce_disk_location")

	# Print report for gce_disk_location
	report_print("GCE disk location", disk_location_result, report, mitigation_name, severity)


def gce_instance_externalip(cmd_list, report="False", severity="Major", mitigation_name="gce_instance_externalip_mitigation.json"):
	"""
		Test for external ip on GCE instance
	"""
	external_ip_result = gce_reduce(cmd_list, "gce_instance_externalip")

	# Print report for gce_instance_externalip
	report_print("GCE instance external ip", external_ip_result, report, mitigation_name, severity)


def gce_instance_location(cmd_list, report="False", severity="Major", mitigation_name="gce_instance_location_mitigation.json"):
	"""
		Test for instance location compliance to GDPR
	"""
	location_result = gce_reduce(cmd_list, "gce_instance_location")
	
	# Print report for gce_disk_location
	report_print("GCE instance location", location_result, report, mitigation_name, severity)


def gce_instance_service_account(cmd_list, report="False", severity="Major", mitigation_name="gce_instance_service_account_mitigation.json"):
	"""
		Test for instance default account
	"""
	location_result = gce_reduce(cmd_list, "gce_instance_service_account")
	if "API_BILLING" in location_result:
		services_account = location_result
	else:
		services_account = gce_reduce_two(location_result, cmd_list, "gce_instance_service_account")

	# Print report for gce_instance_service_account
	report_print("GCE instance service account", services_account, report, mitigation_name, severity)


def gce_ip_forwarding(cmd_list, report="False", severity="Critical", mitigation_name="gce_ip_forwarding_mitigation.json"):
	"""
		Test for 
	"""
	location_result = gce_reduce(cmd_list, "gce_ip_forwarding")
	if "API_BILLING" in location_result:
		services_account = location_result
	else:
		services_account = gce_reduce_two(location_result, cmd_list, "gce_ip_forwarding")

	# Print report for gce_instance_service_account
	report_print("GCE instance IP forwarding", services_account, report, mitigation_name, severity)
		

def gce_network_name(cmd_list, report="False", severity="Major", mitigation_name="gce_network_name_mitigation.json"):
	"""
		Test for 
	"""
	location_result = gce_reduce(cmd_list, "gce_network_name")
	
	if "API_BILLING" in location_result:
		network_default = location_result
	else:
		network_default = gce_reduce_two(location_result, cmd_list, "gce_network_name")

	# Print report for gce_network_name
	report_print("GCE instance instance default network", network_default, report, mitigation_name, severity)


def gce_shielded_instances(cmd_list, report="False", severity="Minor", mitigation_name="gce_shielded_instances_mitigation.json"):
	"""
		Test if enableIntegrityMonitoring, enableSecureBoot,enableVtpm are enable on GCE instances
	"""
	location_result = gce_reduce(cmd_list, "gce_shielded_instances")
	if "API_BILLING" in location_result:
		shield_result = location_result
	else:
		shield_result = gce_reduce_two(location_result, cmd_list, "gce_shielded_instances")

	# Print report for gce_shielded_instances
	report_print("GCE instance shielding", shield_result, report, mitigation_name, severity)
