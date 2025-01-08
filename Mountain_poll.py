# Create an empty dictionary to store responses
responses = {}

# Set a flag to indicate that the polling process is active
polling_active = True

# Start a loop to collect responses while polling is active
while polling_active:

    # Prompt the user to enter their name
    name = input("\nWhat is your name? ")

    # Prompt the user to enter the mountain they would like to climb
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary, with the name as the key and the mountain as the value
    responses[name] = response

    # Ask the user if another person would like to respond
    repeat = input("Would you like to let another person respond? (yes/no) ")

    # If the user says 'no', set the flag to False to end the loop
    if repeat == 'no':
        polling_active = False

# After polling is complete, display the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    # Print each person's name and the mountain they want to climb
    print(f"{name} would like to climb {response}.")
