num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = 0
difference = 0
product = 0

def calculate_sum(num1, num2):
    sum = num1 + num2
    print(f"the sum is:  {sum}")

def calculate_diff(num1, num2):
    difference = num1 - num2
    print(f"the difference is:    {difference}")

def calculate_product(num1, num2):
    product = num1 * num2
    print(f"the product is:  {product}")

def calculate_quotient(num1, num2):
    quotient = num1 / num2
    print(f"the quotient is:  {quotient}")

calculate_sum(num1, num2)
calculate_diff(num1, num2)
calculate_product(num1, num2)
calculate_quotient(num1, num2)


