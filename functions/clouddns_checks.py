from functions.clouddns_misc_functions import *


def clouddns_dnssec(cmd_list, report="False", lock="", severity="Major", mitigation_name="clouddns_dnssec.md"):
	"""
		Test for DNSSEC security
	"""
	# DNSSEC check
	dnssec_results = clouddns_reduce(cmd_list, "clouddns_dnssec", lock)

	# Print report for DNSSEC
	report_print("Cloud DNS DNSSEC check", dnssec_results, report, mitigation_name, severity, lock)


def clouddns_rsasha1(cmd_list, report="False", lock="", severity="Critical", mitigation_name="clouddns_rsasha1.md"):
	"""
		Test for DNSSEC RSASHA1 weak algorithm
	"""
	rsasha1_results = clouddns_reduce(cmd_list, "clouddns_rsasha1", lock)

	# Print report for RSASHA1
	report_print("Cloud DNS RSASHA1 check", rsasha1_results, report, mitigation_name, severity, lock)
