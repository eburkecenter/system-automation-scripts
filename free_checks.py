#!/usr/bin/env python3
import os
import sys
import shutil
import psutil 
import socket




def check_reboot():
	"""Returns True if the computer has a pending reboot"""
	return os.path.exists("/run/reboot-required")

def check_root_full():
	"""Returns True if the root partition is full, False otherwise"""
	return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_disk_full(disk, min_gb, min_percent):
	"""Returns True if there isn't enough disk space, False otherwise."""
	du = shutil.disk_usage(disk)
	#calculate the percentage of the free space
	percentage_free = 100 * du.free / du.total
	#Calculate how many free gigbytes
	gigabytes_free = du.free / 2**30
	if gigabytes_free < min_gb or percentage_free < min_percent:
		return True
	return False


def check_cpu_constrained():
	"""Returns True if the cpu is having too much usage, False otherwise"""
	return psutil.cpu_percent(1)>75


def check_no_network():
	"""Returns True if it fails to resole Google's URL, False otherwise"""
	try: 
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks = [
		(check_reboot, "Pending Reboot"),
		(check_root_full, "Root partition full"),
		(check_no_network, "Not connection to network")
	]

	status_ok = True
	for check, message in checks: 
		if check():
			print(message)
			status_ok = False
	if not status_ok:
		sys.exit(1)
			
	print("Everything is okay")
	sys.exit(0)

if __name__=="__main__":
	main()

