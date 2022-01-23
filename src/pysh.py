# CMD shell enabler
import subprocess, sys
arg = ['cmd']
arg.extend(sys.argv[1:])
subprocess.run(arg)
