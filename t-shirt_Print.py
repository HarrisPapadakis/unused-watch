def make_shirt(size, message):
    """Display the message that will be printed on the t-shirt."""  # Explains the purpose of the function to show the shirt's size and message with a dockstring.
    print(f"A {size} shirt will be printed with the message: '{message}'.")  # Outputs a formatted string describing the shirt size and message.

make_shirt("Large", "Iron Maiden")  # Calls the function with a positional argument for size and message.
make_shirt(size="Medium", message="Python Rules")  # Calls the function using keyword arguments for clarity and flexibility.
