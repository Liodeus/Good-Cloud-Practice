# from functions.cloudsql_misc_functions import *


def cloudsql_backup(cmd_list, report="False", lock="", severity="Major", mitigation_name="cloudsql_backup.md"):
	"""
		Test 
	"""
	pass
	# cloudsql_backup
	# 	gcloud sql instances list
	# 	gcloud sql instances describe NAME
	# 	yaml -> ["settings"]["backupConfiguration"]["enabled"]
	# 	if enabled == false
	# 		error
	# 		if binaryLogEnabled: == false


def cloudsql_backup_location(cmd_list, report="False", lock="", severity="Critical", mitigation_name="cloudsql_backup_location.md"):
	"""
		Test 
	"""
	pass
	# cloudsql_backup_location
	# 	gcloud sql instances list
	# 	gcloud sql instances describe NAME
	# 	yaml -> ["settings"]["backupConfiguration"]["location"]
	# 	if "europe" not in location
	# 		error


def cloudsql_location(cmd_list, report="False", lock="", severity="Critical", mitigation_name="cloudsql_location.md"):
	"""
		Test 
	"""
	pass
	# cloudsql_location
	# gcloud sql instances list
	# 	if europe not in location


def cloudsql_maintenance(cmd_list, report="False", lock="", severity="Minor", mitigation_name="cloudsql_maintenance.md"):
	"""
		Test 
	"""
	pass
	# cloudsql_maintenance
	# 	gcloud sql instances list
	# 	gcloud sql instances describe NAME
	# 	    # Verify that resource is Cloud SQL instance and is not a first gen
	# 	    # Maintenance window is supported only on 2nd generation instances
	# 			backendType: SECOND_GEN
	# 			instanceType: CLOUD_SQL_INSTANCE
	# 	yaml
	# 	maintenanceWindow:
	# 		if day  == 0:
	# 			error
