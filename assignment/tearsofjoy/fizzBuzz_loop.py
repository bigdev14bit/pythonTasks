for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print(number,"fizzBuzz", end=" ")
    elif number % 3 == 0:
        print(number, "fizz", end=" ")
    elif number % 5 == 0:
        print(number, "Buzz", end=" ")
print()
