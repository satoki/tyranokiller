# TyranoKiller
Code injection tool for Tyrano.  
![main.png](images/main.png)  
CVE-XXXX-XXXX (0day)  

## Vulnerability
All games created with the tools listed below have a vulnerability in the save data file.  
- TyranoBuilder <= 2.00  
- TyranoRider <= 2.10  
- TyranoScript <= 5.00  

Attackers can use Node.js functionality from JavaScript by embedding HTML tags in save data files, allowing them to execute arbitrary code.
Don't use untrusted files.  

## Usage
```bash
usage: tyranokiller.py [-h] [-c COMMAND] filename

positional arguments:
  filename              Specify the target sav file name

optional arguments:
  -h, --help            show this help message and exit
  -c COMMAND, --command COMMAND
                        Specify the command to be injected
```
The default is to execute the `calc` command.  