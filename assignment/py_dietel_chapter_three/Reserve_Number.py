user_input = int(input("Enter a 5 digit number: "))

while user_input > 0:
   extract = user_input % 10
   print(extract)
   reduuce = int(user_input / 10)
   user_input = reduuce
