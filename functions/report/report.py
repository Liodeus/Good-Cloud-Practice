from jinja2 import Environment, FileSystemLoader
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np


all_results = {}
mitigation_to_name = {
	"gce_instance_externalip": "Google Compute Engine instance external IP",
	"gce_instance_location": "Google Compute Engine instance location",
	"gce_instance_service_account": "Google Compute Engine instance service account",
	"gce_disk_location": "Google Compute Engine disk location",
	"gce_firewallrule_log": "Google Compute Engine firewall rule log",
	"gce_ip_forwarding": "Google Compute Engine IP forwarding",
	"gce_network_name": "Google Compute Engine network name",
	"gce_shielded_instances": "Google Compute Engine shielded instances",
	"gae_runtime": "Google AppEngine runtine",
	"gae_env_secret": "Google AppEngine environment secret",
	"gae_max_version": "Google AppEngine max version",
	"gae_location": "Google AppEngine location",
	"clouddns_dnssec": "Cloud DNS DNSSEC",
	"clouddns_rsasha1": "Cloud DNS RSASHA1",
	"bq_dataset_location": "BigQuery Dataset Location",
	"gcf_env_secret": "Google Cloud Function environment secret",
	"gcf_location": "Google Cloud Function location",
	"gcf_runtime": "Google Cloud Function runtime",
	"gcf_service_account": "Google Cloud Function service account",
	"cloudsql_backup": "Cloud SQL backup",
	"cloudsql_backup_location": "Cloud SQL backup location",
	"cloudsql_location": "Cloud SQL location",
	"cloudsql_maintenance": "Cloud SQL maintenance"
}

def markdown_to_report(project, mitigation_name, information, severity, compliant_or_not):
	with open(f"./mitigations/{mitigation_name}") as f:
		mitigation = f.read()
		information = replace_for_html(information)
		background = replace_for_html(ref_to_href('\n'.join(mitigation.split('## Fix')[0].split('\n')[4:-2]).strip()))
		mitigation_name = mitigation_to_name[mitigation_name[:-3]]
		fix = replace_for_html(ref_to_href(mitigation.split('## Fix')[1].split('## References')[0].strip()))
		references = ref_to_href(mitigation.split('## Fix')[1].split('## References')[1].strip())

		if not compliant_or_not:
			if "API" in information or "Missing permission" in information:
				tmp = [severity, information]
				try:
					all_results[project]["errors"][mitigation_name] = tmp
				except KeyError:
					all_results[project] = {"non_compliant":{}, "compliant":{}, "errors": {}, "numbers_results": []}
					all_results[project]["errors"][mitigation_name] = tmp
			else:
				tmp = [severity, information, background, fix, references]
				try:
					all_results[project]["non_compliant"][mitigation_name] = tmp
				except KeyError:
					all_results[project] = {"non_compliant":{}, "compliant":{}, "errors": {}, "numbers_results": []}
					all_results[project]["non_compliant"][mitigation_name] = tmp
		else:
			tmp = [severity, background]
			try:			
				all_results[project]["compliant"][mitigation_name] = tmp
			except KeyError:
				all_results[project] = {"non_compliant":{}, "compliant":{}, "errors": {}, "numbers_results": []}
				all_results[project]["compliant"][mitigation_name] = tmp


def replace_for_html(strg):
	return strg.replace('\n', '</br>').replace('\t', '&emsp;').replace("```shell", "<div class='code'>").replace("```", "</div>")


def ref_to_href(refs):
	strg = ""
	if refs:
		for ref in refs.split('\n'):
			if ref[:3] == "- [" or ref[:3] == "\t- ":
				ref = ref[2:]
				tmp = ref.split('(')

				url = f'- <a href="{tmp[1][:-1]}">{tmp[0][1:-1]}</a>'
				strg += f"{url}</br>"
			else:
				strg += f"{ref}\n"
		
	return strg


def generate_html(date, user, folder_name, global_heights):
	final = {}
	file_loader = FileSystemLoader("functions/report/template")
	env = Environment(loader=file_loader)
	template = env.get_template('template.html')

	for key in all_results.keys():
		non_compliant_number = len(all_results[key]["non_compliant"])
		compliant_number = len(all_results[key]["compliant"])
		errors_number = len(all_results[key]["errors"])
		all_results_number = non_compliant_number + compliant_number + errors_number

		all_results[key]["numbers_results"].append(all_results_number)
		all_results[key]["numbers_results"].append(non_compliant_number)
		all_results[key]["numbers_results"].append(compliant_number)
		all_results[key]["numbers_results"].append(errors_number)
		for k in all_results[key].keys():
			try:
				final[key][k] = sorted(all_results[key][k].items(), key=lambda x:x[1])
			except KeyError:
				final[key] = {"non_compliant":[], "compliant":[], "errors": [], "numbers_results": []}
				final[key][k] = sorted(all_results[key][k].items(), key=lambda x:x[1])
			except AttributeError:
				final[key][k] = all_results[key][k]

	output = template.render(all_results=final, size=len(final),date=date[:10], user=user)

	with open(f"{folder_name}/report.html", "w") as result_file:
	    result_file.write(output)


def genereta_graph_by_severity(height_severity, project, folder_name, state):
	bars = ("Critical", "Major", "Medium", "Minor")
	y_pos = np.arange(len(bars))
	plt.bar(y_pos, height_severity, color=["red", "orange", "green", "cyan"])
	plt.xticks(y_pos, bars, )
	plt.title("Non compliance by severity")

	if state:
		plt.savefig(f"{folder_name}/graph_images/graph_by_severity_{project}.png")
	else:
		plt.savefig(f"{folder_name}/graph_images/graph_by_severity_global.png")
	
	plt.clf()


def genereta_graph_by_types(height_types, project, folder_name, state):
	bars = ("BQ", "CLOUDDNS", "GAE", "GCE", "GCF", "CLOUDSQL")
	y_pos = np.arange(len(bars))
	plt.bar(y_pos, height_types)
	plt.xticks(y_pos, bars, )
	plt.title("Non compliance by types")

	if state:
		plt.savefig(f"{folder_name}/graph_images/graph_by_types_{project}.png")
	else:
		plt.savefig(f"{folder_name}/graph_images/graph_by_types_global.png")

	plt.clf()
