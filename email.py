import smtplib
from email.message import EmailMessage

def email_alert(to, subject, body):

    msg = EmailMessage()
    msg.set_content(body)

    email_addr = 'jkristi4n@gmail.com'
    login_password = 'app_pass'
    msg['Subject'] = subject
    msg['From'] = 'jkristi4n@gmail.com'
    msg['To'] = to

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(email_addr, login_password)
    s.send_message(msg)
    s.quit()

if __name__ == '__main__':
    email_alert('to_someone@somewhere.com', 'test', 'server address')
