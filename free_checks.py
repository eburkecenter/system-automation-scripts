#!/usr/bin/env python3
import os
import sys
import shutil

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

def main():
	if check_reboot():
		print("Pending Reboot")
		sys.exit(1)
	if check_root_full():
		print("Full Disk")
		sys.exit(1)
	print("Everything is okay")
	sys.exit(0)


main()