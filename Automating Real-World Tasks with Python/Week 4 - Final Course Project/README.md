## Week 4 - Final Course Project 

### Qwiklabs Assessment: Automate updating catalog information


**Introduction**

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

**What you'll do**

- Write a script that summarizes and processes sales data into different categories
- Convert images to smaller JPEG and text file for description
- Upload converted content via a web service that is already running using Django (Python framework)
- All content should be displayed as HTML page on web browser
- Generate a PDF using Python
- Automatically send a PDF by email
- Write a script to check the health status of the system
- Test health check script is working

---

### Solution

Python script named **changeImage.py** created to process the supplier images. Images are saved to ~/supplier-data/images (with a JPEG extension).

**supplier_image_upload.py** script is created to upload jpeg images from the ~/supplier-data/images directory and uploads them to the web server fruit catalog (ie, /mediaimages/).

Django REST framework is already installed and running on the web server. Created a Python script that will automatically POST the fruit images and their respective description in JSON format. **run.py** scritp will process the text filesfrom ~/supplier-data/descriptions directory and upload (as JSON format) to web service. Check the website (http://[linux-instance-IP-Address]/) to make sure the HTML webpage is displaying the uploaded content.

Created **reports.py** script to generate PDF report and **report_email.py** to process supplier fruit description data from ~/supplier-data/descriptions directory. Created **emails.py** to send the email once PDF is generated. Make sure to login to Roundcube webmail program to check email has been received. 

Created **health_check.py** script that can be used to run in the background to monitor some of your system statistics: CPU usage, disk space, available memory and name resolution. When a problem is detected, it will send a notification (ie, email) to alert you. The detected problems are:
- Report an error if CPU usage is over 80%
- Report an error if available disk space is lower than 20%
- Report an error if available memory is less than 500MB
- Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

