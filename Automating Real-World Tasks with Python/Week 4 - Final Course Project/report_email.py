#!/usr/bin/env python3

import datetime
import os

from run import catalog_data
from reports import generate_report
from emails import generate_email, send_email

def pdf_body(input_for,desc_dir):
    # Generate a summary with two columns to output name and weight
    res = []
    wt = []
    for item in os.listdir(desc_dir):
      filename=os.path.join(desc_dir,item)
      with open(filename) as f:
        line=f.readlines()
        weight=line[1].strip('\n')
        name=line[0].strip('\n')
        print(name,weight)
        res.append('name: ' +name)
        wt.append('weight: ' +weight)
        print(res)
        print(wt)
    new_obj = ""  # initializing the object
    # Call values from two lists one by one.
    for i in range(len(res)):
        if res[i] and input_for == 'pdf':
            new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_obj

if __name__ == "__main__":
    user = os.getenv('USER')
    description_directory = '/home/{}/supplier-data/descriptions/'.format(user)  # The directory with all the files for the content.
    current_date = datetime.date.today().strftime("%B %d, %Y")  # Show date format as 'May 5, 2020'
    title = 'Processed Update on ' + str(current_date)  # Title for the PDF file that includes created date
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf',description_directory))  # call the report function from reports module to generate PDF report (processed.pdf) and save PDF in /tmp
    email_subject = 'Upload Completed - Online Fruit Store'
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # Email body text
    msg = generate_email("automation@example.com", "{}@example.com".format(user),
                         email_subject, email_body, "/tmp/processed.pdf")  # Generate email and attachment file to be sent
    send_email(msg)
