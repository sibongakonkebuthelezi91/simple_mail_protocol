from flask import Flask, render_template, request
from validator import email_validate
from mail import send_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        email = request.form.get('email')
        valid_email_and_sent = email_validate(email) and send_email(email) 
        if valid_email_and_sent:
            return render_template("sent.html")
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
