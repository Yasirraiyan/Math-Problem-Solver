# Function to check if a number is a Harshad number
def is_harshad_number(num):
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % sum_of_digits == 0

# Input from the user
number = int(input("Enter a number: "))

# Check if it's a Harshad number
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
