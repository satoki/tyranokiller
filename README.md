# TyranoKiller
OS command injection PoC tool for Tyrano.  
![main.png](images/main.png)  
CVE-XXXX-XXXX  

## Vulnerability
All games created with the tools listed below have an OS command injection vulnerability in the save data file.  
Use only trusted save data files.  
- TyranoBuilder <= 2.00  
- TyranoRider <= 2.10  
- TyranoScript <= 5.00  

The attackers can embed HTML tags in the save data file.  
This allows JavaScript to be executed on the game, using the full functionality of Node.js.  

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
