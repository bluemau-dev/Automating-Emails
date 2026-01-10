import smtplib
import os
import time
from email.message import EmailMessage
from src.generate_quotes import load_quote

def sendEmail():
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

    # Get Quote and Author
    quote, author = load_quote()

    # Write the Email Message
    mySubject = "Have a great " + time.strftime("%A") + " Bluemau Developer!"
    
    # Create Email Message
    msg = EmailMessage()

    msg['Subject'] = f"Have a great {time.strftime('%A')} Bluemau Developer!"
    msg['From'] = f"Bluemau Quotes <{USERNAME}>"
    msg['To'] = RECIPIENT_EMAIL

    # Format and Sends Email
    msg.set_content(f"""\
    {quote}

    {author}
    """)

    # Uses the SMTP Object to Send Email from the Formatted Message
    smtpObj.send_message(msg)
    print("Email Sent Successfully!")

    # Logout
    smtpObj.quit()
    print("Session terminated. Have a good day!")