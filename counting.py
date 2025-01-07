# Initialize the variable `current_number` to 0
current_number = 0

# Start a while loop that runs as long as `current_number` is less than 10
while current_number < 10:
    # Increment the value of `current_number` by 1
    current_number += 1
    
    # Check if `current_number` is even (divisible by 2)
    if current_number % 2 == 0:
        # If the number is even, skip the rest of the loop using `continue`
        continue
    
    # Print the current number if it is odd
    print(current_number)
