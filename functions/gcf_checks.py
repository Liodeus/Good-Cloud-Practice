from functions.gcf_misc_functions import *


def gcf_env_secret(cmd_list, report="False", lock="", severity="Critical", mitigation_name="gcf_env_secret.md"):
	"""
		Test
	"""
	gcf_result = gcf_reduce(cmd_list, "gcf_env_secret")
	gcf_env_secret_result = gfc_reduce_two(gcf_result, cmd_list, "gcf_env_secret")
	
	report_print("GCF env secret check", gcf_env_secret_result, report, mitigation_name, severity, lock)


def gcf_location(cmd_list, report="False", lock="", severity="Major", mitigation_name="gcf_location.md"):
	"""
		Test
	"""
	gcf_location_result = gcf_reduce(cmd_list, "gcf_location")

	# Print report for gcf_location
	report_print("GCF location check", gcf_location_result, report, mitigation_name, severity, lock)


def gcf_runtime(cmd_list, report="False", lock="", severity="Major", mitigation_name="gcf_runtime.md"):
	"""
		Test
	"""
	gcf_result = gcf_reduce(cmd_list, "gcf_runtime")
	gcf_runtime_result = gfc_reduce_two(gcf_result, cmd_list, "gcf_runtime")

	# Print report for gcf_runtime
	report_print("GCF runtime check", gcf_runtime_result, report, mitigation_name, severity, lock)


def gcf_service_account(cmd_list, report="False", lock="", severity="Major", mitigation_name="gcf_service_account.md"):
	"""
		Test
	"""
	gcf_result = gcf_reduce(cmd_list, "gcf_service_account")
	gcf_service_account_result = gfc_reduce_two(gcf_result, cmd_list, "gcf_service_account")

	# Print report for gcf_service_account
	report_print("GCF service account check", gcf_service_account_result, report, mitigation_name, severity, lock)
