from  colorama import Fore, Style
from ..report.report import *
from os import mkdir
import subprocess
import threading
import datetime
import shlex
import yaml
import json
import sys
import re

NB_CRITICAL = 8
NB_MAJOR = 12
NB_MEDIUM = 1
NB_MINOR = 2
NB_TOTAL = NB_CRITICAL + NB_MAJOR + NB_MEDIUM + NB_MINOR


def banner():
	""""
		Print the tool banner
	"""
	banner = f'''
{Fore.CYAN}   _____ {Style.RESET_ALL}                      _    {Fore.CYAN}  _____ {Style.RESET_ALL}  _                       _    {Fore.CYAN} _____  {Style.RESET_ALL}                        _     _               
{Fore.CYAN}  / ____|{Style.RESET_ALL}                     | |   {Fore.CYAN} / ____|{Style.RESET_ALL} | |                     | |   {Fore.CYAN}|  __ \ {Style.RESET_ALL}                       | |   (_)              
{Fore.CYAN} | |  __ {Style.RESET_ALL}   ___     ___     __| |   {Fore.CYAN}| |     {Style.RESET_ALL} | |   ___    _   _    __| |   {Fore.CYAN}| |__) |{Style.RESET_ALL}  _ __    __ _    ___  | |_   _    ___    ___ 
{Fore.CYAN} | | |_ |{Style.RESET_ALL}  / _ \   / _ \   / _` |   {Fore.CYAN}| |     {Style.RESET_ALL} | |  / _ \  | | | |  / _` |   {Fore.CYAN}|  ___/ {Style.RESET_ALL} | '__|  / _` |  / __| | __| | |  / __|  / _ \

{Fore.CYAN} | |__| |{Style.RESET_ALL} | (_) | | (_) | | (_| |   {Fore.CYAN}| |____ {Style.RESET_ALL} | | | (_) | | |_| | | (_| |   {Fore.CYAN}| |     {Style.RESET_ALL} | |    | (_| | | (__  | |_  | | | (__  |  __/
{Fore.CYAN}  \_____|{Style.RESET_ALL}  \___/   \___/   \__,_|   {Fore.CYAN} \_____|{Style.RESET_ALL} |_|  \___/   \__,_|  \__,_|   {Fore.CYAN}|_|     {Style.RESET_ALL} |_|     \__,_|  \___|  \__| |_|  \___|  \___|
                                                                                                                                 
                                                                                                                      By Liodeus           
	'''
	print(banner)


def exec_cmd(cmd):
	"""
		Execute a command line passed by argument

		Return the results of the executed command as str
	"""
	args = shlex.split(cmd)
	p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,)

	return p.communicate()[0].decode("utf-8")


def read_mitigation(mitigation_name):
	"""
		Read json mitigation and transform to it to dictionnary

		Return mitigation as a dictionnary
	"""
	with open(f"mitigations/{mitigation_name}") as f:
		mitgation = f.read()

		return mitgation


def pretty_print_mitigation(mitigation):
	"""
		Pretty print the mitigation

		Return mitigation as str
	"""
	mitigation = '\n'.join(mitigation.split('\n')[2:])
	print(mitigation)
	print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")


def change_project(project_id):
	"""
		Change the project

		Return True if ok else return False
	"""
	if re.match("[a-z]{1}[a-z0-9-]{5,29}", project_id):
		res = exec_cmd(f"gcloud config set project {project_id}")

		if "You do not appear to have access to project" not in res and "(gcloud.config.set)" not in res:
			print(f"{Fore.CYAN}\t\t\t\t\t\t**************************************************{Style.RESET_ALL}")
			print(f"{Fore.CYAN}\t\t\t\t\t\t**************************************************{Style.RESET_ALL}")
			print(f"\t\t\t\t\t\t\t\t{project_id}")
			print(f"{Fore.CYAN}\t\t\t\t\t\t**************************************************{Style.RESET_ALL}")
			print(f"{Fore.CYAN}\t\t\t\t\t\t**************************************************{Style.RESET_ALL}\n")
			return True
		else:
			return print_error(project_id)
	else:
		return print_error(project_id)


def print_error(project_id):
	print(f"You do not appear to have access to project [{project_id}] or it does not exist.\n")
	print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
	return False


def print_report(report, mitigation_name, severity):
	"""
		Print report
	"""
	if mitigation_name not in ["gae_env_secret.md", "gcf_env_secret.md"]:
		print("")

	print_severity(severity)
	if report:
		mitigation = read_mitigation(mitigation_name)
		pretty_print_mitigation(mitigation)
	else:
		print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")


