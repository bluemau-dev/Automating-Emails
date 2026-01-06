import smtplib

# SMTP Server | Domain Name, Port Number
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)

# Establish connection to SMTP Server
smtpObj.ehlo()

# Secures Ecrypted Data
smtpObj.starttls()

# Prompts User to enter credentials
USERNAME = input("Enter Username: ")
PASSWORD = input("Enter Password: ")

# Recepient's Email Address
RECIPIENT_EMAIL = USERNAME

# Login to SMPT Server / With Authentication
if(smtpObj.login(USERNAME, PASSWORD)):
    print("LOGGED IN.")

# Write the Email Message
mySubject = input("What is the subject? ")
myMessage = input("What is the message? ")
myName = input("Who is it from? ")

# Format and Sends Email
myEmail = f"""\
From: {USERNAME}
To: {RECIPIENT_EMAIL}
Subject: {mySubject}

{myMessage}\n

{myName}
"""
if(smtpObj.sendmail(USERNAME, RECIPIENT_EMAIL, myEmail)):
    print("Email Sent!")

# Logout
smtpObj.quit()
print("Session terminated. Have a good day!")