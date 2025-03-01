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
  command = ["/usr/bin/mate-terminal", "-e", "/home/kean/doit.sh /home/kean/tmp ls -m"]
  subprocess.Popen(command, start_new_session=True)
  subprocess.Popen(command, start_new_session=True)
  