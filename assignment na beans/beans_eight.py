principal = int(input("Enter Principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter Time: "))

simple_interest = (principal * rate * time)/100
print("Your simple interest is: ", simple_interest)

amount = principal + simple_interest
print("Amount is: ", amount)
