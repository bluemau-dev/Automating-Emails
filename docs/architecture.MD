# Documentation of Project Files

# Automation / Email.py

Sending Email using SMPT Library
1. Connect to SMTP Server: 'smtplib.SMPT('DOMAIN NAME', PORT #)'
2. Establish connection to SMTP Server: 'OBJECT.ehlo()'
3. Start TLS Encryption: 'OBJECT.starttls()'
4. Logging in to SMTP Server: 'OBJECT.login(USERNAME, PASSWORD)'
5. Sending the email: 'OBJECT.sendmail('USERNAME', 'RECEPIENT_EMAIL', 'Subject: XXX.\n Dear Bob, this is an email. Sincerely, John')

Notes:
- USERNAME: my_email_address@gmail.com
- PASSWORD: my_password
- Sending the email, it starts with a Subject which is then separated by a '\n' new line character. From there write the body of the email.
- TLS stands for Transport Layer Security: Meaning it secures communication on the internet by encrypting data between sender and receiver.
- f-strings: Formatted String Literals to help incorate formatting and interpolation.
- Interpolation: Meaning subsituting placeholders in a string with values like (Primitive or Non-Primitive Data Types)

Connecting to Domain Name: 
Depending on what you use, 