import smtplib
from email.message import EmailMessage

virus = True

email = EmailMessage()

email["from"] = "programmingdumdum@hotmail.com"
email["to"] = "bsbs66@hotmail.com"
email["subject"] = f"We have detected that you have a virus in your rheonix os after 3 scans. Please Install A Antivirus before five days. Now is. For safety"

email.set_content("html.substitute(version = 0.134, user='bsbs66@hotmail.com'), 'html'")

if virus:
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("programmingdumdum@hotmail.com", "domy6666")
        
        smtp.send_message(email)