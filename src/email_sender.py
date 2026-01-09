import smtplib
import os

# SMTP Server | Domain Name, Port Number
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)

# Establish connection to SMTP Server
smtpObj.ehlo()

# Secures Ecrypted Data
smtpObj.starttls()

# Uses GitHub Secret Key to Login for Security
USERNAME = os.getenv("EMAIL_SECRET")
PASSWORD = os.getenv("PASS_SECRET")

# Recepient's Email Address
RECIPIENT_EMAIL = USERNAME

# Login to SMPT Server / With Authentication
try:
    smtpObj.login(USERNAME, PASSWORD)
    print("Logged In.")

except smtplib.SMTPAuthenticationError:
    print("Login failed. Check username/password.")
    exit(1)

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