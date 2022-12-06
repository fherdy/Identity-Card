import os
import smtplib


SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
PASSWORD = os.environ.get('PASSWORD')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.message = ""

    def send_email(self, name, email, message):
        self.name = name
        self.emal = email
        self.message = message

        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)

            try:
                connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=os.environ.get('REC_EMAIL'),
                                msg=f"Subject:You just got contacted by {self.name} \n\nName: {self.name} \nEmail: {self.emal} \nMessage: {self.message}")
                print("Successfully Sent!")
            except (smtplib.SMTPResponseException, smtplib.SMTPRecipientsRefused, smtplib.SMTPAuthenticationError):
                print(f"{self.receipient_email} is an invalid email")


