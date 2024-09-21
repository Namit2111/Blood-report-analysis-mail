import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from langchain.tools import tool

@tool("Send an email")
def send_email(email,subject,body):
    """
    Send an email to the given recipient with the given subject and body
    @param email: The recipient's email address
    @param subject: The subject of the email
    @param body: The body of the email
    @return: A string indicating the email was sent
    """
    msg = EmailMessage()
    msg['Subject'] = f'from Medical bot'
    msg['From'] = "namitjain2111@gmail.com"
    msg['To'] = email
    msg.set_content(f'{body}')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("namitjain2111@gmail.com", 'tyanoszdfykftptq')
        smtp.send_message(msg)
    return "email sent"