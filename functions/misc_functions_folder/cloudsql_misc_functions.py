from functions.misc_functions_folder.misc_functions import *


def cloudsql_reduce(cmd_list, function_name, lock, project, mitigation_name, severity):
	"""
		Cloud SQL function lines of code reducer
	"""
	datas = exec_cmd(cmd_list[0])

	if "API [sqladmin.googleapis.com] not enabled" in datas:
		pretty_print_error(lock, f"Cloud SQL {function_name}", "API [sqladmin.googleapis.com] not enabled", True, project, mitigation_name, severity)

	if "ERROR:" in datas:
		pretty_print_error(lock, f"Cloud SQL {function_name}", "Missing permission", True, project, mitigation_name, severity)

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
		Cloud SQL function lines of code reducer two
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