def print_severity(severity):
	"""
		Print the severity by colors
	"""
	color = ""
	if severity == "Minor":
		color = Fore.CYAN
	elif severity == "Medium":
		color = Fore.GREEN
	elif severity == "Major":
		color = Fore.YELLOW
	elif severity == "Critical":
		color = Fore.RED

	print(f"Severity : {color}{severity}{Style.RESET_ALL}\n")


def get_project_list():
	"""
		Get the list of projects

		Return list of projects
	"""
	try:
		res = exec_cmd("gcloud projects list")
	except FileNotFoundError:
		print("You need to install gcloud !\n")
		print("Go check requirements : https://github.com/Liodeus/Good-Cloud-Practice#requirements")
		sys.exit()

	if "You do not currently have an active account selected." in res:
		print("You do not currently have an active account selected.\nPlease run :\n\tgcloud auth login")
		sys.exit()

	if "UNAUTHENTICATED" in res:
		print("You need to reauthenticate !\n")
		print("You may run the following command : gcloud auth login")
		sys.exit()

	return [x.split()[0] for x in res.split('\n')[1:-1]]


def list_projects():
	"""
		Print the list of projects
	"""
	projects = get_project_list()
	current_project = get_current_project().strip()
	print_current_user()

	print("This is the list of project(s) :")
	for project in projects:
		if project == current_project:
			print(f"\t{project} -> Current project")
		else:
			print(f"\t{project}")
	sys.exit()


def get_current_project():
	"""
		Get the current project

		Return name of current project
	"""
	return exec_cmd("gcloud config get-value project")


def get_list_users():
	"""
		Get the list of users

		Return list of users
	"""
	res = exec_cmd("gcloud auth list").split('\n')[2:]

	if res[1] == "To login, run:":
		print("You do not currently have an active account selected.\nPlease run :\n\tgcloud auth login")
		sys.exit()

	users = []
	for x in res:
		try:
			users.append(x.split()[-1])
		except IndexError:
			break

	return users


def list_users():
	"""
		Print the list of users
	"""
	users = get_list_users()
	print_current_user()

	print("This is the list of user(s) :")
	for user in users:
		print(f"\t{user}")
	sys.exit()


def print_current_user():
	"""
		Get the current user
	"""
	res = exec_cmd("gcloud auth list").split('\n')[2:]
	user = ""
	for x in res:
		if "*" in x:
			user = x.split()[1]
			print(f"Current user : {user}\n") 
	return user


def report_print(project, string_to_print, dict_result, report, mitigation_name, severity, lock):
	"""

	"""
	state = True
	str_to_print = ""
	lock.acquire()
	if dict_result:
		print(f"{string_to_print} : {Fore.RED}x{Style.RESET_ALL}")
		print("\tInformation :")
		if "API_BILLING" in dict_result:
			print("\t\tThis API method requires billing to be enabled. Please enable billing by visiting https://console.developers.google.com/billing/enable then retry.\n")
			print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
		else:
			non_compliance_summary[severity] += 1
			str_start = string_to_print[:3]
			state = False

			if str_start == "BQ ":
				non_compliance_summary["BQ"] += 1
			elif str_start == "GAE": 
				non_compliance_summary["GAE"] += 1
			elif str_start == "GCE": 
				non_compliance_summary["GCE"] += 1
			elif str_start == "GCF": 
				non_compliance_summary["GCF"] += 1
			elif "Cloud DNS" in string_to_print: 
				non_compliance_summary["CLOUDDNS"] += 1
			elif "Cloud SQL" in string_to_print: 
				non_compliance_summary["CLOUDSQL"] += 1

			
			for key, value in dict_result.items():
				if string_to_print == "GCE instance shielding":
					for config_name, state in value.items():
						if not state:
							print(f"\t\t{key} : {config_name} -> {state}")
				elif string_to_print in ["GAE env variable check", "GCF env secret check"]:
					str_tmp = ""
					print(f"\t\t{key} :")
					for result in value:
						for secret, secret_value in result.items():
							str_tmp += f"\t\t\t{secret} -> {secret_value}\n"
					str_to_print = str_tmp.replace('\t', '')
					print(f"{str_tmp}")
				elif string_to_print == "GAE max version check":
					print(f"\t\t{key}")
					str_to_print += f"{key}\n"
				else:
					str_to_print += f"{key} -> {value}\n"
					print(f"\t\t{key} -> {value}")

			print_report(report, mitigation_name, severity)

	else:
		print(f"{string_to_print} : {Fore.GREEN}✓{Style.RESET_ALL}\n")
		print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
	
	markdown_to_report(project, mitigation_name, str_to_print, severity, state)
	lock.release()


