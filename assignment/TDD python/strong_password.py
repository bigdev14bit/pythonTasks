def strong_password(password):
    if len(password) > 8:
        return True
    else:
        return False

print(strong_password("Linux@3000"))
print(strong_password("adeola"))
