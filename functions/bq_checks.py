from functions.misc_functions import *


def bq_dataset_location(cmd_list, report="False", lock="", severity="Critical", mitigation_name="bq_dataset_location.md"):
	"""
		Test for BigQuery location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0])

	if "BigQuery error in ls operation" in datas:
		error_api_not_enabled(lock, "BQ dataset location", "BiqQuery has not been enabled")
		lock.acquire()

	bq_result = {}
	if datas:
		datas = datas.split()[2:]
		for data in datas:
			res = json.loads(exec_cmd(cmd_list[1] + data))["location"]
			if "europe" not in res:
				bq_result[data] = res
	
	report_print("BQ dataset location", bq_result, report, mitigation_name, severity, lock)
