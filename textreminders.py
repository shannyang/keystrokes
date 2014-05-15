# textreminders.py
# Script to text email reminders to 

# Modules
import smtplib
import time
import shelve
from email.mime.text import MIMEText

# Server stuff
# Security what security
SERVER = "smtp.gmail.com"
PORT = 587
USER = "keystrokeforensics@gmail.com"
PASS = "youwillneverguessthis" # egregious

# Recipient data
RECIPIENTS = "recipients"

def sendMessage(subject,message):
    global RECIPIENTS
    recipients = shelve.open(RECIPIENTS)
    for recipient in recipients:
        newMessage(subject,message,recipients[recipient])
    recipients.close()
            
def newMessage(subject, message, recipient):
    global SERVER, PORT, USER, PASS

    msg = MIMEText(message)
    s = smtplib.SMTP(SERVER,PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(USER,PASS)

    msg["Subject"] = subject
    msg["From"] = USER
    msg["To"] = recipient
    
    s.sendmail(USER, [msg["To"]], msg.as_string())
    s.quit()
