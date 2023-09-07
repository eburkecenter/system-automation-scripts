#!/usr/bin/env python3
import re
import operator
import csv 
import os
""" This is a script is used to process logs """

def errors_log(file):
	"""
   	Function takes text or list as inputs and find all the errors.
   	The errors are grouped in a dictionary 
   	It returns a sorted dictionary of errors
	"""
	errors_dict = {}
	for line in file:
		match = re.search(r"ticky: ERROR: ([\w ]*) ", line)
		if match:
			error = match.group(1)
			if error not in errors_dict:
				errors_dict[error] = 0
			errors_dict[error] +=1
	return errors_dict

def info_log(file):
	"""
   	Function takes a file as input and categorize all users ticket interaction.
   	The two categories are info and errors
   	It returns a sorted dictionary of errors
	"""
	info_dict = {}
	for line in file:
		match = re.search(r"ticky: ([\w ]*): (.*) \((.*)\)", line)
		#or match = re.search(r"ticky: (INFO|ERROR) (.*) \((.*)\)", line)
		if match:
			user = match.group(3)
			message_type = match.group(1)
			info_dict.setdefault(user, [0,0])
			if message_type == "INFO":
				info_dict[user][0] +=1
			elif message_type == "ERROR":
				info_dict[user][1] +=1
	return info_dict
file_path = "/home/jackdoe/GoogleTraining/gitinit/project.log"
#print(file_path)
with open(file_path, "r") as file:
	errors_sorted = sorted(errors_log(file).items(), key=operator.itemgetter(1), reverse=True)


with open(file_path, "r") as file:
	user_sorted = sorted(info_log(file).items())



with open("error_message.csv", "w", newline="") as error_report:
    writer = csv.writer(error_report)
    writer.writerow(["Error", "Count"])
    writer.writerows(errors_sorted)

with open("user_statistics.csv", "w", newline="") as user_report:
    writer = csv.writer(user_report)
    writer.writerow(["Username", "INFO", "ERROR"])
    writer.writerows(user_sorted)
