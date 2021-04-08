from functions.misc_functions import *


def gce_firewallrule_log(cmd_list, report="False", severity="Medium", mitigation_name="gce_firewallrule_log_mitigation.json"):
	"""
		Test <TODO>

	"""
	pass


def gce_disk_location(cmd_list, report="False", severity="Major", mitigation_name="gce_disk_location_mitigation.json"):
	"""
		Test for disk location compliance to GDPR
	"""
	datas = exec_cmd(cmd_list[0]).split('\n')

	if "ERROR:" in datas[0]:
		print("GCE disk location check : x")
		print("\tAn error occured")
		print(f"\t\t{' '.join(datas)}")
		print("*************************\n")
		sys.exit()


	# Print report for gce_disk_location
	datas = datas[1:-1][0].split()[1]
	if "europe" not in datas:
		print("GCE disk location check : x")
		print("\tInformation :")
		print(f"\t\tGoogle Compute Engine disk location :")
		print(f"\t\t\t{datas}\n")

		# Print report for gce_disk_location
		print_report(report, mitigation_name)

	else:
		print("GCE disk location : ✓\n")
		print("*************************\n")
