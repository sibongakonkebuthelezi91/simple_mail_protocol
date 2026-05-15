from dotenv import load_dotenv
import os
import requests


has_env = None
if os.path.exists(".env"):
    try:
        has_env = load_dotenv()
    except ImportError:
        print("dotenv module not found. Make sure to install it using 'pip install python-dotenv' if you want to use environment variables.")


def check_env():
    if has_env:
        email_user = os.getenv("email_user")
        email_pass = os.getenv("email_password") 
        return str(email_user), str(email_pass)
    else:
        return None


def read_html():
    with open("templates/genai.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html


def send_email(email: str) -> bool:
    html = read_html()
    email_user = ""
    email_pass = ""
    has_env = check_env()
    if not has_env:
        return False
    email_user, email_pass = has_env
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": str(email_pass),         
        "content-type": "application/json"
    }
    
    data = {
        "sender": {"email": email_user},
        "to": [{"email": email}],
        "subject": "COURSES TO STUDY",
        "htmlContent": html
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in [200, 201, 202]:
            print("Email sent successfully!")
            return True
        else:
            print(f"Brevo Error: {response.text}")
            return False
    except Exception as e:
        print(f"Connection Error: {e}")
        return False
   


if __name__ == "__main__":
    print(send_email("dumasiyanda627@gmail.com"))
    # print(check_env())