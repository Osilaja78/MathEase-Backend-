"""
* This script sends email.

"""

from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl, smtplib
from dotenv import load_dotenv
import os


load_dotenv()
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# This function sends email to users
# It recieves two parameters, the reciever's email 
# and the content to be sent
async def send_mail(email: str, content: str):

    email_sender = EMAIL_SENDER
    email_password = EMAIL_PASSWORD
    email_reciever = email

    subject = 'MathEase Account.'

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject

    em.attach(MIMEText(content, "html"))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        'smtp.gmail.com',
        465,
        context=context
    ) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())