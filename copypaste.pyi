import smtplib
from email.message import EmailMessage

email = EmailMessage()

email["from"] = "Render Intelligente"
email["to"] = "bsbs66@hotmail.com"
email["subject"] = "Update Finished"

email.set_content("We are Intelligente")

with smtplib.SMTP(host="smtp.outlook.com", port=993) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("programmingdumdum@hotmail.com", "program1234")