# Modules
import smtplib
from email.mime.text import MIMEText

# Globals
TEXTFILE = "text.txt" # dummy file for MIMEText
SERVER = "localhost"

def newMessage(subject, message):
    global TEXTFILE
    global SERVER

    fp = open(TEXTFILE,"rb")
    msg = MIMEText(fp.read())
    s = smtplib.SMTP(SERVER)
    fp.close()
    
    msg["Subject"] = subject
    msg["From"] = "keystrokeforensics@gmail.com"
    msg["To"] = "3015237912@tmomail.net"

    s.sendmail(msg["From"], [msg["To"]], message)
    s.quit()
newMessage("hi","maya is a good girl")
