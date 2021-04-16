from functions.misc_functions_folder.gcf_misc_functions import *


def gcf_env_secret(cmd_list, report="False", lock="", severity="Critical", mitigation_name="gcf_env_secret.md"):
	"""
		Test for Google Cloud Function env variable secret
	"""
	env_secret = gcf_reduce(cmd_list, "gcf_env_secret", lock)
	env_secret_result = gfc_reduce_two(env_secret, cmd_list, "gcf_env_secret")
	report_print("GCF env secret check", env_secret_result, report, mitigation_name, severity, lock)


def gcf_location(cmd_list, report="False", lock="", severity="Major", mitigation_name="gcf_location.md"):
	"""
		Test if Google Cloud Function location is compliant to GDPR
	"""
	location = gcf_reduce(cmd_list, "gcf_location", lock)
	report_print("GCF location check", location, report, mitigation_name, severity, lock)


def gcf_runtime(cmd_list, report="False", lock="", severity="Major", mitigation_name="gcf_runtime.md"):
	"""
		Test for Google Cloud Function programming languages
	"""
	runtime = gcf_reduce(cmd_list, "gcf_runtime", lock)
	runtime_result = gfc_reduce_two(runtime, cmd_list, "gcf_runtime")
	report_print("GCF runtime check", runtime_result, report, mitigation_name, severity, lock)


def gcf_service_account(cmd_list, report="False", lock="", severity="Major", mitigation_name="gcf_service_account.md"):
	"""
		Test for Google Cloud Function instance default account
	"""
	service_account = gcf_reduce(cmd_list, "gcf_service_account", lock)
	service_account_result = gfc_reduce_two(service_account, cmd_list, "gcf_service_account")
	report_print("GCF service account check", service_account_result, report, mitigation_name, severity, lock)
