import subprocess
from subprocess import Popen, PIPE
import re
import time

def scan_network():
	#sudo bypass
	sudo_password = 'placeholder' #sudo password here
	command = '-'
	command = command.split()
	cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
	cmd2 = subprocess.Popen(['sudo','-s'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)

	current_time = time.time()

	command = ['sudo', 'arp-scan' ,'-l','-r','5']
	manu_list = []
	users = []
	valid_mac = ['1c:1a:c0:8f:45:88', '3c:ab:8e:d2:63:58', '28:e0:2c:6d:b2:46', 'ac:63:be:c0:a1:d1']
	valid_names = ['John', 'Jane', 'Mary', 'Andy']

	out = subprocess.check_output(command).decode('utf-8')
	regex_mac = re.compile('\s+((?:[0-9A-Fa-f]{2}:){5}(?:[0-9A-Fa-f]){2})\s+')
	mac_list = re.findall(regex_mac, out)

	split = out.splitlines()
	split = split[2:-3]

	for x in range(len(split)):
		num = split[x].rfind('\t')
		manu_list.append(split[x][num + 1:])

	index = 0
	for x in mac_list:
		if x in valid_mac:
			users.append((mac_list[index], manu_list[index], current_time, valid_names[valid_mac.index(x)]))
		index += 1
	return users

def count():
	return len(scan_network())