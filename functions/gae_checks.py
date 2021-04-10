from functions.gae_misc_functions import *

def gae_env_secret(cmd_list, report="False", severity="Critical", mitigation_name="gae_env_secret_mitigation.json"):
	"""
		Test for AppEngine env variable secret

	"""
	gae_datas = gae_reduce(cmd_list, "gae_env_secret")
	gae_regex_result = gae_reduce_two(gae_datas, cmd_list, "gae_env_secret")

	# Print report for gae_env_secret
	report_print("GAE env variable check", gae_regex_result, report, mitigation_name, severity)


def gae_max_version(cmd_list, report="False", severity="Critical", mitigation_name="gae_max_version_mitigation.json"):
	"""
		Test for AppEngine max version number

	"""
	max_version_result = gae_reduce(cmd_list, "gae_max_version")

	# Print report for gae_max_version
	report_print("GAE max version check", max_version_result, report, mitigation_name, severity)


def gae_location(cmd_list, report="False", severity="Major", mitigation_name="gae_location_mitigation.json"):
	"""
		Test for AppEngine location compliance to GDPR

	"""
	location_id = gae_reduce(cmd_list, "gae_location")

	# Print report for gae_runtime
	report_print("GAE location check", location_id, report, mitigation_name, severity)


def gae_runtime(cmd_list, report="False", severity="Major", mitigation_name="gae_runtime_mitigation.json"):
	"""
		Test for AppEngine location compliance to GDPR

	"""
	gae_datas = gae_reduce(cmd_list, "gae_runtime")
	gae_runtime_result = gae_reduce_two(gae_datas, cmd_list, "gae_runtime")

	# Print report for gae_runtime
	report_print("GAE runtime check", gae_runtime_result, report, mitigation_name, severity)
