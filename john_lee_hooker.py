def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a neatly formatted full name."""  # Added a docstring for better understanding
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"  # Corrected the quotes inside the f-string
    else:
        full_name = f"{first_name} {last_name}"  # Corrected the quotes inside the f-string
    return full_name.title()

# Calling the function with and without the middle name
musician = get_formatted_name("jimi", "hendrix")
print(musician)  # Output: Jimi Hendrix

musician = get_formatted_name("john", "hooker", "lee")
print(musician)  # Output: John Lee Hooker
