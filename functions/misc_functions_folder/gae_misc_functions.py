from functions.misc_functions_folder.misc_functions import *


def get_secret_search():
	"""
		Return all the regex to search
	"""
	return {
		'AWS Access Key ID Value': '(A3T[A-Z0-9]|AKIA|AGPA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}',
		'AWS Access Key ID': '((\"|''|`)?((?i)aws)?_?((?i)access)_?((?i)key)?_?((?i)id)?(\"|''|`)?\\s{0,50}(:|=>|=)\\s{0,50}(\"|''|`)?(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}(\"|''|`)?)',
		'AWS Account ID': '((\"|''|`)?((?i)aws)?_?((?i)account)_?((?i)id)?(\"|''|`)?\\s{0,50}(:|=>|=)\\s{0,50}(\"|''|`)?[0-9]{4}-?[0-9]{4}-?[0-9]{4}(\"|''|`)?)',
		'AWS Secret Access Key': '((\"|''|`)?((?i)aws)?_?((?i)secret)_?((?i)access)?_?((?i)key)?_?((?i)id)?(\"|''|`)?\\s{0,50}(:|=>|=)\\s{0,50}(\"|''|`)?[A-Za-z0-9/+=]{40}(\"|''|`)?)',
		'AWS Session Token': '((\"|''|`)?((?i)aws)?_?((?i)session)?_?((?i)token)?(\"|''|`)?\\s{0,50}(:|=>|=)\\s{0,50}(\"|''|`)?[A-Za-z0-9/+=]{16,}(\"|''|`)?)',
		'Artifactory': '(?i)artifactory.{0,50}(\"|''|`)?[a-zA-Z0-9=]{112}(\"|''|`)?',
		'CodeClimate': '(?i)codeclima.{0,50}(\"|''|`)?[0-9a-f]{64}(\"|''|`)?',
		'Facebook access token': 'EAACEdEose0cBA[0-9A-Za-z]+',
		'Google (GCM) Service account': '(("|''|`)?type(\"|''|`)?\\s{0,50}(:|=>|=)\\s{0,50}(\"|''|`)?service_account(\"|''|`)?,?)',
		'Stripe API key': '(?:r|s)k_[live|test]_[0-9a-zA-Z]{24}',
		'Google OAuth Key': '[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com',
		'Google Cloud API Key': 'AIza[0-9A-Za-z\\-_]{35}',
		'Google OAuth Access Token': 'ya29\\.[0-9A-Za-z\\-_]+',
		'Picatic API key': 'sk_[live|test]_[0-9a-z]{32}',
		'Square Access Token': 'sq0atp-[0-9A-Za-z\-_]{22}',
		'Square OAuth Secret': 'sq0csp-[0-9A-Za-z\-_]{43}',
		'PayPal/Braintree Access Token': 'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
		'Amazon MWS Auth Token': 'amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
		'Twilo API Key': 'SK[0-9a-fA-F]{32}',
		'SendGrid API Key': 'SG\.[0-9A-Za-z\-_]{22}\.[0-9A-Za-z\-_]{43}',
		'MailGun API Key': 'key-[0-9a-zA-Z]{32}',
		'MailChimp API Key': '[0-9a-f]{32}-us[0-9]{12}',
		'SSH Password': 'sshpass -p.*[''|\"]',
		'Outlook team': '(https://outlook.office.com/webhook/[0-9a-f-]{36}@)',
		'Sauce Token': '(?i)sauce.{0,50}(\"|''|`)?[0-9a-f-]{36}(\"|''|`)?',
		'Slack Token': '(xox[pboa]-[0-9]{12}-[0-9]{12}-[A-Za-z0-9]{24})',
		'Slack Token': '(xox[pboa]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})',
		'Slack Webhook': 'https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}',
		'SonarQube Docs API Key': '(?i)sonar.{0,50}(\"|''|`)?[0-9a-f]{40}(\"|''|`)?',
		'HockeyApp': '(?i)hockey.{0,50}(\"|''|`)?[0-9a-f]{32}(\"|''|`)?',
		'Username and password in URI': '([\w+]{1,24})(://)([^$<]{1})([^\s";]{1,}):([^$<]{1})([^\s";/]{1,})@[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,24}([^\s]+)',
		'NuGet API Key': 'oy2[a-z0-9]{43}',
		'StackHawk API Key': 'hawk\.[0-9A-Za-z\-_]{20}\.[0-9A-Za-z\-_]{20}',
		'Contains a private key': '-----BEGIN (EC |RSA |DSA |OPENSSH |PGP |)PRIVATE KEY',
		'WP-Config': 'define(.{0,20})?(DB_CHARSET|NONCE_SALT|LOGGED_IN_SALT|AUTH_SALT|NONCE_KEY|DB_HOST|DB_PASSWORD|AUTH_KEY|SECURE_AUTH_KEY|LOGGED_IN_KEY|DB_NAME|DB_USER)(.{0,20})?[''|"].{10,120}[''|"]',
		'AWS cred file info': '(?i)(aws_access_key_id|aws_secret_access_key)(.{0,20})?=.[0-9a-zA-Z\/+]{20,40}',
		'Facebook Client ID': '(?i)(facebook|fb)(.{0,20})?[''\"][0-9]{13,17}[''\"]',
		'Twitter Secret Key': '(?i)twitter(.{0,20})?[''\"][0-9a-z]{35,44}[''\"]',
		'Twitter Client ID': '(?i)twitter(.{0,20})?[''\"][0-9a-z]{18,25}[''\"]',
		'Heroku API key': '(?i)heroku(.{0,20})?[''"][0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}[''"]',
		'LinkedIn Secret Key': '(?i)linkedin(.{0,20})?[''\"][0-9a-z]{16}[''\"]'
	}


