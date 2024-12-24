# Define a dictionary to store each person's favorite programming language
favorite_progr_language = {
    "harris": "python",  # Harris' favorite programming language is Python
    "manos": "java",     # Manos' favorite programming language is Java
    "jorge": "c",        # Jorge's favorite programming language is C
    "edward": "c#",      # Edward's favorite programming language is C#
    "koley": "ruby",     # Koley's favorite programming language is Ruby
    "marly": "python"    # Marly's favorite programming language is Python
}


friends = ["harris", "marly"]                  # Define a list of friends whose favorite programming languages we want to highlight


for name in favorite_progr_language.keys():    # Loop through all the keys (names) in the favorite_progr_language dictionary
    
    print(name.title())                         # Print the name of the person in title case

    
    if name in friends:                          # Check if the current name is in the friends list
        
        language = favorite_progr_language[name].title()       # Get the person's favorite programming language and capitalize it
        
        print(f"\t{name.title()}, I see you love {language}!")        # Print a personalized message about their favorite language
