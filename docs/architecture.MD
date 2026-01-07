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

# ScheduleEmail.py

* Time-Module:
- time.time() method returns the seconds since the epoch time as a floating-point number.
- time.gmtime(x) method returns a tuple of epoch time. The parameter 'x' can be 0, which returns the starting point of time: 'time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=1, tm_sec=40, tm_wday=3, tm_yday=1, tm_isdst=0)'
or can be the current time by setting 'x' as the seconds since the epoch time.

//EXAMPLE CODE//
x = time.time() //x = 1767751391.924533
print(time.gmtime(x)) //PRINTS: time.struct_time(tm_year=2026, tm_mon=1, tm_mday=7, tm_hour=2, tm_min=3, tm_sec=11, tm_wday=2, tm_yday=7, tm_isdst=0)

Notes:
- What is Epoch? It is the point where time starts and is platform-dependant(meaning only works on Operating Systems like Windows, MacOS, or Linux). The starting point of time is January 1, 1970, 00:00:00 UTC, acting as a universtal time standard.
- Greenwich Mean Time (GMW) is the point of reference for that global time. 