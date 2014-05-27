# textreminders.py
# Script to text email reminders, used with cron

# Modules
import smtplib
import time
from email.mime.text import MIMEText

# Server stuff
# Security what security
SERVER = "smtp.gmail.com"
PORT = 587
USER = "keystrokeforensics@gmail.com"
PASS = "youwillneverguessthis" # egregious

def newMessage(subject, message, recipient):

    # Login
    global SERVER, PORT, USER, PASS
    s = smtplib.SMTP(SERVER,PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(USER,PASS)

    # Creates message
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = USER
    msg["To"] = recipient

    # Send
    s.sendmail(USER, [msg["To"]], msg.as_string())
    s.quit()

newMessage("Yo!",
           "Sent at %d:%d" % (time.localtime().tm_hour, time.localtime().tm_min),
           "3015237912@tmomail.net")
