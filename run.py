#https://unix.stackexchange.com/questions/9107/how-can-i-run-firefox-on-linux-headlessly-i-e-without-requiring-libgtk-x11-2-0
#to use without a display: sudo apt install xvfb
#then: xvfb-run -a python3 run.py <MessengerID> [Browser]

#https://askubuntu.com/questions/661186/how-to-install-previous-firefox-version
#sudo apt-get install firefox=75.0+build3-0ubuntu1

import os
import sys
import time
import signal
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
#https://superuser.com/questions/731467/command-line-option-to-open-chrome-in-new-window-and-move-focus
funcs = {
    'nt': lambda: subprocess.Popen([browser or 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', '-new-window', url]),
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


print('\nBot Started.')

i = 0
while True:
    i += 1
    try:
        print('\rRestarting browser: ' + str(i), end='')
        proc = func()
        time.sleep(10)
        proc.kill()
        #Windows, Windows...
        if os.name == 'nt' and browser is None: subprocess.run(['taskkill', '-f', '-im', 'msedge.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        print('Error: An exception occured while attempting to open a browser. ' + tips[os.name])
        print('')
        raise
