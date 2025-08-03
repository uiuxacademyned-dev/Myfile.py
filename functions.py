def sum(num1,num2):
    result = num1 + num2 
    print(f"Sum = {result}")
def diff(num1,num2):
    result = num1 - num2 
    print(f"difference ={result}")
def divide(num1,num2):
    result = num1 / num2
    print(f"Division = {result}")

num1 = int(input("Enter any number : "))
num2 = int(input("Enter another number : "))
op = input("Enter any number : ")

if op == "+":
    sum(num1,num2)
elif op == "-":
    diff(num1,num2)
elif op == "/":
    divide(num1.num2)

