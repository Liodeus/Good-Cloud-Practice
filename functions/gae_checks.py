from functions.gae_misc_functions import *

def gae_env_secret(cmd_list, report="False", lock="", severity="Critical", mitigation_name="gae_env_secret.md"):
	"""
		Test for AppEngine env variable secret

	"""
	gae_datas = gae_reduce(cmd_list, "gae_env_secret")
	gae_regex_result = gae_reduce_two(gae_datas, cmd_list, "gae_env_secret")

	# Print report for gae_env_secret
	report_print("GAE env variable check", gae_regex_result, report, mitigation_name, severity, lock)


def gae_max_version(cmd_list, report="False", lock="", severity="Critical", mitigation_name="gae_max_version.md"):
	"""
		Test for AppEngine max version number

	"""
	max_version_result = gae_reduce(cmd_list, "gae_max_version")

	if not len(max_version_result) > 2:
		max_version_result = {}

	# Print report for gae_max_version
	report_print("GAE max version check", max_version_result, report, mitigation_name, severity, lock)


def gae_location(cmd_list, report="False", lock="", severity="Major", mitigation_name="gae_location.md"):
	"""
		Test for AppEngine location compliance to GDPR

	"""
	location_id = gae_reduce(cmd_list, "gae_location")

	# Print report for gae_runtime
	report_print("GAE location check", location_id, report, mitigation_name, severity, lock)


def gae_runtime(cmd_list, report="False", lock="", severity="Major", mitigation_name="gae_runtime.md"):
	"""
		Test for AppEngine location compliance to GDPR

	"""
	gae_datas = gae_reduce(cmd_list, "gae_runtime")
	gae_runtime_result = gae_reduce_two(gae_datas, cmd_list, "gae_runtime")

	# Print report for gae_runtime
	report_print("GAE runtime check", gae_runtime_result, report, mitigation_name, severity, lock)
