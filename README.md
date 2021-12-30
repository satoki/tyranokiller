# TyranoKiller
👻 Code injection tool for Tyrano.  
![main.png](images/main.png)  
CVE-XXXX-XXXX (0day)  

**⚠Don't use untrusted files!!!⚠**  

The vulnerability was disclosed after 365 days of reporting to IPA and developers.  
I have also received a response that it is not a vulnerability.  
This PoC was created to alert users and investigate vulnerabilities in their own games, and is not to be used for attacks.  

## Vulnerability
All games created with the tools listed below have a vulnerability in the save data file.  
- TyranoBuilder <= 1.87b  
- TyranoBuilderV5 <= 2.02  
- TyranoRider <= 2.20  
- TyranoStudio <= 1.10d  
- (TyranoScript <= 4.88)  
- (TyranoScriptV5 <= 5.11d)  

Attackers can use Node.js functionality from JavaScript by embedding HTML tags in save data files, allowing them to execute arbitrary code.
They can also do that using the game development data `index.html`.
The ability to inject into index.html is not included in this tool, but by previewing the game with the following code embedded, it becomes XSS to ACE.  
```html
<script>
require("child_process").exec("calc");
</script>
```

### Demo
![calc.gif](images/calc.gif)  
(Sample Game: https://tyrano.jp/)  

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
The code will only be injected into the first save data.  
