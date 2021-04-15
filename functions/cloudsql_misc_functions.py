from functions.misc_functions import *


def cloudsql_reduce(cmd_list, function_name, lock):
	"""

	"""
	datas = exec_cmd(cmd_list[0])

	if "API [sqladmin.googleapis.com] not enabled" in datas:
		error_api_not_enabled(lock, f"GCF {function_name}", "API [sqladmin.googleapis.com] not enabled")

	datas = datas.split('\n')[1:-1]

	res = {}
	for data in datas:
		tmp = data.split()
		name = tmp[0]

		if function_name == "cloudsql_location":
			location = tmp[2]
			if "europe" not in location:
				res[name] = location
		else:
			res[name] = name

	return res


def cloudsql_reduce_two(result, cmd_list, function_name):
	"""

	"""
	res = {}
	for key in result.keys():
		cmd = f"{cmd_list[1]}{key}"
		yaml_result = yaml.load(exec_cmd(cmd), Loader=yaml.FullLoader)

		if function_name == "cloudsql_backup":
			backup_result = yaml_result["settings"]["backupConfiguration"]["enabled"]

			if backup_result == False:
				res[key] = backup_result

		elif function_name == "cloudsql_backup_location":
			backup_location_result = yaml_result["settings"]["backupConfiguration"]["location"]

			if "eu" not in backup_location_result:
				res[key] = backup_location_result

		elif function_name == "cloudsql_maintenance":
			backup_maintenance_result = yaml_result["settings"]["maintenanceWindow"]

			if backup_maintenance_result["day"] == 0:
				res[key] = "Disable"

	return res
