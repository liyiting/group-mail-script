#!/usr/bin/env python

__author__ = "Yiting Li"
__email__ = "yl2919@columbia.edu"
__description__ = "Send email to a list of people by parsing the csv file"

import csv
import sys
import smtplib
from email.mime.text import MIMEText
from optparse import OptionParser


DELIMITER = ','
QUOTECHAR = '"'
TITLE_FIX = ""

SMTP_SERVER = "smtp.gmail.com:587"
FROM_EMAIL = "***"
FROM_PASSWORD = "***"
TO_DOMAIN = "@columbia.edu"
CC_EMAIL = "***"
SUBJECT = "[S1004] Homework Grade Report"
CONTENT_PREFIX = "S1004 homework grade report:\n"
CONTENT_POSTFIX = "\nRegards,\nYiting"


class ListMail():

    title = []
    credit = []
    report = {}

    option_dic = {
        'title': title.append,
        'credit': credit.append
    }

    def __init__(self, *args, **kwargs):
        self.send = kwargs.get('send', False)
        self.no_confirm = kwargs.get('no_confirm', False)
        self.server = smtplib.SMTP(SMTP_SERVER)
        self.server.starttls()
        self.server.login(FROM_EMAIL, FROM_PASSWORD)

    def execute(self, filename):
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTECHAR)
            for line in reader:
                if line[0] in self.option_dic:
                    self.option_dic[line[0]](line)
                else:
                    self.render_line(line)
        print self.report

    def render_line(self, line):
        content = "Hi, " + line[0] + ":\n\n" + CONTENT_PREFIX
        target = line[0] + TO_DOMAIN
        for i in range(1, len(line)):
            for t in range(len(self.title)):
                if self.title[t][i]:
                    if t != (len(self.title)-1):
                        content += '\n' + TITLE_FIX + self.title[t][i] + TITLE_FIX + '\n'
                    else:
                        content += self.title[t][i] + ": "
            if line[i]:
                content += line[i]
            else:
                content += "None"
            for c in range(len(self.credit)):
                if self.credit[c][i]:
                    content += '/' + self.credit[c][i]
            content += '\n'
        content += CONTENT_POSTFIX
        if self.send is True:
            self.send_mail(target=target, content=content)
        else:
            print content

    def send_mail(self, target, title=None, content=None):
        msg = MIMEText(content)
        msg['From'] = FROM_EMAIL
        msg['To'] = target
        msg["Cc"] = CC_EMAIL
        msg['Subject'] = SUBJECT
        if self.no_confirm is False:
            print msg.as_string()
            var = raw_input("Send mail? (yes/n): ")
            if var == 'yes':
                self.server.sendmail(FROM_EMAIL, [target] + [CC_EMAIL], msg.as_string())
            else:
                self.report[target] = False

    def __del__(self):
        self.server.quit()


def main():
    usage = "usage: listmail.py file [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-s", "--send", action="store_true", default=False,
                      help="send email to list, if not set, just print e-mail content")
    parser.add_option("-n", "--no-confirm", action="store_true", default=False,
                      help="no ask for comfirmation of the content of each e-mail before send")
    (options, args) = parser.parse_args()
    print options
    if not args:
        parser.print_help()
        sys.exit(1)
    obj = ListMail(send=options.send, no_confirm=options.no_confirm)
    obj.execute(args[0])


if __name__ == "__main__":
    main()
