from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt
import numpy as np

all_results = {}


def markdown_to_report(project, mitigation_name, information, severity, compliant_or_not):
	with open(f"./mitigations/{mitigation_name}") as f:
		mitigation = f.read()
		information = replace_for_html(information)
		background = replace_for_html('\n'.join(mitigation.split('## Fix')[0].split('\n')[4:-2]).strip())

		fix = replace_for_html(mitigation.split('## Fix')[1].split('## References')[0].strip())
		references = replace_for_html(mitigation.split('## Fix')[1].split('## References')[1].strip())

		if not compliant_or_not:
			if "API" in information:
				tmp = [severity, information]
				try:
					all_results[project]["errors"][mitigation_name[:-3]] = tmp
				except KeyError:
					all_results[project] = {"non_compliant":{}, "compliant":{}, "errors": {}}
					all_results[project]["errors"][mitigation_name[:-3]] = tmp
			else:
				tmp = [severity, information, background, fix, references]
				try:
					all_results[project]["non_compliant"][mitigation_name[:-3]] = tmp
				except KeyError:
					all_results[project] = {"non_compliant":{}, "compliant":{}, "errors": {}}
					all_results[project]["non_compliant"][mitigation_name[:-3]] = tmp
		else:
			tmp = [severity, background]
			try:			
				all_results[project]["compliant"][mitigation_name[:-3]] = tmp
			except KeyError:
				all_results[project] = {"non_compliant":{}, "compliant":{}, "errors": {}}
				all_results[project]["compliant"][mitigation_name[:-3]] = tmp


def replace_for_html(strg):
	return strg.replace('\n', '</br>').replace('\t', '&emsp;').replace("```shell", "<code>").replace("```", "</code>")


def generate_html(date, user):
	file_loader = FileSystemLoader("functions/report/template")
	env = Environment(loader=file_loader)
	template = env.get_template('template.html')


	output = template.render(all_results=all_results, date=date, user=user)

	with open("report.html", "w") as result_file:
	    result_file.write(output)


def genereta_graph_by_severity(height_severity, project):
	bars = ("Critical", "Major", "Medium", "Minor")
	y_pos = np.arange(len(bars))

	plt.bar(y_pos, height_severity, color=["red", "orange", "green", "cyan"])
	plt.xticks(y_pos, bars, )
	plt.title("Non compliance by severity")
	plt.savefig(f"functions/report/graph_images/graph_by_severity_{project}.png")
	plt.clf()


def genereta_graph_by_types(height_types, project):
	bars = ("BQ", "CLOUDDNS", "GAE", "GCE", "GCF", "CLOUDSQL")
	y_pos = np.arange(len(bars))

	plt.bar(y_pos, height_types)
	plt.xticks(y_pos, bars, )
	plt.title("Non compliance by types")
	plt.savefig(f"functions/report/graph_images/graph_by_types_{project}.png")
	plt.clf()
