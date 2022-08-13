# receiving emails in python
'''
1. To view received emails in python we can use built in "imaplib" and email lobraries in python.
2. the "imaplib" library has a special syntax for searching your inbox.
3. KEYWORD and their defination ss is saved.

'''
import imaplib
M = imaplib.IMAP4_SSL("imap.gmail.com")
import getpass
email = getpass.getpass("email: ")
password = getpass.getpass("Password: ") # App password

M.login(email,password)
print(M.list())
M.select('inbox')

# to find a email of any type we can use.
# remember this will output numbers related to that of findings if no numbers are printed then it means it was not there.
typ, data = M.search(None,'BEFORE 23-Jul-2022')  # to get the emails sent before this date.
typ, data = M.search(None,'FROM user@example.com') # to find the email send from this user.and
typ, data = M.search(None,'SUBJECT "NEW TEST PYTHON"')  # search by subject


