<p align="center">
  <img src="https://github.com/Liodeus/Good-Cloud-Practice/blob/main/Images/logo.png" alt="Logo">
  
<p align="center">A python3 script, which scan and report your Google Cloud Platfrom non compliance.

<p align="center">
  <a href="#introduction">Introduction</a>
 • <a href="#main-features">Main Features</a>
 • <a href="#requirements">Requirements</a>
 • <a href="#installation">Installation</a>
 • <a href="#usage">Usage</a>
 • <a href="#Examples">Examples</a>
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
- Google Compute Engine checks : 8
- Google Cloud Function checks : 4
- Cloud SQL checks : 4

## Requirements

You will need to have a Google account and those tools installed.

### Tools

- [gcloud](https://cloud.google.com/sdk/docs/install#deb)
- python3
- python3-pip - (sudo apt install python3-pip)

Once gcloud is installed, you need to authorize gcloud to access the Cloud Platform with Google user credentials.

```bash
gcloud auth login
```

## Installation

```
git clone https://github.com/Liodeus/Good-Cloud-Practice
cd Good-Cloud-Practice
pip3 install -r requirements.txt
```

## Usage

```
Usage: Good_Cloud_Practice.py [-h] [-r] [-lp] [-lu] [--project_id PROJECT_ID]

optional arguments:
  -h, --help            show this help message and exit
  -r, --report          Enable report mode
  -lp, --list_projects  List projects
  -lu, --list_users     List users
  -pi PROJECT_ID, --project_id PROJECT_ID
                        Do the compliances checks on this project ID
  -l LIST, --list LIST  Do the compliances checks on this list of project ID
```

## Examples

Run all the compliances checks on every projects :
```
python3 Good_Cloud_Practice.py
```

Run all the compliances checks on every projects and enable report mode :
```
python3 Good_Cloud_Practice.py -r
```

Run all the compliances checks on a particular project :
```
python3 Good_Cloud_Practice.py --project_id mystic-sun-309920
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Thanks

Thanks to this project : [ram](https://github.com/BrunoReboul/ram) for most of the inspiration.
