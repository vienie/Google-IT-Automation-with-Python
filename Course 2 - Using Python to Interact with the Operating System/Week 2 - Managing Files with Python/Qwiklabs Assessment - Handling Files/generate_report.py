#!/usr/bin/env python3

import csv

# Convert employee data to dictionary

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list

employee_list = read_employees('/home/student-00-2237e86289ec/data/employees.csv') # to find the dir path, in this current directory (ie, ~/script), type: pwd in your terminal. This will print out the path on your terminal screen. 
print(employee_list)

# Now save the file and execute it to complete the first part ('Convert employee data to dictionary')
# If successful, carry on to the next stage, below.

# Process employee data

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])

  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

dictionary = process_data(employee_list)
print(dictionary)

# At this point, save this file and execute it to complete this stage ('Process employee data')
# If successful, carry on to the next stage, below

# Generate a reoprt

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
write_report(dictionary, '/home/student-00-2237e86289ec/data/report.txt')