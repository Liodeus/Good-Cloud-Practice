import shlex, subprocess
import json


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
		mitgation = json.loads(f.read())

		return mitgation


def pretty_print_mitigation(mitigation):
	"""
		Pretty print the mitigation

		Return mitigation as str
	"""
	print("Description :")
	print(f"\t{mitigation['description']}\n")

	print("Fix :")
	print(f"\t{mitigation['fix']}\n")

	print("References :")
	print(f"\t{mitigation['references']}\n")

	print("*************************\n")


def get_project_list():
	"""
		Get the list of projects

		Return list of projects
	"""
	res = exec_cmd("gcloud projects list").split('\n')[1:-1]

	return [x.split()[0] for x in res]


def change_project(project_id):
	"""
		Change the project
	"""
	res = exec_cmd(f"gcloud config set project {project_id}")
	print("\t\t**************************************************")
	print("\t\t**************************************************")
	print(f"\t\t\t\t{project_id}")
	print("\t\t**************************************************")
	print("\t\t**************************************************\n")


def print_report(report, mitigation_name):
	"""
		Print report
	"""
	if report:
		mitigation = read_mitigation(mitigation_name)
		pretty_print_mitigation(mitigation)
	else:
		print("*************************\n")


def list_projects():
	"""
		List projects
	"""
	projects = get_project_list()

	print("This is the list of project(s) :")
	for project in projects:
		print(f"\t{project}")
	exit()


def list_users():
	"""
		List users
	"""

	# print("This is the list of user(s) :")
	# for user in users:
	# 	print(f"\t{user}")
	# exit()