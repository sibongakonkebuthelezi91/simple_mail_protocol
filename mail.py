import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_env():
    has_env = os.path.exists(".env")
    if has_env:
        email_user = os.getenv("email_user")
        email_pass = os.getenv("email_password")
        return email_user, email_pass
    else:
        return (0, 0)


def read_html():
    with open("templates/genai.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html


def send_email(email: str) -> bool:
    html = read_html()
    message = MIMEText(html, "html")
    email_user = ""
    email_pass = ""
    has_env = check_env()
    if not has_env:
        return False
    email_user, email_pass = has_env
    msg = MIMEMultipart()
    try:
        msg['subject'] = "COURSES TO STUDY"
        msg['from'] = email_user
        msg['to'] = email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # server.ehlo()
        # server.starttls()
        msg.attach(message)
        server.login(email_user, email_pass)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Email error: {e}")
        return False
    else:
        return True


if __name__ == "__main__":
    print(send_email("dumasiyanda627@gmail.com"))
    # print(check_env())