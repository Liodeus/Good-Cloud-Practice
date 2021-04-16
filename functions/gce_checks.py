from functions.misc_functions_folder.gce_misc_functions import *


def gce_firewallrule_log(cmd_list, report="False", lock="", severity="Medium", mitigation_name="gce_firewallrule_log.md"):
	"""
		Test if firewall rule are enable
	"""
	firewallrule_log = gce_reduce(cmd_list, "gce_firewallrule_log", lock)
	report_print("GCE firewallrule_log ", firewallrule_log, report, mitigation_name, severity, lock)


def gce_disk_location(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_disk_location.md"):
	"""
		Test if disk location is compliant to GDPR
	"""
	disk_location = gce_reduce(cmd_list, "gce_disk_location", lock)
	report_print("GCE disk location", disk_location, report, mitigation_name, severity, lock)


def gce_instance_externalip(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_instance_externalip.md"):
	"""
		Test for external ip on GCE instance
	"""
	instance_externalip = gce_reduce(cmd_list, "gce_instance_externalip", lock)
	report_print("GCE instance external ip", instance_externalip, report, mitigation_name, severity, lock)


def gce_instance_location(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_instance_location.md"):
	"""
		Test if instance location is compliant to GDPR
	"""
	instance_location = gce_reduce(cmd_list, "gce_instance_location", lock)
	report_print("GCE instance location", instance_location, report, mitigation_name, severity, lock)


def gce_instance_service_account(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_instance_service_account.md"):
	"""
		Test for GCE instance default account
	"""
	instance_service_account = gce_reduce(cmd_list, "gce_instance_service_account", lock)
	instance_service_account_result = gce_reduce_two(instance_service_account, cmd_list, "gce_instance_service_account")
	report_print("GCE instance service account", instance_service_account_result, report, mitigation_name, severity, lock)


def gce_ip_forwarding(cmd_list, report="False", lock="", severity="Critical", mitigation_name="gce_ip_forwarding.md"):
	"""
		Test for GCE IP forwarding
	"""
	ip_forwarding = gce_reduce(cmd_list, "gce_ip_forwarding", lock)
	ip_forwarding_result = gce_reduce_two(ip_forwarding, cmd_list, "gce_ip_forwarding")
	report_print("GCE instance IP forwarding", ip_forwarding_result, report, mitigation_name, severity, lock)
		

def gce_network_name(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_network_name.md"):
	"""
		Test for Default network name in GCE
	"""
	network_name = gce_reduce(cmd_list, "gce_network_name", lock)
	network_name_result = gce_reduce_two(network_name, cmd_list, "gce_network_name")
	report_print("GCE instance instance default network", network_name_result, report, mitigation_name, severity, lock)


def gce_shielded_instances(cmd_list, report="False", lock="", severity="Minor", mitigation_name="gce_shielded_instances.md"):
	"""
		Test if enableIntegrityMonitoring, enableSecureBoot,enableVtpm are enable on GCE instances
	"""
	shielded_instances = gce_reduce(cmd_list, "gce_shielded_instances", lock)
	shielded_instances_result = gce_reduce_two(shielded_instances, cmd_list, "gce_shielded_instances")
	report_print("GCE instance shielding", shielded_instances_result, report, mitigation_name, severity, lock)