def get_languages():
	"""
		Return all the language accepted
	"""
	return {
		"go": ["go111" , "go112", "go113", "go114", "go115", "go116"],
		"ja": ["java11", "java8"],
		"no": ["nodejs10", "nodejs12", "nodejs14"],
		"ph": ["php72", "php73", "php74"],
		"py": ["python37", "python38", "python39"],
		"ru": ["ruby25", "ruby26", "ruby27"]
	}


def gae_reduce(cmd_list, function_name, lock, project, mitigation_name, severity):
	"""
		Google AppEngine function lines of code reducer
	"""
	result = {}

	if function_name == "gae_location":
		try:
			yaml_datas = yaml.load(exec_cmd(cmd_list[0]), Loader=yaml.FullLoader)
		except yaml.scanner.ScannerError:
			pretty_print_error(lock, f"GAE {function_name}", "Missing permission", True, project, mitigation_name, severity)
	
		if "ERROR" in yaml_datas:
			pretty_print_error(lock, f"GAE {function_name}", "The current Google Cloud project does not contain an App Engine application", True, project, mitigation_name, severity)

		if "europe" not in yaml_datas["locationId"]:
			result["location"] = yaml_datas["locationId"]

	else:	
		datas = exec_cmd(cmd_list[0])

		if "ERROR:" in datas:
			pretty_print_error(lock, f"GAE {function_name}", "Missing permission", True, project, mitigation_name, severity)

		datas = datas.split('\n')[1:-1]

		for data in datas:
			if function_name in ["gae_max_version"]:
				result[data.split()[1]] = ""
			else:
				result[data.split()[1]] = data.split()[0]

	return result


def gae_reduce_two(result, cmd_list, function_name):
	"""
		Google AppEngine function lines of code reducer two
	"""
	res = {}

	for version, service in result.items():
		cmd = f"{cmd_list[1]}{service} {version}"
		yaml_result = yaml.load(exec_cmd(cmd), Loader=yaml.FullLoader)
		yaml_result_name_variable = yaml_result["name"]

		if function_name in ["gae_env_secret"]:
			secret_search_list = get_secret_search()
			try:
				yaml_result_env_variable = yaml_result["envVariables"]
			except KeyError:
				continue

			for var, value in yaml_result_env_variable.items():
				for secret_name, regex in secret_search_list.items():
					regex_result = re.search(regex, value)
					if regex_result:
						val = {secret_name: regex_result.group()}
						try:
							res[yaml_result_name_variable].append(val)
						except KeyError:
							res[yaml_result_name_variable] = []
							res[yaml_result_name_variable].append(val)
		elif function_name in ["gae_runtime"]:
			yaml_result_runtime_variable = yaml_result["runtime"]
			languages = get_languages()

			try:
				short = yaml_result_runtime_variable[:2]
				gae_runtime_result = {}
				if yaml_result_runtime_variable in languages[short]:
					continue
				else:
					gae_runtime_result[yaml_result_name_variable] = yaml_result_runtime_variable
			except:
				print("error")
				print(yaml_result_runtime_variable)
				break
	return res
