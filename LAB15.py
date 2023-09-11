"""
Your module description
You can use Linux to do many administrative tasks from the terminal, or the Bash command line. Python provides several modules that you can also use to run commands on the command line. In this lab, you will use os.system() and subprocess.run() to run Bash commands from Python.

In this lab, you will:

    Use os.system() to run a Bash command
    Use subprocess.run() to run Bash commands

"""
import os
import subprocess



subprocess.run(["ls","-l","README.md"])


command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])