import subprocess
import re
import os
import sys
import json
import time

APPNAME = sys.argv[1]


def check_app_status():
    print(f"Checking state of App {APPNAME}.")
    output = subprocess.run(re.split("\s+", f"heroku ps -a {APPNAME} --json"),
                            capture_output=True,
                            text=True
                            )
    if output.stdout:
        print(output.stdout)
    if output.stderr:
        print('There was an error from heroku cli, check it out:')
        print(output.stderr)

    app_info = json.loads(output.stdout)
    app_state = app_info[0]['state']
    if app_state == 'up':
        print(f"App {APPNAME} is up. Ready to migrate.")
        return
    elif (app_state == 'starting') or (app_state == 'restarting'):
        print(f"App {APPNAME} is still starting up. Trying again")
        time.sleep(1)
        check_app_status()
    else:
        print(f"Error: App {APPNAME} is in state {app_state}")
        sys.exit(1)


check_app_status()
