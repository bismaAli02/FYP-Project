import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from Backend.config import db
from Backend.Logs.logger import Logger
import logging


class emailServices:
    instance = None

    def getInstance():
        if emailServices.instance is None:
            emailServices()
        return emailServices.instance

    def __init__(self):
        if emailServices.instance is not None:
            raise Exception(
                "This class is a Singleton! Use getInstance() method to get the instance")
        else:
            emailServices.instance = self
            s = smtplib.SMTP(
                host=db.configEmail["host"], port=db.configEmail["port"])
            s.starttls()
            self.sender = s

    def sendEmailMessage(self, MY_ADDRESS, password, recieverEmail, name):
        try:
            self.sender.login(MY_ADDRESS, password)
            message_template = self.read_template(
                'Backend\BL\Services\msg_template.txt')
            msg = MIMEMultipart()       # create a message
            # add in the actual person name to the message template
            message = message_template.substitute(PERSON_NAME=name)
            print(message)
            msg['From'] = MY_ADDRESS
            msg['To'] = recieverEmail
            msg['Subject'] = "Your request has been approved!"
            # add in the message body
            msg.attach(MIMEText(message, 'plain'))
            # send the message via the server set up earlier.
            self.sender.send_message(msg)

        except Exception as e:
            msg = "Exception in Email Service's Send Email Message Function " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
        finally:
            del msg

    def read_template(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as template_file:
                template_file_content = template_file.read()
            return Template(template_file_content)
        except Exception as e:
            msg = "Exception in Email Service's Read Template Function " + \
                str(e)
            Logger.CreateLog(
                logging.ERROR, msg)
            pass
