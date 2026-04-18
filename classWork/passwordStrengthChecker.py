"""
1. collect password from user
2. check the length
3. classify it into this category: very weak, weak, strong, very strong
"""
password = input("Enter Password: ")

password_length = len(password)

if password_length < 6:
    print("Your password contain ", password_length, " digit, VERY WEAK")
elif password_length > 6 and password_length < 8:
    print("Your password contain ", password_length, " digit, WEAK!!! *(<,>)*")
elif password_length > 8 and password_length < 12:
    print("Your password contain ", password_length, " digit, STRONG")
elif password_length > 12 and password_length < 16:
    print("Your password contain ", password_length, " digit, VERY STRONG")
else:
    print("Password mismatch")
