import shlex, subprocess
import json
import sys


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


def change_project(project_id):
	"""
		Change the project
	"""
	exec_cmd(f"gcloud config set project {project_id}")
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


def get_project_list():
	"""
		Get the list of projects

		Return list of projects
	"""
	res = exec_cmd("gcloud projects list")
	if "UNAUTHENTICATED" in res:
		print("You need to reauthenticate !\n")
		print("You may run the following command : gcloud auth login")
		exit()

	return [x.split()[0] for x in res.split('\n')[1:-1]]


def list_projects():
	"""
		Print the list of projects
	"""
	projects = get_project_list()
	current_project = get_current_project().strip()

	print("This is the list of project(s) :")
	for project in projects:
		if project == current_project:
			print(f"\t{project} -> Current project")
		else:
			print(f"\t{project}")
	exit()


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
	current_user = get_current_user()

	print("This is the list of user(s) :")
	for user in users:
		if user == current_user:
			print(f"\t{user} -> Current user")
		else:
			print(f"\t{user}")
	exit()


def get_current_user():
	"""
		Get the current user

		Return name of current user
	"""
	res = exec_cmd("gcloud auth list").split('\n')[2:]

	for x in res:
		if "*" in x:
			return x.split()[1]