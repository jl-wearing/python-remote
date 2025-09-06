# Program to return a dictionary of information about an album.

def make_album(title, author, number_of_songs=None):
    """Return a dictionary of information about an album."""
    album = {
        'title': title.lower(),
        'author': author.lower(),
    }

    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album

def main():
    """Mainline logic to test the make_album function."""
    # Test with 4 different dictionaries.
    eminem = make_album('encore', 'eminem')
    david_guetta = make_album('nothing but the beat', 'david guetta')
    beyonce = make_album(author='beyonce', title='speak my mind')
    avicii = make_album('true', 'avicii', number_of_songs=10)

    # Output
    print(eminem, david_guetta, beyonce, avicii, sep='\n')

# Call the main function.
if __name__ == '__main__':
    main()