import subprocess
from subprocess import Popen, PIPE
import re

def scan_network():
	#sudo bypass
	sudo_password = 'placeholder' #enter sudo password here
	command = '-'
	command = command.split()
	cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
	cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)

	command = ['sudo', 'arp-scan' ,'-l','-r','5']
	new_list = []
	users_mac = []
	valid_manuf = ['Apple, Inc.', 'Amazon Technologies Inc.', 'Samsung Electronics Co.,Ltd', 'Google Inc.', 'HTC Corporation', 'LG Electronics (Mobile Communications)']

	out = subprocess.check_output(command)
	regex_mac = re.compile(ur'(?:[0-9a-fA-F]:?){12}')
	mac_list = re.findall(regex_mac, out)

	split = out.splitlines()
	split = split[2:-3]

	for x in range(len(split)):
		num = split[x].rfind('\t')
		new_list.append(split[x][num + 1:])

	index = 0
	for x in new_list:
		if x in valid_manuf:
			users_mac.append(mac_list[index])
		index += 1

	return users_mac

def count():
	return len(scan_network())