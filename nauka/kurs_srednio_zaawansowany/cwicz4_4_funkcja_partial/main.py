'''
import smtplib


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = """From: {}
Subject:{}

{}
""".format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print("mail sent")
        return True
    except:
        print("error sending email")
        return False


mailFrom = "Your automation system"
mailTo = ["naukapythona1313@gmail.com"]
mailSubject = "Processing finished successfully"
mailBody = """Hello

This mail confirms that processing has finished without problems,

Have a nice day!"""

user = "naukapythona1313@gmail.com"
password = "super_tajne_haslo"

SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
'''

# ------
'''
import smtplib
import functools


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = """From: {}           
Subject:{}

{}
""".format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print("mail sent")
        return True
    except:
        print("error sending email")
        return False


mailFrom = "Your automation system"
mailTo = ["naukapythona1313@gmail.com"]
mailSubject = "Processing finished successfully"
mailBody = """Hello!

This mail confirms that processing has finished without problems,

Have a nice day!"""

user = "naukapythona1313@gmail.com"
password = "super_tajne_haslo"

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password)       

SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)     
'''
#SendInfoEmail(user, password, mailFrom, mailTo,mailSubject, mailBody)


# -----

import smtplib
import functools


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = """From: {}           
Subject:{}

{}
""".format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print("mail sent")
        return True
    except:
        print("error sending email")
        return False


mailFrom = "Your automation system"
mailTo = ["naukapythona1313@gmail.com"]
mailSubject = "Processing finished successfully"
mailBody = """Hello!

This mail confirms that processing has finished without problems,

Have a nice day!"""

user = "naukapythona1313@gmail.com"
password = "super_tajne_haslo"

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password, mailSubject="Execution alert")

SendInfoEmailFromGmail(mailFrom=mailFrom, mailTo=mailTo, mailBody=mailBody)

# SendInfoEmail(user, password, mailFrom, mailTo,mailSubject, mailBody)

