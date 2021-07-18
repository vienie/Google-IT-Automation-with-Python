#!/usr/bin/env python3

import sys
import re
import operator
import csv

# Variable to count number of entries for each user
per_user = {} 
# variable for number of different error messages
errors = {}

# * Read file and create dictionary
with open('syslog.log') as file:

    for line in file.readlines():
        # regex search
        # Sample Line of log file
        # Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (username)"
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        # Populates error dict with ERROR messages from log file
        if error_msg not in errors.keys():
            errors[error_msg] = 1
        else:
            errors[error_msg] += 1
        # Populates per_user dict with users and default values
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
        # Populates per_user dict with users logs entry
        if code == 'INFO':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]["INFO"] += 1
        elif code == 'ERROR':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]['ERROR'] += 1


# Sorted by value (most common to least common)
errors_list = sorted(errors.items(), key=operator.itemgetter(0))

# Sorted by username
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

file.close()
# Insert at the beginning of the list
errors_list.insert(0, ('Error', 'Count'))

# Create user_statistics.csv
with open('user_statistics.csv', 'w', newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' +
                       str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

# Create error_message.csv
with open('error_message.csv', 'w', newline='') as error_csv:
    for key, value in errors_list:
        error_csv.write(str(key) + ' ' + str(value)+'\n')

