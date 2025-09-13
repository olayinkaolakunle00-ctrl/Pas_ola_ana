import re

def check_password(password):
    if len(password) < 8:
        return "Fail ❌: Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return "Fail ❌: Must include at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Fail ❌: Must include at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return "Fail ❌: Must include at least one digit."

    if not re.search(r"[^A-Za-z0-9]", password):
        return "Fail ❌: Must include at least one special character."

    return "Pass ✅: Strong password!"

# Get user input
password_input = input("Enter your password to check: ")

# Check and print result
print(check_password(password_input))
