# Program to display the messages in a list.

def show_message(current_message):
    """Display the current message being sent."""
    print(f"Currently sending: {current_message}")

def send_messages(messages):
    """
    Function to send a list of unsent messages to a sent box.
    :param messages: a list of unsent messages
    :return: a list of sent messages
    """
    sent_messages = []
    while messages:
        # Get the first message from the list of messages.
        current_message = messages.pop(0)

        # Display the current message being printed.
        show_message(current_message)

        # Move the current message to sent messages.
        sent_messages.append(current_message)

    return sent_messages

def show_sent_messages(sent_messages):
    """
    Simple function to display a list of sent messages.
    :param sent_messages: a list of sent messages
    """
    print('\nThese are the sent messages:')
    for message in sent_messages:
        print(f'\t{message}')

def main():
    """Mainline logic for sending messages."""
    messages = ['it is what it is', 'just do it', 'hello', 'to be or not to be']

    # Send the messages.
    sent_messages = send_messages(messages[:])

    # Show the list of sent messages.
    show_sent_messages(sent_messages)

    # Check the list of unsent messages.
    print(messages)

# Call the main function.
if __name__ == '__main__':
    main()