import pandas as pd 
import numpy as np 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def names(name_list):
    names=name_list["Name"]
    return names

def emails(name_list):
    emails=name_list["Email"]
    return emails
    

def certificate(name):
    img=Image.open('template.jpg')
    draw=ImageDraw.Draw(img)
    font_selecter=ImageFont.truetype("font.TTF",size=30)
    draw.text((265,188),name,(0,0,0),font=font_selecter)
    #draw.text((x,y),text,(r,g,b),font=font)
    img.save('certificate '+name+'.pdf',"PDF",resolution=100.0)
    return 'certificate '+name+'.pdf'

def mailer(email,certi):
    sender=""
    password=""

    #setting up the email header
    msg=MIMEMultipart()
    msg['Subject'] = 'EDC certificate'
    msg['From'] = sender
    msg['Reply-to'] = sender
    msg['To']=email

    part=MIMEText("Please find attached the EDC certificate. \n Greetings from EDC-NSSCE")
    msg.attach(part)

    attachment=MIMEApplication(open(certi,"rb").read())
    attachment.add_header('Content-Disposition', 'attachment', filename = os.path.basename(certi))
    msg.attach(attachment)

    mailer=smtplib.SMTP('smtp.gmail.com:587')
    try:
        mailer.starttls()
        mailer.login(username,password)
        mailer.sendmail(sender,email,msg.as_string())
        mailer.close()
        print('Certificate send successfully')
    except:
        print('Could not login. Check the credentials and try again')
        mailer.close()


if __name__ == "__main__":
    name_list=pd.read_csv('list.csv')
    names=names(name_list)
    email=emails(name_list)
    for i in range(len(names)):
        name=names[i]
        certi=certificate(name)
        print('Certificate of '+names[i]+' ready!!!!')
        print('Sending certificate to '+email[i]+' now!!!!')
        time.sleep(1)
        mailid=email[i]
        mailer(mailid,certi)
    print('Certificate send. Closing application now....')
    time.sleep(3)
    