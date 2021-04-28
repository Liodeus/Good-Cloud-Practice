<p align="center">
  <img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/images/logo.png" alt="Logo">
  
<p align="center">A python3 script, which scan and generate a html report about your Google Cloud Platfrom non compliance.

<p align="center">
  <a href="#introduction">Introduction</a>
 • <a href="#main-features">Main Features</a>
 • <a href="#requirements">Requirements</a>
 • <a href="#installation">Installation</a>
 • <a href="#usage">Usage</a>
 • <a href="#Examples">Examples</a>
 • <a href="#HTML-report">HTML report</a>
 • <a href="#contributing">Contributing</a>
 • <a href="#thanks">Thanks</a>
</p>

<div align="center">
  <sub>Created by
  <a href="https://liodeus.github.io/">Liodeus</a>
</div>

## Introduction

I made this tool to learn security on Google Cloud Platform.

## Main Features

- BigQuery checks : 1
- Cloud DNS checks : 2
- Google AppEngine checks : 4
- Google Compute Engine checks : 13
- Google Cloud Function checks : 4
- Cloud SQL checks : 4
- Google Cloud Storage : 1

## Requirements

You will need to have a Google account and those tools installed.

### Tools

- [gcloud](https://cloud.google.com/sdk/docs/install#deb)
- python3
- python3-pip

Once gcloud is installed, you need to authorize gcloud to access the Cloud Platform with Google user credentials or use a service account via a key :

#### Authorize gcloud
```bash
gcloud auth login
```

##### Service account

1. In the Cloud Console, go to the Service accounts page.
2. Select a project.
3. Click Create service account.
   Enter a service account name to display in the Cloud Console.
4. The Cloud Console generates a service account ID based on this name. Edit the ID if necessary. You cannot change the ID later.
5. To set access controls, click Create and continue to the next step.
6. Choose one or more IAM roles to grant to the service account on the project.
7. Grant the role : Viewer
8. When you are done adding roles, click Continue.

##### Generate keys

1. Click on your newly created account
2. Go to keys panel
3. Add key -> Create new key
4. Key type : JSON
5. Click create and store the key securely

## Installation

```
git clone https://github.com/Liodeus/Good-Cloud-Practice
cd Good-Cloud-Practice
pip3 install -r requirements.txt
```

## Usage

```
Usage: Good_Cloud_Practice.py [-h] [-r] [-lp] [-lu] [-pi PROJECT_ID] [-l LIST] [-u USER] [-k KEY]

optional arguments:
  -h, --help            show this help message and exit
  -r, --report          Enable report mode
  -lp, --list_projects  List projects
  -lu, --list_users     List users
  -pi PROJECT_ID, --project_id PROJECT_ID
                        Do the compliances checks on this project ID
  -l LIST, --list LIST  Do the compliances checks on this list of project ID
  -u USER, --user USER  Use this user acccount to do the compliances checks
  -k KEY, --key KEY     Use this service acccount to do the compliances checks
```

## Examples

Run all the compliances checks on every projects :
```shell
python3 Good_Cloud_Practice.py
```

Run all the compliances checks on every projects and enable report mode :
```shell
python3 Good_Cloud_Practice.py -r
```

Run all the compliances checks on a particular project :
```shell
python3 Good_Cloud_Practice.py --project_id mystic-sun-309920
```

Use a service account :
```shell
python3 Good_Cloud_Practice.py -k path_of_the_key.json
```

List users
```shell
python3 Good_Cloud_Practice.py -lu
```

Use a particular account
```shell
python3 Good_Cloud_Practice.py -u ACCOUNT
```

## HTML report

### Header
Print the user who launch the scan and the date of the scan.
<img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/images/header.png" alt="Logo">

### Global section
With a summary of all the non compliances (only printed if there is more thant one project scan).
<img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/images/global.png" alt="Global">

### Report section
Print the name of the project scanned, the summary of non compliances found and the result underneath.
<img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/images/section.png" alt="Section">

### Results
Once the "Results" are unfold, you have three sections.
<img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/images/unfold_section.png" alt="Unfold section">

### Section
Here's what you can see once the "Non compliant" section is unfold.
<img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/images/unfold_section_two.png" alt="Unfold section two">

### Footer
And finally the footer, with some links and at the right side a "Back to the top" button.
<img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/images/footer.png" alt="Footer">

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Thanks

Thanks to this project : [ram](https://github.com/BrunoReboul/ram) for most of the inspiration.
