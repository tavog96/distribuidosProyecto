from subprocess import Popen
import subprocess
sp = subprocess.Popen('python startServer.py', shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
output, error = sp.communicate()