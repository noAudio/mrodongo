import smtplib
from email.message import EmailMessage

sender = 'Mr Odongo Contact Form'
receiver = 'samieodd@gmail.com'
subject = 'Contact Form Message'

_usrnm = 'botmrodongo@gmail.com'
_pwd = 'MrOdongoEmailBot'

def create_email(name, contact, message):
    email = EmailMessage()
    email['from'] = sender
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(f'Message from: {name} \n\nContact: {contact} \n\nMessage:\n{message}')
    return email

def send_email(email):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(_usrnm, _pwd)
        smtp.send_message(email)