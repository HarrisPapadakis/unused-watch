def make_shirt(size='Large', message='I love Python'):
    """Display the message that will be printed on the t-shirt."""  # Explains that the function displays the size and message for a t-shirt using a dockstring.
    print(f"A {size} shirt will be printed with the message: '{message}'.")  # Prints the size and message for the shirt using an f-string.

make_shirt()  # Calls the function with default values
make_shirt(size="Medium")  # Calls the function, overriding the default size with "Medium" while keeping the default message.
make_shirt(size="Small", message="Keep calm and love Python")  # Calls the function, overriding both default values with specific arguments.
