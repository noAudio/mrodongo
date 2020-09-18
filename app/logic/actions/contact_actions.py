import smtplib
from email.message import EmailMessage
from typing import Any
from email_config import email_attr, usrnm, pwd

def create_email(name: str, contact: str, message: str) -> Any:
    email = EmailMessage()
    email['from'] = email_attr['sender']
    email['to'] = email_attr['receiver']
    email['subject'] = email_attr['subject']
    email.set_content(f'Message from: {name} \n\nContact: {contact} \n\nMessage:\n{message}')
    print(email)
    return email

def send_email(email: Any) -> None:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(usrnm, pwd)
        smtp.send_message(email)