from functions.misc_functions_folder.misc_functions import *


def bq_dataset_location(cmd_list, report, lock, project, severity="Critical", mitigation_name="bq_dataset_location.md"):
	"""
		Test for BigQuery location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0])

	if datas == "":
		pretty_print_error(lock, "bq_dataset_location", "Missing permission or BiqQuery has not been enabled", True, project, mitigation_name, severity)

	if "BigQuery error in ls operation" in datas:
		pretty_print_error(lock, "bq_dataset_location", "BiqQuery has not been enabled", True, project, mitigation_name, severity)

	if "Reauthentication required." in datas:
		pretty_print_error(lock, "bq_dataset_location", "Reauthentication required with bq. You may run : bq ls", True, project, mitigation_name, severity)

	bq_result = {}
	if datas:
		datas = datas.split()[2:]
		for data in datas:
			res = json.loads(exec_cmd(cmd_list[1] + data))["location"]
			if "europe" not in res:
				bq_result[data] = res
	
	report_print(project, "BQ dataset location", bq_result, report, mitigation_name, severity, lock)
