
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
  result = num1 + num2
elif choice == '2':
  result = num1 - num2
elif choice == '3':
  result = num1 * num2
elif choice == '4':
  result = num1 / num2
else:
  print("Invalid input")

print("Result:", result)
