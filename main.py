#If the number is divisible by 20, it provides an output "twist."
number = int(input("Enter number:"))
if number % 20 ==0:
    print("twist")

#If the number is divisible by 15, it will pass (no output)
num = int(input("Enter number:"))
if number %15 ==0:
    pass

#If the number is divisible by 5, it will give an output “fizz.”
x= int(input("Enter num:"))
if x %3 ==0:
    print("buzz")