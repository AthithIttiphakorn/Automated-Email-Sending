import smtplib
import getpass
import time

start_time = time.time()

#2 step verification must be turned on and an app password must be used instead of a normal password.

#create smtp object for a server
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

#run EHLO command to establish connection with server
smtp_object.ehlo()

#encryption
smtp_object.starttls()

appws = #your app password that was given to you. Do not share it to other people.

email = getpass.getpass("Sender Email: ")

#hide app password when typing in
#password = getpass.getpass('Enter password: ')
password = appws

print("hey guys")
#authenticate email account with Gmail's servers so emals can be sent.
print(smtp_object.login(email, password))

from_address = email
to_address = "2029ryu.r@shrewsbury.in.th"
subject = input("Enter the subject line: ")
message = input("Enter a message... ")

#function is going to accept the entire email as 1 block like this.
msg = "Subject: " + subject + '\n' + message
while True: #schedule email send
    elapsed_time = time.time() - start_time
    if elapsed_time >= 20:
        smtp_object.sendmail(from_address, to_address, msg)
        start_time = time.time()
