# Certificate-Mailer
Certificate mailer is a Python script for automation of certificate generation and mailing.

## Usage
First change the sender to your email address and provide the 'APP SPECIFIC KEY' by gmail as password for the perfect working of the script.

You can change the template file by replacing the file with any other template image. 
(If doing so also change the name in the script)

Add the list (CSV Format only) and save it in the same folder as 'list.csv'
Make sure that the csv file contains columns with header "Name" and "Email"

Then: 
''''bash
python certificate-mailer.py
''''
###OR
''''bash
python3 certificate-mailer.py
''''

### References 
https://github.com/kunalgrover05/Certificate-sender