# Prompt the user to input the number of people for dinner and convert the input to an integer
people = int(input("How many people are you for dinner? "))

# Check if the number of people is greater than 8
if people > 8:
    # If more than 8 people, print a message indicating they need to wait for a table
    print("You will have to wait a bit for a table.")
else:
    # If 8 or fewer people, print a message indicating their table is ready
    print("Your table is ready.")
