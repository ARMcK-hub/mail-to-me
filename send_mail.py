'''
Mail-To-Me - Send Mail
Author: Andrew McKinney
Creation Date: 8/16/2020
'''


# importing dependencies
import smtplib
from email.mime.text import MIMEText
from importz import p, u

def send_mail(to_mail, form_data):
    port = 587
    smtp_server = 'smtp.gmail.com'
    uni = 'mailtome'
    pen = 'mail2me'
    
    sender_email = form_data['sender_email']
    to_email = to_mail

    # generating email message
    message = f'''

    <h3><center>The following message was sent via Mail-To-Me:</center></h3>
    <br>
    <p>From: {sender_email}</p>
    <p>To: {to_email}</p>
    
    '''
    
    # looping through form submissions
    for field in form_data:
        field = field
        value = form_data[field]
        field_msg = f"<p>{field}: {value}</p>"
        if field != "sender_email":
            message = message + field_msg

    # including Mail-To-Me standard email footer
    end_msg = '''<br><br><br>
    <p><i>This message was automatically generated by the Mail-To-Me application. Please do not reply to this email. 
    <br>
    If you have not set up a submission form to Mail-To-Me or would like to stop future emails, please forward this message to: armck@ymail.com.
    <br>
    For more information on Mail-To-Me visit: https://mailtome.herokuapp.com/</i></p>'''
    
    message = message + end_msg

    corn = p
    guin = u

    # forming message structure
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'A Message from Mail-To-Me'
    msg['From'] = sender_email
    msg['To'] = to_email

    unicorn = uni + corn
    penguin = pen + guin

    # Sending Email vaia smtp
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.login(unicorn, penguin)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()