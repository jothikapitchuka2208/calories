import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('jothika0822@gmail.com','qhtdnhfbfiopimld')
    msg=EmailMessage()
    msg['From']='jothika0822@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

    







        
    





'''import smtplib
from smtplib import SMTP
from email.message import EmailMessage

def sendmail(to,otp):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('venkatadattu999@gmail.com','jwzsnvropfnuvhfz')
    msg=EmailMessage()
    msg['From']='venkatadattu999@'''
    
