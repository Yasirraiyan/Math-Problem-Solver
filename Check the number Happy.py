# Function to check if a number is a happy number
def is_happy_number(num):
    seen_numbers = set()  # Set to track numbers we've seen

    while num != 1:
        if num in seen_numbers:  # If we see a number we've seen before, it means we're in a loop
            return False
        seen_numbers.add(num)  # Add the current number to the set
        
        # Calculate the sum of the squares of the digits
        num = sum(int(digit) ** 2 for digit in str(num))
    
    return True  # If we reach 1, it's a happy number

# Input from the user
number = int(input("Enter a number: "))

# Check if it's a happy number
if is_happy_number(number):
    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")
