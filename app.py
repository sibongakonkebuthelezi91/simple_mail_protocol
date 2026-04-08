from flask import Flask, render_template, request
from validator import email_validate
from mail import send_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        email = request.form.get('email')
        valid_email = email_validate(email)
        if valid_email:
            send_email(email)
            return render_template("sent.html")
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
