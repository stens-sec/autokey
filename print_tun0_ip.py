import netifaces as ni

# inserts the IP address of the tun0 NIC
# to current cursor position
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
  keyboard.send_keys(tun_ip)
