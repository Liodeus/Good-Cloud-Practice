from functions.misc_functions_folder.gce_misc_functions import *


def gce_firewallrule_log(cmd_list, report, lock, project, severity="Medium", mitigation_name="gce_firewallrule_log.md"):
	"""
		Test if firewall rule are enable
	"""
	firewallrule_log = gce_reduce(cmd_list, "gce_firewallrule_log", lock, project, mitigation_name, severity)
	report_print(project, "GCE firewallrule log ", firewallrule_log, report, mitigation_name, severity, lock)


def gce_disk_location(cmd_list, report, lock, project, severity="Major", mitigation_name="gce_disk_location.md"):
	"""
		Test if disk location is compliant to GDPR
	"""
	disk_location = gce_reduce(cmd_list, "gce_disk_location", lock, project, mitigation_name, severity)
	report_print(project, "GCE disk location", disk_location, report, mitigation_name, severity, lock)


def gce_instance_externalip(cmd_list, report, lock, project, severity="Major", mitigation_name="gce_instance_externalip.md"):
	"""
		Test for external ip on GCE instance
	"""
	instance_externalip = gce_reduce(cmd_list, "gce_instance_externalip", lock, project, mitigation_name, severity)
	report_print(project, "GCE instance external ip", instance_externalip, report, mitigation_name, severity, lock)


def gce_instance_location(cmd_list, report, lock, project, severity="Major", mitigation_name="gce_instance_location.md"):
	"""
		Test if instance location is compliant to GDPR
	"""
	instance_location = gce_reduce(cmd_list, "gce_instance_location", lock, project, mitigation_name, severity)
	report_print(project, "GCE instance location", instance_location, report, mitigation_name, severity, lock)


def gce_instance_service_account(cmd_list, report, lock, project, severity="Major", mitigation_name="gce_instance_service_account.md"):
	"""
		Test for GCE instance default account
	"""
	instance_service_account = gce_reduce(cmd_list, "gce_instance_service_account", lock, project, mitigation_name, severity)
	instance_service_account_result = gce_reduce_two(instance_service_account, cmd_list, "gce_instance_service_account")
	report_print(project, "GCE instance service account", instance_service_account_result, report, mitigation_name, severity, lock)


def gce_ip_forwarding(cmd_list, report, lock, project, severity="Critical", mitigation_name="gce_ip_forwarding.md"):
	"""
		Test for GCE IP forwarding
	"""
	ip_forwarding = gce_reduce(cmd_list, "gce_ip_forwarding", lock, project, mitigation_name, severity)
	ip_forwarding_result = gce_reduce_two(ip_forwarding, cmd_list, "gce_ip_forwarding")
	report_print(project, "GCE instance IP forwarding", ip_forwarding_result, report, mitigation_name, severity, lock)
		

def gce_network_name(cmd_list, report, lock, project, severity="Major", mitigation_name="gce_network_name.md"):
	"""
		Test for Default network name in GCE
	"""
	network_name = gce_reduce(cmd_list, "gce_network_name", lock, project, mitigation_name, severity)
	network_name_result = gce_reduce_two(network_name, cmd_list, "gce_network_name")
	report_print(project, "GCE instance default network", network_name_result, report, mitigation_name, severity, lock)


def gce_shielded_instances(cmd_list, report, lock, project, severity="Minor", mitigation_name="gce_shielded_instances.md"):
	"""
		Test if enableIntegrityMonitoring, enableSecureBoot,enableVtpm are enable on GCE instances
	"""
	shielded_instances = gce_reduce(cmd_list, "gce_shielded_instances", lock, project, mitigation_name, severity)
	shielded_instances_result = gce_reduce_two(shielded_instances, cmd_list, "gce_shielded_instances")
	report_print(project, "GCE instance shielding", shielded_instances_result, report, mitigation_name, severity, lock)


def gce_router_nat_location(cmd_list, report, lock, project, severity="Critical", mitigation_name="gce_router_nat_location.md"):
	"""
		Test for NAT router location compliance to GDPR
	"""
	router_nat_location = gce_reduce(cmd_list, "gce_router_nat_location", lock, project, mitigation_name, severity)
	report_print(project, "GCE router NAT location", router_nat_location, report, mitigation_name, severity, lock)


def gce_router_nat_log(cmd_list, report, lock, project, severity="Medium", mitigation_name="gce_router_nat_log.md"):
	"""
		Test for NAT router log should enable : Translation and errors
	"""
	router_nat_log = gce_reduce(cmd_list, "gce_router_nat_log", lock, project, mitigation_name, severity)
	router_nat_log_result = gce_reduce_two(router_nat_log, cmd_list, "gce_router_nat_log")
	report_print(project, "GCE router NAT log", router_nat_log_result, report, mitigation_name, severity, lock)


def gce_firewallrule_traffic(cmd_list, report, lock, project, severity="Critical", mitigation_name="gce_firewallrule_traffic.md"):
	"""
		Test if firewall rule are enable
	"""
	firewallrule_traffic = gce_reduce(cmd_list, "gce_firewallrule_traffic", lock, project, mitigation_name, severity)
	report_print(project, "GCE firewallrule traffic", firewallrule_traffic, report, mitigation_name, severity, lock)


def gce_target_https_proxy_ssl_policy(cmd_list, report, lock, project, severity="Major", mitigation_name="gce_target_https_proxy_ssl_policy.md"):
	"""
		Test 
	"""
	target_https_proxy_ssl_policy = gce_reduce(cmd_list, "gce_target_https_proxy_ssl_policy", lock, project, mitigation_name, severity)
	target_https_proxy_ssl_policy_result = gce_reduce_two(target_https_proxy_ssl_policy, cmd_list, "gce_target_https_proxy_ssl_policy")
	report_print(project, "GCE target https proxy SSL policy", target_https_proxy_ssl_policy_result, report, mitigation_name, severity, lock)


def gce_target_ssl_proxy_ssl_policy(cmd_list, report, lock, project, severity="Major", mitigation_name="gce_target_ssl_proxy_ssl_policy.md"):
	"""
		Test 
	"""
	target_ssl_proxy_ssl_policy = gce_reduce(cmd_list, "gce_target_ssl_proxy_ssl_policy", lock, project, mitigation_name, severity)
	target_ssl_proxy_ssl_policy_result = gce_reduce_two(target_ssl_proxy_ssl_policy, cmd_list, "gce_target_ssl_proxy_ssl_policy")
	report_print(project, "GCE target https proxy SSL policy", target_ssl_proxy_ssl_policy_result, report, mitigation_name, severity, lock)