def get_date():
	"""
		Print the actual date
	"""
	print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
	print()


non_compliance_summary = {
	"Critical": 0,
	"Major": 0,
	"Medium": 0,
	"Minor": 0,
	"BQ": 0,
	"CLOUDDNS": 0,
	"GAE": 0,
	"GCE": 0,
	"GCF": 0,
	"CLOUDSQL": 0
}
def print_non_compliance_summary():
	"""
		Print at the end of the scan the non compliance summary by severity, then by types of checks	
	"""
	crit = non_compliance_summary['Critical']
	maj = non_compliance_summary['Major']
	med = non_compliance_summary['Medium']
	mino = non_compliance_summary['Minor']
	total = crit + maj + med + mino

	height_severity = [crit, maj, med, mino]
	height_types = [non_compliance_summary['BQ'], non_compliance_summary['CLOUDDNS'], non_compliance_summary['GAE'], non_compliance_summary['GCE'], non_compliance_summary['GCF'], non_compliance_summary['CLOUDSQL']]

	print("Non compliances summary :")
	print(f"\t{Fore.RED}Critical -> {crit}/{NB_CRITICAL}{Style.RESET_ALL}")
	print(f"\t{Fore.YELLOW}Major -> {maj}/{NB_MAJOR}{Style.RESET_ALL}")
	print(f"\t{Fore.GREEN}Medium -> {med}/{NB_MEDIUM}{Style.RESET_ALL}")
	print(f"\t{Fore.CYAN}Minor -> {mino}/{NB_MINOR}{Style.RESET_ALL}")
	print(f"\tTotal -> {total}/{NB_TOTAL}\n")

	print("Nom compliances by type :")
	print(f"\tBiqQuery -> {non_compliance_summary['BQ']}")
	print(f"\tCloud DNS -> {non_compliance_summary['CLOUDDNS']}")
	print(f"\tGoogle AppEngine -> {non_compliance_summary['GAE']}")
	print(f"\tGoogle Compute Engine -> {non_compliance_summary['GCE']}")
	print(f"\tGoogle Cloud Function -> {non_compliance_summary['GCF']}")
	print(f"\tCloud SQL -> {non_compliance_summary['CLOUDSQL']}\n")

	print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
	reset_count_non_compliance()

	return height_severity, height_types


def reset_count_non_compliance():
	"""
		Reset the global non_compliance_summary variable
	"""
	global non_compliance_summary

	non_compliance_summary = {
		"Critical": 0,
		"Major": 0,
		"Medium": 0,
		"Minor": 0,
		"BQ": 0,
		"CLOUDDNS": 0,
		"GAE": 0,
		"GCE": 0,
		"GCF": 0,
		"CLOUDSQL": 0
	}


def pretty_print_error(lock, type_function_name, error_message, state, project, mitigation_name, severity):
	""""
		Pretty print error message
	"""
	lock.acquire()
	if state:
		print(f"{type_function_name} check : {Fore.RED}x{Style.RESET_ALL}")
		print("\tInformation")
		print(f"\t\t{error_message}\n")
		markdown_to_report(project, mitigation_name, error_message, severity, False)
	else:
		print(f"{type_function_name} check : {Fore.GREEN}✓{Style.RESET_ALL}\n")
		markdown_to_report(project, mitigation_name, error_message, severity, True)

	print(f"{Fore.BLUE}****************************************************************************************************{Style.RESET_ALL}\n")
	lock.release()
	sys.exit()


def create_folders():
	date_of_scan = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
	report_folder_name = f"./results/report_{date_of_scan.replace('-', '_')}"

	try:
		mkdir("./results")
	except FileExistsError:
		pass

	mkdir(report_folder_name)
	mkdir(f"{report_folder_name}/graph_images")
	mkdir(f"{report_folder_name}/css")
	mkdir(f"{report_folder_name}/js")
	mkdir(f"{report_folder_name}/images")
	exec_cmd(f"cp functions/report/template/script.js {report_folder_name}/js/")
	exec_cmd(f"cp functions/report/template/script.js {report_folder_name}/js/")
	exec_cmd(f"cp functions/report/template/style.css {report_folder_name}/css/")
	exec_cmd(f"cp images/logo.png {report_folder_name}/images/")
	exec_cmd(f"cp functions/report/template/style_details.css {report_folder_name}/css/")

	return date_of_scan, report_folder_name