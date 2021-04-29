from functions.cmds_args import *
import argparse
import os.path
import time
import sys


def main(REPORT, project_id=None, path=None, user=None, key=None, lp=None, lu=None, threads=None, slow=None, fast=None):
	t0 = time.time()
	get_date()
	speed = 0

	if slow:
		speed = 5
	elif fast:
		speed = 20
	elif threads != None:
		if threads > 30:
			speed = 30
		elif threads < 0:
			print("Threads must be a number greater than 0 !")
			sys.exit()
		else:
			speed = threads
	else:
		speed = 5

	if key:
		if os.path.isfile(key):
			res = exec_cmd(f"gcloud auth activate-service-account --key-file={key}")
			if "ERROR:" in res:
				print("There is a problem with the key.")
				sys.exit()
		else:
			print("The path of the key file does not exist or is wrong.")
			sys.exit()

	if user:
		users = get_list_users()

		if user in users:
			res = exec_cmd(f"gcloud config set account {user}")
		else:
			print("User does not exist or you need to run : gcloud auth login")
			sys.exit()

	if lp:
		list_projects()
	
	if lu:
		list_users()

	if path != None:
		if os.path.isfile(path):
			with open(path) as f:
				projects_list = [x.strip() for x in f]
				launch(REPORT, set(projects_list))
		else:
			print("File does not exist.")
			sys.exit()
	else:
		projects_list = get_project_list()

		if project_id == None:
			launch(REPORT, speed, projects_list)
		elif project_id in projects_list:
			launch(REPORT, speed, [project_id])
		else:
			print(f"You do not appear to have access to project [{project_id}] or it does not exist.")
			sys.exit()

		print(f"\nThe scan took {round(time.time()-t0)} secondes.")


if __name__ == "__main__":
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--report", action="store_true", help="Enable report mode")
	parser.add_argument( "-lp", "--list_projects", action="store_true", help="List projects")
	parser.add_argument("-lu", "--list_users", action="store_true", help="List users")
	parser.add_argument("-pi", "--project_id", required=False, help="Do the compliances checks on this project ID")
	parser.add_argument("-l", "--list", required=False, help="Do the compliances checks on this list of project ID")
	parser.add_argument("-u", "--user", required=False, help="Use this user acccount to do the compliances checks")
	parser.add_argument("-k", "--key", required=False, help="Use this service acccount to do the compliances checks")
	parser.add_argument("-t", "--threads", type=int,required=False, help="Define the numbers of threads")
	parser.add_argument("-s", "--slow", action="store_true", required=False, help="Slower scan, less ressources used")
	parser.add_argument("-f", "--fast", action="store_true", required=False, help="Faster scan, more ressources used")
	args = parser.parse_args()

	if args.key and args.user:
		print("Choose between --user and --key not both")
		sys.exit()

	if args.list_projects and args.list_users:
		print("Choose between --list_projects and --list_users not both")
		sys.exit()

	# if args

	if args.threads and args.slow or args.threads and args.fast or args.slow and args.fast or args.threads and args.slow and args.fast:
		print("You must choose a speed, not multiple ones.")
		sys.exit()

	try:
		main(args.report, args.project_id, args.list, args.user, args.key, args.list_projects, args.list_users, args.threads, args.slow, args.fast)
	except KeyboardInterrupt:
		print("CTRL+C")
		sys.exit()
