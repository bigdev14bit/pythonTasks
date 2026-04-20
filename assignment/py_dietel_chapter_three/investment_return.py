investment = float(input("Enter investment amount: "))

percentage = 0.07
amount = investment

print("\nYEAR"," ","AMOUNT ON DEPOSIT")
for year in range(1, 31):
   # Logic: New amount = current amount + (current amount * 0.07)
   amount = amount + (amount * percentage)
   
   print(year," ", "\t",amount)   
