while True:  # Keep asking until valid input is provided
    try:
        # Prompt the user to enter a number and convert the input to an integer

        number = int(input("Enter a number: "))

# Check if the number is divisible by 10 using the modulus operator (%)
        if number % 10 == 0:
    # If the remainder is 0, print a message indicating the number is a multiple of 10
            print(f"The number {number} is a multiple of 10.")
        else:
    # If the remainder is not 0, print a message indicating the number is not a multiple of 10
         print(f"The number {number} isn't a multiple of 10.")

        break  # Exit the loop if valid input is provided
    
    except ValueError:
        # If the input cannot be converted to an integer, prompt the user again
        print("Invalid input. Please enter a valid number.")
