# Program to count how common a word is in a file.
from pathlib import Path

def get_input() -> str:
    """Function to get what word to count in each file."""
    word = input('Enter the word you want to count in each file: ')
    return word

def read_file(filename: str) -> str or None:
    """Function to read and return the contents of a file."""
    path = Path(filename)

    try:
        # Get the contents of the file.
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    else:
        return contents

def count_common_word(word: str, contents: str) -> int:
    """Function to count how common a word is in a book."""
    return contents.lower().count(word.lower())

def main():
    """Main function for counting how common a word is in a file."""
    files = ['only_seven_were_hanged.txt', 'romeo_and_juliet.txt']

    # Get input from the user.
    word = get_input()

    for file in files:
        # Read the contents of the file.
        content = read_file(file)

        # Count how common the word is in each file.
        if content:
            number_of_occurrences = count_common_word(word, content)

            # Display the count.
            print(f"The number of times {word} appears in {file} is {number_of_occurrences}.")

# Call the main function.
if __name__ == '__main__':
    main()