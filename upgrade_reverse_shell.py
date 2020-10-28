# autokey script to automatically upgrade a reverse shell
# to a better interactive shell which supports most features
# of a full tty and keystrokes like ctrl+c
#
# to install, copy and paste this code
# to a new script in autokey and set a hotkey


# found no way to dynamically determine cols and rows
# via tput or stty -a because this script does not run in a shell
# set manually to fit your needs

_cols = 220
_rows = 50

keyboard.send_keys("python -c \"import pty; pty.spawn('/bin/bash')\"")
keyboard.send_keys("<enter>")
time.sleep(1)
keyboard.send_keys("<ctrl>+z")
time.sleep(0.5)

keyboard.send_keys('stty raw -echo')
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('fg')
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('fg')
keyboard.send_keys("<enter>")
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('stty rows {} columns {}'.format(_rows,_cols))
keyboard.send_keys("<enter>")
time.sleep(0.5)

keyboard.send_keys('export TERM=xterm-256color')
keyboard.send_keys("<enter>")

