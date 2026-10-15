num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = 0
difference = 0

def calculate_sum():
    sum = num1 + num2
    print(f"the sum is:  {sum}")

def calculate_diff():
    difference = num1 - num2
    print(f"the difference is:    {difference}")

calculate_sum()
calculate_diff()

