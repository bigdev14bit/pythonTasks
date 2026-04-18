print("*" * 66)
print("\t.M O R T G A G E  C A L C U L A T O R.")
print("*" * 66)

principal = int(input("\nENTER THE PRINCIPAL AMOUNT: "))
annual_rate = float(input("ENTER THE ANNUAL RATE: "))
duration = int(input("ENTER THE DURATION IN YEARS: "))

principal_one = annual_rate * (1 + annual_rate) ** duration
principal_two = (1 + annual_rate) ** duration
principal_three = principal_two - 1

mortgage = (principal_one / principal_two) + principal_three

print("\nYour monthly payment is: ", mortgage) 
