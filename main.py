from stats import num_words
from stats import character_count

def get_book_text (path_to_file):
    with open(path_to_file) as text:
        file_contents = text.read()
       # print(file_contents)
    return file_contents


def main ():
    text = get_book_text ("books/frankenstein.txt")
    words = num_words(text)
    letters = character_count(text)
    print(f"{words} words found in the document")
    print(f"{letters}")

main()


    



        