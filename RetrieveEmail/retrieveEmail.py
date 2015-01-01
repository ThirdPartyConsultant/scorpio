#!/usr/bin/python
import imaplib
import urllib2
import os
#import base64
from subprocess import call
from datetime import datetime



# connecting to mail server via IMAP$...
def connect_to_mail_server():

    log('=============== ' + time + ' ====================')
    log('Connecting to mail server...')
    try:
        MailConnection = imaplib.IMAP4_SSL('imap.gmail.com','993')
        MailConnection.login('safesync@kenyang.net', 'xxxxxxxx')
        MailConnection.select('Inbox')
        return MailConnection
    except:
        log('Fail to connect to mail server')
        return None

def search_email():
    # searching email
    log('Searching email on ' + date + ' ...')
    typ, data = MailConnection.search(None, '(SUBJECT "ttid" FROM "trend.com.tw" UNSEEN)')

    if (typ == 'OK'):
        return data
    else:
        return None

def read_emails(emails):
    bHaveP0 = False
    szData = emails[0].split()
    log('There are ' + str(len(szData)) + ' unread emails.')

    for num in szData:

        # mark the mail as seen
        MailConnection.store(num, '+FLAGS', '\SEEN')

        if (not bHaveP0):
            log('Reading mail ' +num+'...')
            # get email content
            typ, data = MailConnection.fetch(num, '(BODY.PEEK[TEXT])')

            for response_part in data:
                if isinstance(response_part, tuple):
                    strBody = response_part[1]
                    #strBody = base64.decodestring(strBody)

                    # Parsing data
                    index = strBody.find('Priority: ')
                    strPriority = ''
                    if (index != -1):
                        strPriority = strBody[index+10:index+12]
                    log('Priority : ' +strPriority)

                    if (strPriority=='P0'):
                        bHaveP0 = True

    return bHaveP0


def close_connection():
    MailConnection.close()
    MailConnection.logout()


def log(strMsg):
    print strMsg
    strDirectory = '/var/log/monitorTT'
    if not os.path.exists(strDirectory):
        os.makedirs(strDirectory)

    strCmd= "echo {0} >> {1}/{2}".format(strMsg, strDirectory, logfilename)
    os.system(strCmd)

# init variable
date = datetime.now()
logfilename = date.strftime('%Y%m%d')
time = date.strftime('%H:%M')
date = date.strftime('%d-%b-%Y')

# init connection
MailConnection = connect_to_mail_server()

if (MailConnection is not None):
    emails = search_email() 

    if (emails is not None):
        bHaveP0 = read_emails(emails)
        if (bHaveP0):
            log('There are critical cases.')
            urllib2.urlopen('http://10.1.193.195/command/turn_on_rely').read()
        else:
            log('There are no any critical cases.')

    close_connection()

