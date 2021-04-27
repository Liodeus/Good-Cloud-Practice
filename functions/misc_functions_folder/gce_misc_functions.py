from functions.misc_functions_folder.misc_functions import *


def gce_reduce(cmd_list, function_name, lock, project, mitigation_name, severity):
	"""
		Google Compute Engine function lines of code reducer
	"""
	result = {}

	if function_name in ["gce_firewallrule_log", "gce_firewallrule_traffic"]:
		res = exec_cmd(cmd_list[0])
		if "ERROR:" in res:
			pretty_print_error(lock, f"GCE {function_name}", "Missing permissions", True, project, mitigation_name, severity)

		try:
			datas = json.loads(res)
		except json.decoder.JSONDecodeError:
			pretty_print_error(lock, f"GCE {function_name}", "This API method requires billing to be enabled. Please enable billing by visiting https://console.developers.google.com/billing/enable then retry.", True, project, mitigation_name, severity)

		for data in datas:
			state = data["logConfig"]["enable"]
			name = data["name"]
			source_range = data["sourceRanges"]

			if function_name == "gce_firewallrule_log":
				if not state:
					result[name] = state
			else:
				if "0.0.0.0/0" in source_range:
					result[name] = "Allow source range 0.0.0.0/0"
	else:
		if function_name in  ["gce_target_https_proxy_ssl_policy", "gce_target_ssl_proxy_ssl_policy"]:
			datas = exec_cmd(cmd_list[0])

			if "Listed 0 items." in datas:
				return result

			if "not enabled on project" in datas:
				pretty_print_error(lock, f"GCE {function_name}", "Missing permissions", True, project, mitigation_name, severity)

			if "Please enable billing" in datas:
				pretty_print_error(lock, f"GCE {function_name}", "This API method requires billing to be enabled. Please enable billing by visiting https://console.developers.google.com/billing/enable then retry.", True, project, mitigation_name, severity)

			for data in datas.split('\n')[1:-1]:
				tmp = data.split()	
				name = tmp[0]
				location = tmp[1]

				result[name] = location

		else:

			datas = exec_cmd(cmd_list[0]).split('\n')[1:-1]

			if not datas:
				return result

			if "permission for" in datas[0] or "Would you like to enable and retry" in datas[0]:
				pretty_print_error(lock, f"GCE {function_name}", "Missing permissions", True, project, mitigation_name, severity)

			if "This API method requires billing to be enabled." in datas[0]:
				pretty_print_error(lock, f"GCE {function_name}", "This API method requires billing to be enabled. Please enable billing by visiting https://console.developers.google.com/billing/enable then retry.", True, project, mitigation_name, severity)

			if function_name in ["gce_disk_location"]:
				if "ERROR:" in datas[0]:
					print("\tAn error occured")
					print(f"\t\t{' '.join(datas)}")
					print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
					sys.exit()
			
			for data in datas:
				tmp = data.split()	
				name = tmp[0]
				location = tmp[1]

				if function_name in ["gce_shielded_instances", "gce_network_name", "gce_ip_forwarding", "gce_instance_service_account", "gce_target_https_proxy_ssl_policy"]:
					result[name] = location
				elif function_name in ["gce_instance_location", "gce_disk_location", "gce_router_nat_location"]:
					if "europe" not in location:
						result[name] = location
				elif function_name in ["gce_instance_externalip"]:
					external_ip = tmp[4]
					if external_ip not in ["TERMINATED", "RUNNING"]:
						result[name] = external_ip
				elif function_name == "gce_router_nat_log":
					cmd = f"{cmd_list[1]} {name} --region {location}"
					tmp_res = exec_cmd(cmd)
					for x in tmp_res.split('\n')[1:-1]:
						try:
							result[name][location].append(x.split()[0])
						except KeyError:
							result[name] = {}
							result[name][location] = []
							result[name][location].append(x.split()[0])

	return result


def gce_reduce_two(result, cmd_list, function_name):
	"""
		Google Compute Engine function lines of code reducer two
	"""
	res = {}
	for name, location in result.items():
		if function_name == "gce_router_nat_log":
			for key, values in location.items():
				for value in values:
					cmd = f"{cmd_list[2]} {value} --router {name} --region {key} "
					yaml_datas = yaml.load(exec_cmd(cmd), Loader=yaml.FullLoader)
					log_conf = yaml_datas["logConfig"]
					log_enable = log_conf["enable"]
					log_filter = log_conf["filter"]

					if not log_enable or log_filter != "ALL":
						res[value] = "Need to enable translation AND errrors"
		elif function_name in ["gce_target_https_proxy_ssl_policy", "gce_target_ssl_proxy_ssl_policy"]:
			yaml_datas = yaml.load(exec_cmd(f"{cmd_list[1]} {name}"), Loader=yaml.FullLoader)

			if "sslPolicy" not in yaml_datas:
				res[name] = "Missing SSL policy"
		else:
			yaml_datas = yaml.load(exec_cmd(f"{cmd_list[1]}{location} {name}"), Loader=yaml.FullLoader)

			if function_name == "gce_instance_service_account":
				email = yaml_datas["serviceAccounts"][0]["email"]

				if re.match("[0-9]*-compute@developer.gserviceaccount.com", email):
					res[name] = email

			elif function_name == "gce_ip_forwarding":
				forward = yaml_datas["canIpForward"]

				if forward:
					res[name] = forward

			elif function_name == "gce_network_name":
				network = yaml_datas["networkInterfaces"][0]["network"].split('/')[-1]

				if network == "default":
					res[name] = network

			elif function_name == "gce_shielded_instances":
				shield_config = yaml_datas["shieldedInstanceConfig"]
				for value in shield_config.values():
					if not value:
						res[name] = shield_config
						break
	return res
