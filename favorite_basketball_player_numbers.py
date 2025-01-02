# Define a dictionary with basketball player names as keys and their jersey numbers as values
favorite_basketball_player_numbers = {
    "Michael": 23,  # Michael's jersey number is 23
    "Lebron": 9,    # LeBron's jersey number is 9
    "Kobe": 24,     # Kobe's jersey number is 24
    "Steph": 30,    # Steph's jersey number is 30
    "Luka": 77      # Luka's jersey number is 77
}

# Loop through each key-value pair in the dictionary
for name, number in favorite_basketball_player_numbers.items():
    # Print a formatted message showing the player's name and their jersey number
    print(f"Most loved jersey number of {name} is {number}.")
