import subprocess

# User input
user = input("Enter username: ")

# Vulnerable code
subprocess.call(f"grep '{user}' /etc/passwd", shell=True)

##InstructLLM response
##The code is vulnerable to command injection. The user input is passed to the grep command as a parameter, which allows an attacker to execute arbitrary commands on the system by injecting malicious code into the user variable. For example, an attacker could inject a command to execute a shell script with elevated privileges, potentially leading to a full system compromise.
##The problem is that the shell=True parameter is used in the subprocess.call function, which allows the command to be executed directly by the shell instead of being passed as a string to the system's grep command.