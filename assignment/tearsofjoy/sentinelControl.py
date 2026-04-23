total_sum = 0

while True:
    user_input = int(input("Enter number, or 0 to quit: "))

    if user_input == 0:
        break;
    total_sum += user_input
    print("The current sum is: ", total_sum)
print("The total sum is: ", total_sum)
