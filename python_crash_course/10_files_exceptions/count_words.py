# Program to count the number of words in a file.
from pathlib import Path

def count_words(filename: str) -> int:
    """Function to count the number of words in a file."""
    path = Path(filename)


    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist.")
        return -1
    else:
        # Count the number of words in the file.
        words = contents.split()

        # Return the number of words in the file.
        return len(words)

def main():
    """Main function to count the number of words in a file."""
    # Files to read from.
    files = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'siddhartha.txt']

    # Count the number of words in each file.
    for file in files:
        number_of_words = count_words(file)
        if number_of_words != -1:
            print(f"The file {file} has about {number_of_words} words.")

# Call the main function.
if __name__ == '__main__':
    main()