from functions.cloudsql_misc_functions import *


def cloudsql_backup(cmd_list, report="False", lock="", severity="Major", mitigation_name="cloudsql_backup.md"):
	"""
		Test 
	"""
	cloudsql_backup_one = cloudsql_reduce(cmd_list, "cloudsql_backup", lock)
	cloudsql_backup_location_result = cloudsql_reduce_two(cloudsql_backup_one, cmd_list, "cloudsql_backup_location")

	# Print report for cloudsql_backup
	report_print("Cloud SQL backup check", cloudsql_backup_location_result, report, mitigation_name, severity, lock)


def cloudsql_backup_location(cmd_list, report="False", lock="", severity="Critical", mitigation_name="cloudsql_backup_location.md"):
	"""
		Test 
	"""
	cloudsql_backup_location_one = cloudsql_reduce(cmd_list, "cloudsql_backup", lock)
	cloudsql_backup_location_result = cloudsql_reduce_two(cloudsql_backup_location_one, cmd_list, "cloudsql_backup_location")

	# Print report for cloudsql_backup_location
	report_print("Cloud SQL backup location check", cloudsql_backup_location_result, report, mitigation_name, severity, lock)


def cloudsql_location(cmd_list, report="False", lock="", severity="Critical", mitigation_name="cloudsql_location.md"):
	"""
		Test 
	"""
	cloudsql_location = cloudsql_reduce(cmd_list, "cloudsql_location", lock)

	# Print report for cloudsql_backup
	report_print("Cloud SQL location check", cloudsql_location, report, mitigation_name, severity, lock)


def cloudsql_maintenance(cmd_list, report="False", lock="", severity="Minor", mitigation_name="cloudsql_maintenance.md"):
	"""
		Test 
	"""
	cloudsql_maintenance_one = cloudsql_reduce(cmd_list, "cloudsql_backup", lock)
	cloudsql_maintenance_result = cloudsql_reduce_two(cloudsql_maintenance_one, cmd_list, "cloudsql_maintenance")

	# Print report for cloudsql_backup_location
	report_print("Cloud SQL maintenance check", cloudsql_maintenance_result, report, mitigation_name, severity, lock)
