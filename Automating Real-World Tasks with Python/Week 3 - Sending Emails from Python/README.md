## Module 3 Project

### Qwiklabs Assessment: Automatically Generate a PDF and send it by Email

**Introduction**

You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable.

**What you'll do**

- Write a script that summarizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email 

---

### Solution

This assessment is split into 2 parts. The first past is to generate a PDF report and send it by email with *exmaple.py* script. Then check you have received the PDF report as an attachment using roundcube mail program. 

The second part is to extract the data from car_sales.json and generate a car sales pdf report using *cars.py* script. Then, send it by email. Finally, you can check using roundcube email program to see if you have received the email with PDF attached.  

You will find all the working Python3 scripts in /scripts directory on Github. All generated PDF reports are saved to /tmp but on the Qwiklab VM, the temp dir is <root>/tmp 
