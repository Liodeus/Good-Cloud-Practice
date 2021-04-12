from functions.cmds_args import *
import argparse
import os.path
import time
import sys


def main(REPORT, project_id=None, path=None):
	t0 = time.time()
	get_date()

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
			launch(REPORT, projects_list)
		elif project_id in projects_list:
			launch(REPORT, [project_id])
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
	args = parser.parse_args()

	if args.list_projects:
		list_projects()
	elif args.list_users:
		list_users()

	try:
		main(args.report, args.project_id, args.list)
	except KeyboardInterrupt:
		print("CTRL+C")
		sys.exit()
