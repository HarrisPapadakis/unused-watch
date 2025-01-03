# Define a dictionary to store users and their details
users = {
    "aeinstein": {  # Key: username, Value: another dictionary with user details
        "first": "albert",   # First name of the user
        "last": "einstein",  # Last name of the user
        "location": "princeston"  # Location of the user
    },
    "mcurie": {  # Another user
        "first": "marie",
        "last": "curie",
        "location": "paris"
    },
}

# Loop through each username and its corresponding user information in the dictionary
for username, user_info in users.items():
    # Print the username
    print(f"\nUsername: {username}")
    
    # Combine the first and last name into a full name
    full_name = f"{user_info['first']} {user_info['last']}"
    
    # Retrieve the user's location
    location = user_info["location"]

    # Print the full name, formatted with title case
    print(f"\tFull name: {full_name.title()}")
    
    # Print the user's location, formatted with title case
    print(f"\tLocation: {location.title()}")
