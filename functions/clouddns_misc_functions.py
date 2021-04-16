from functions.misc_functions import *

def clouddns_reduce(cmd_list, function_name, lock):
	"""

	"""
	datas = exec_cmd(cmd_list[0]).split()

	if datas[0] == "ERROR:":
		error_api_not_enabled(lock, f"Cloud DNS {function_name}", "Missing permissions")

	if datas[0] == "API":
		error_api_not_enabled(lock, f"Cloud DNS {function_name}", "API [dns.googleapis.com] not enabled")

	if function_name == "clouddns_dnssec":
		if datas[0] == "Listed":
			lock.acquire()
			print(f"Cloud DNS DNSSEC check : {Fore.GREEN}✓{Style.RESET_ALL}\n")
			lock.release()
			print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
			sys.exit()

	managed_zones = [x.split('/')[-1] for x in datas]

	managed_zones_results = {}
	for zone in managed_zones:
		managed_zones_results[zone] = exec_cmd(f"{cmd_list[1]} {zone}")

	res = {}
	for zone, result in managed_zones_results.items():
		if function_name == "clouddns_dnssec":
			if "state: off" in result or "state" not in result:
				res[zone] = "OFF"
			else:
				if "algorithm: RSASHA1" in value:
					rsasha1_results[key] = "RSASHA1"

	return res