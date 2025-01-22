import datetime

# Function to get and display the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"The current time is {current_time}")

# Main program execution
if __name__ == "__main__":
    while True:
        # Prompt user for input
        user_input = input("Ask me 'what time is it?' or type 'exit' to quit: ").strip().lower()
        
        # Check user input and respond accordingly
        if user_input == "what time is it?":
            tell_time()
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            # Handle unrecognized input
            print("I didn't understand that. Please ask 'what time is it?' or type 'exit'.")
-