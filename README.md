<p align="center">
![](/Images/logo.png)
  
<p align="center">A python3 script, which scan and report your Google Cloud Platfrom non compliance.

<p align="center">
  <a href="#introduction">Introduction</a>
 • <a href="#main-features">Main Features</a>
 • <a href="#requirements">Requirements</a>
 • <a href="#installation">Installation</a>
 • <a href="#usage">Usage</a>
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

- Bla
- Bla
- Bla

## Requirements

You will need to have a Google account and those tools installed.

### Tools

- [gcloud](https://cloud.google.com/sdk/docs/install#deb)
- python3

Now you need to authorize gcloud to access the Cloud Platform with Google user credentials.

```bash
gcloud auth login
```

## Installation

```bash
git clone https://github.com/Liodeus/Good-Cloud-Practice
cd Good-Cloud-Practice
pip3 install -r requirements.txt
```

## Usage

```bash
Usage: Good_Cloud_Practice.py [-h] [-r] [-lp] [-lu] [--project_id PROJECT_ID]

optional arguments:
  -h, --help            show this help message and exit
  -r, --report          Enable report mode
  -lp, --list_projects  List projects
  -lu, --list_users     List users
  --project_id PROJECT_ID
                        Do the checks on this project-id
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Thanks

Thanks to this project : [ram](https://github.com/BrunoReboul/ram) for most of the inspiration.
