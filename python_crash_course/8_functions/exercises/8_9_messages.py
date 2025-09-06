# Program to display the messages in a list.

def show_messages(messages):
    """
    Function to display a list of messages.
    :param messages: A list of messages.
    """
    for message in messages:
        print(message)

def main():
    """Mainline logic to display messages."""
    messages = ['hello', 'it is what it is','to be or not to be', 'just do it']
    show_messages(messages)

# Call the main function.
if __name__ == '__main__':
    main()