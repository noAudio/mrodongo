import smtplib
from email.message import EmailMessage
from email_config import sender, receiver, subject, usrnm, pwd

def create_email(name, contact, message):
    email = EmailMessage()
    email['from'] = sender
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(f'Message from: {name} \n\nContact: {contact} \n\nMessage:\n{message}')
    print(email)
    return email

def send_email(email):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(usrnm, pwd)
        smtp.send_message(email)