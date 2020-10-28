# pentesting autokey scripts

## description

This repository contains useful scripts for the autokey-software for pentesting purposes.

If you perform some tasks like upgrading reverse shells manually, you definitely want to automate the process to save yourself some time.

I will update these from time to time, so check this repository for updates.

Currently it automates the following tasks:
* upgrade a simple reverse shell to a more fully interactive tty
* insert your tun0-IP at you current cursor position
* download and execute linpeas.sh via wget from your current tun0-IP

## installation

To install autokey for XFCE and the dependencies of these scripts, run

```
sudo apt install -y autokey-gtk python3-netifaces
```

## configuration

Copy and paste the scripts to new script-objects in autokey and assign a hotkey to run them. 
Make sure to change parameters where needed.
