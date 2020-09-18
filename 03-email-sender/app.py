import smtplib
from decouple import config


SENDER_EMAIL = config('EMAIL')
SENDER_PASSWORD = config('PASSWORD')


to = input("Enter the email of recipient\n")
content = input('Enter the content for the email:\n')


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, to, content)
    server.close()


send_email(to, content)