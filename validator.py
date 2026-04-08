from email_validator import validate_email


def email_validate(email: str):
    try:
        validate_email(email)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    print(email_validate("destiny@gmail.com"))
