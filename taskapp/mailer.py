from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from getpass import getpass


def send_email(subject, body, destinatario):
    m_from = ""
    m_pwd = ""
    s = smtplib.SMTP(host='smtp.office365.com',
                     port=587)
    s.starttls()
    s.login(m_from, m_pwd)
    msg = MIMEMultipart()
    msg['From'] = m_from
    msg['To'] = destinatario
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()
