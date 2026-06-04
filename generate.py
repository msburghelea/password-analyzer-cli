import secrets
import string

def generate_password(length=12):
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    for _ in range(length - 4):
        password.append(secrets.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        ))

    secrets.SystemRandom().shuffle(password)
    result = "".join(password)
    print(f"Generated password: {result}")
    return result