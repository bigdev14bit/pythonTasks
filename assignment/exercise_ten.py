digit = int(input("Enter Three Digit Number: "))

first_number = digit // 100
second_number = (digit % 100) // 10
third_number = digit % 10 

sum = first_number + second_number + third_number
average = sum / 3
product = first_number * second_number * third_number
print("The sum of ",first_number, second_number, third_number, "is ",sum)
