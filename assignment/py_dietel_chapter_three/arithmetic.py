integer = int(input("Enter Number: "))

largest = integer
smallest = integer

total_sum = integer
product = integer

for count in range(3):
   integer = int(input("Enter Number: "))

   total_sum += integer
   product *= integer
   
   if integer > largest:      
      largest = integer 
        
   if integer < smallest:
      smallest = integer

average = total_sum / 4



print("\nThe sum is: ",total_sum)
print("The product is: ",product)
print("The Average is: ",average)
print("The largest number is: ", largest)
print("The smallest number is: ", smallest)
