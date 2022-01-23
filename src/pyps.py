# PowerShell enabler
import subprocess, sys
arg = ['powershell']
arg.extend(sys.argv[1:])
subprocess.run(arg)
