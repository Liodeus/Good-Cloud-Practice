import shlex, subprocess
import json


def exec_cmd(cmd):
	"""
		Execute a command line passed by argument

		Return the results of the executed command as str
	"""
	args = shlex.split(cmd)
	p = subprocess.Popen(args, stdout=subprocess.PIPE)

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