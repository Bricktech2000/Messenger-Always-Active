#https://unix.stackexchange.com/questions/9107/how-can-i-run-firefox-on-linux-headlessly-i-e-without-requiring-libgtk-x11-2-0
#to use without a display: sudo apt install xvfb
#then: xvfb-run -a python3 run.py <MessengerID> [Browser]

import os
import sys
import time
import subprocess


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Error: Usage: run.py <MessengerID> [Browser]')
    exit(1)
id = sys.argv[1]
browser = None
if len(sys.argv) == 3: browser = sys.argv[2]
url = 'https://www.messenger.com/t/' + id

print('Note: Make sure you log into Messenger if you are promped to.')

#https://stackoverflow.com/questions/7032212/how-to-run-application-with-parameters-in-python
#https://stackoverflow.com/questions/31164253/how-to-open-url-in-microsoft-edge-from-the-command-line
#https://stackoverflow.com/questions/1196074/how-to-start-a-background-process-in-python
funcs = {
    'nt': lambda: subprocess.Popen(['explorer.exe', 'microsoft-edge:' + url]),
    'posix': lambda: subprocess.Popen([browser or 'firefox', url]),
}
tips = {
    'nt': 'Make sure Microsoft Edge is installed',
    'posix': 'Make sure Mozilla Firefox is installed. If you wish to use a different browser, provide it as a third commandline argument.'
}
func = funcs.get(os.name)
if func is None:
    print('Error: Unsupported OS: ' + os.name)
    exit(1)

try:
    proc = func()
except:
    print('Error: An exception occured while attempting to open a browser. ' + tips[os.name])
    print('')
    raise

print('\nBrowser Started.')

while True:
    time.sleep(1)
