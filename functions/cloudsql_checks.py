from functions.misc_functions_folder.cloudsql_misc_functions import *


def cloudsql_location(cmd_list, report, lock, project, severity="Critical", mitigation_name="cloudsql_location.md"):
	"""
		Test if Cloud SQL location is compliant to GDPR
	"""
	location = cloudsql_reduce(cmd_list, "cloudsql_location", lock, project, mitigation_name, severity)
	report_print(project, "Cloud SQL location check", location, report, mitigation_name, severity, lock)


def cloudsql_backup(cmd_list, report, lock, project, severity="Major", mitigation_name="cloudsql_backup.md"):
	"""
		Test if there is a Cloud SQL backup
	"""
	backup = cloudsql_reduce(cmd_list, "cloudsql_backup", lock, project, mitigation_name, severity)
	backup_result = cloudsql_reduce_two(backup, cmd_list, "cloudsql_backup")
	report_print(project, "Cloud SQL backup check", backup_result, report, mitigation_name, severity, lock)


def cloudsql_backup_location(cmd_list, report, lock, project, severity="Critical", mitigation_name="cloudsql_backup_location.md"):
	"""
		Test if Cloud SQL backup location is compliant to GDPR
	"""
	backup_location = cloudsql_reduce(cmd_list, "cloudsql_backup", lock, project, mitigation_name, severity)
	backup_location_result = cloudsql_reduce_two(backup_location, cmd_list, "cloudsql_backup_location")
	report_print(project, "Cloud SQL backup location check", backup_location_result, report, mitigation_name, severity, lock)


def cloudsql_maintenance(cmd_list, report, lock, project, severity="Minor", mitigation_name="cloudsql_maintenance.md"):
	"""
		Test is there is a maintenance windows selected for updates
	"""
	maintenance = cloudsql_reduce(cmd_list, "cloudsql_backup", lock, project, mitigation_name, severity)
	maintenance_result = cloudsql_reduce_two(maintenance, cmd_list, "cloudsql_maintenance")
	report_print(project, "Cloud SQL maintenance check", maintenance_result, report, mitigation_name, severity, lock)
