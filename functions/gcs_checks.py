from functions.misc_functions_folder.misc_functions import *


def gcs_storage_location(cmd_list, report, lock, project, severity="Critical", mitigation_name="gcs_storage_location.md"):
	"""
		Test for Google Cloud Storage location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0])

	datas = datas.split('\n')

	buckets_list = [x for x in datas][:-1]

	gcs_storage_result = {}
	for bucket in buckets_list:
		datas = exec_cmd(f"{cmd_list[1]} {bucket}").split('\n')
		bucket_name = datas[0].split()[0]
		location = datas[3].lower().split()[2]

		if "eu" not in location and "europe" not in location:
			gcs_storage_result[bucket_name] = location

	report_print(project, "GCS location check", gcs_storage_result, report, mitigation_name, severity, lock)