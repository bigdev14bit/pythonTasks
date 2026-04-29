def valid_email(email):
    if len(email) > 8:
        return True
    if "@" not in email:
        return False
    if email.startswith("@"):
        return False
    if email.endswith("@"):
        return False
    return True

print(valid_email("devbig14@gmail.com"))
print(valid_email("@testingmycode"))
