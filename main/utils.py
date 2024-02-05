from django.conf import Settings
from django.core.mail import send_mail


def send_password_email(receiver, name, username, new_password):
    subject = f"Password Reset Request"
    message = ''
    from_email = 'encrane04@gmail.com'  # Sender's email
    recipient_list = [receiver]  # List of recipient emails
    html_message = f"""
    <div style="text-align:left; font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
    <h4>Dear {name},<h4><br><br>
    <p>You have requested a password reset. your new temporary password is <span style="color:blue;font-weight:600">{new_password}</span></p>
    <p>Just in case you forgot, Your username is <span style="color:blue;font-weight:600">{username}</span></p>
    <p>Kindly change your password after logging in.</p><br><br>
    <h4>Best Regards,<h4>
    <h4>Rigan Tech.</h4>
    </div>
    """
    fail_silently = False
    send_mail(subject, message, from_email, recipient_list, fail_silently, html_message=html_message)

def confirmation_email(receiver, name):
    subject = f"Rigan API Confirm Email"
    message = ''
    from_email = 'encrane04@gmail.com'  # Sender's email
    recipient_list = [receiver]  # List of recipient emails
    html_message = f"""
    <div style="text-align:center; font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
    <h4>Dear {name},<h4><br><br>
    <p>This is to confirm that you have registered an account on <b>Rigan API</b>.</p>
    <br><br>
    <p>We hope that you enjoy your experience with us.</p><br><br>
    <h4>Best Regards,<h4>
    <h4>Rigan Tech.</h4>
    </div>
    """
    fail_silently = False
    send_mail(subject, message, from_email, recipient_list, fail_silently, html_message=html_message)

def send_contact_message(email, name, subject, mssg):
    subject = f"{subject}"
    message = ''
    from_email = 'encrane04@gmail.com'  # Sender's email
    recipient_list = ['rigantech@gmail.com']  # List of recipient emails
    html_message = f"""
    <div style="text-align:left; font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
    <h4>Dear Rigan,<h4><br><br>
    <p>You have a new message alert from <a href="mailto:{email}" style="color:blue;font-weight:600">{name}: {email}</a></p>
    <p><span style="color:blue;font-weight:600">Message:</span> {mssg}</p><br><br>
    <h4>Best Regards,<h4>
    <h4>Rigan Tech.</h4>
    </div>
    """
    fail_silently = False
    send_mail(subject, message, from_email, recipient_list, fail_silently, html_message=html_message)

def reply_contact_message(receiver, name, subject, sender, mssg):
    subject = f"New Message Alert"
    message = ''
    from_email = 'encrane04@gmail.com'  # Sender's email
    recipient_list = ['rigantech@gmail.com']  # List of recipient emails
    html_message = f"""
    <div style="text-align:left; font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
    <h4>Dear {name},<h4><br><br>
    <p>You have a new message alert from <a href="mailto:{sender}" style="color:blue;font-weight:600">{name}: {sender}</a></p>
    <p><span style="color:blue;font-weight:600">Message:</span> {mssg}</p><br><br>
    <h4>Best Regards,<h4>
    <h4>Rigan Tech.</h4>
    </div>
    """
    fail_silently = False
    send_mail(subject, message, from_email, recipient_list, fail_silently, html_message=html_message)


