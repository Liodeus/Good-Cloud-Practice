from functions.misc_functions_folder.gae_misc_functions import *


def gae_env_secret(cmd_list, report, lock, project, severity="Critical", mitigation_name="gae_env_secret.md"):
	"""
		Test for AppEngine env variable secret

	"""
	env_secret = gae_reduce(cmd_list, "gae_env_secret", lock, project, mitigation_name, severity)
	env_secret_result = gae_reduce_two(env_secret, cmd_list, "gae_env_secret")
	report_print(project, "GAE env variable check", env_secret_result, report, mitigation_name, severity, lock)


def gae_max_version(cmd_list, report, lock, project, severity="Critical", mitigation_name="gae_max_version.md"):
	"""
		Test for AppEngine max version number - The max number of version is 2

	"""
	max_version = gae_reduce(cmd_list, "gae_max_version", lock, project, mitigation_name, severity)

	if not len(max_version) > 2:
		max_version = {}

	report_print(project, "GAE max version check", max_version, report, mitigation_name, severity, lock)


def gae_location(cmd_list, report, lock, project, severity="Major", mitigation_name="gae_location.md"):
	"""
		Test for AppEngine location compliance to GDPR

	"""
	location = gae_reduce(cmd_list, "gae_location", lock, project, mitigation_name, severity)
	report_print(project, "GAE location check", location, report, mitigation_name, severity, lock)


def gae_runtime(cmd_list, report, lock, project, severity="Major", mitigation_name="gae_runtime.md"):
	"""
		Test for AppEngine programming languages

	"""
	runtime = gae_reduce(cmd_list, "gae_runtime", lock, project, mitigation_name, severity)
	runtime_result = gae_reduce_two(runtime, cmd_list, "gae_runtime")
	report_print(project, "GAE runtime check", runtime_result, report, mitigation_name, severity, lock)
