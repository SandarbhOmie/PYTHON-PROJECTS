# Sending e mail with pyhton
'''
1. to send emails with pyhton we need to manually go through steps of connecting to an email server of connecting to an email server,
confirming cinnection , setting protocols , logging in, and sending the message.

2. Fortunately the built-in "smtplib" library function in python makes these steps simple functions calls

3. Each major Email provider has their own SMTP (simple mail transfer protocol) server

for some examples:
    PROVIDER                             SMTP server domain name
      
    Gmail(will need App Password )        smtp.gmail.com
    Yahoo Mail                            smtp.mail.yahoo.com
    Outlook.com/Hotmail.com               smtp-mail.outlook.com

3. We will go over this process by gmail account
4.For gmail users , you need to generate an app password instead of your normal password.
5. This lets the gmail know that the python script attempting to access your account is authorized by you.


'''

import smtplib
# we are using gmail server
smtp_object = smtplib.SMTP('smtp.gmail.com',587)

# this will establish the connection.
smtp_object.ehlo()

smtp_object.starttls()

# we are goona create password
#input('What is your password: ')

import getpass # using this we will be able to hide tha password

# APP PASSWORD:  egcezqrabqbvltwh
# APP DEVICE NAME: Script Python

email = getpass.getpass(prompt="Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email,password)

from_address = email
to_address = "sandarbhparoha1203@gmail.com"
subject = input("enter the subject line: ")
message = input("enter the body message: ")
msg = 'Subject:'+subject+'\n'+message


smtp_object.sendmail((from_address), to_address, msg)

smtp_object.close()



