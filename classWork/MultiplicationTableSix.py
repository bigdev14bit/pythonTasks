print("*" * 60)
print("** BIG DEV TABLE  **")
print("*" * 60)
print("Table\t\tMultiplication")


number = int(input("\nEnter Number: "))

for index in range(1, 11):
   result = number * index
   print("\n",number, " x ", index, "\t", " = ", result)
