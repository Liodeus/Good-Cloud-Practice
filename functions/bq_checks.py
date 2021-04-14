from functions.misc_functions import *


def bq_dataset_location(cmd_list, report="False", severity="Critical", mitigation_name="bq_dataset_location.md"):
	"""
		Test for BigQuery location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0])

	if "BigQuery error in ls operation" in datas:
		print(f"BQ dataset location check : {Fore.RED}x{Style.RESET_ALL}")
		print("\tBiqQuery has not been enabled\n")
		print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
		sys.exit()

	bq_result = {}
	if datas:
		datas = datas.split()[2:]
		for data in datas:
			res = json.loads(exec_cmd(cmd_list[1] + data))["location"]
			if "europe" not in res:
				bq_result[data] = res
	
	report_print("BQ dataset location", bq_result, report, mitigation_name, severity)
