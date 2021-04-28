from functions.misc_functions_folder.misc_functions import *


def kms_max_rotation_period(cmd_list, report, lock, project, severity="Medium", mitigation_name="kms_max_rotation_period.md"):
	"""
		Test
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]
	location_ids = [x.split()[0] for x in datas]

	res = {}
	for location_id in location_ids:
		datas = exec_cmd(f"{cmd_list[1]}{location_id}")

		if "not enabled on project" in datas:
			pretty_print_error(lock, f"KMS max rotation period", "API [cloudkms.googleapis.com] not enabled", True, project, mitigation_name, severity)

		if datas != "Listed 0 items.\n":
			keys = datas.split('\n')[1:-1]
			for key in keys:
				key_name = key.split('/')[-1]

				datas_tmp = exec_cmd(f"{cmd_list[2]} {key_name} --location={location_id}")

				for key_to_describe in datas_tmp.split('\n')[1:-1]:
					tmp_key = key_to_describe.split()[0]

					yaml_result = yaml.load(exec_cmd(f"{cmd_list[3]} {tmp_key}"), Loader=yaml.FullLoader)

					try:
						rotation_period = int(yaml_result["rotationPeriod"][:-1])
					except KeyError:
						try:
							res[location_id][key_name] = [tmp_key, 0, False]
						except KeyError:
							res[location_id] = {}
							res[location_id][key_name] = []
							res[location_id][key_name] = [tmp_key, 0, False]
						continue

					days = rotation_period // (24 * 3600)

					if days > 100:
						try:
							res[location_id][key_name] = [tmp_key, days, True]
						except KeyError:
							res[location_id] = {}
							res[location_id][key_name] = []
							res[location_id][key_name] = [tmp_key, days, True]		

	report_print(project, "KMS max rotation period", res, report, mitigation_name, severity, lock)