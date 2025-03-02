import anvil.server
import subprocess

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def start_jobs():
  #command = ["/usr/bin/mate-terminal", "-e", "/home/kean/doit.sh /home/kean/tmp ls -m"]
  #command = ["c:/cygwin64/bin/mintty.exe", "--exec", "c:/cygwin64/bin/bash", "-lic", "c:/tmp/Raptor/doit.sh c:/tmp/Raptor/tmp ls -m"]

  command = ["c:/cygwin64/bin/mintty.exe", "--exec", "c:/cygwin64/bin/bash", "-lic", "c:/tmp/Raptor/doit.sh c:/work/gsdk/extension/se_firmware pipenv run make-fw --no_docker --compiler gcc rainier -j -B debug --development --fpga"]
  subprocess.Popen(command, start_new_session=True)

  command = ["c:/cygwin64/bin/mintty.exe", "--exec", "c:/cygwin64/bin/bash", "-lic", "c:/tmp/Raptor/doit.sh c:/work/gsdk/extension/se_firmware pipenv run make-rom-dev RAINIER --no_docker --compiler gcc release -j -B"]
  subprocess.Popen(command, start_new_session=True)
  