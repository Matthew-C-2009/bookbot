from stats import num_words
from stats import character_count
from stats import character_dictionary


def get_book_text (path_to_file):
    with open(path_to_file) as text:
        file_contents = text.read()
       # print(file_contents)
    return file_contents


def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text (book_path)
    words = num_words(text)
    letters = character_count(text)
    sorted = character_dictionary(letters)
    print_report(book_path,words,sorted)

    #print(f"{sorted}")

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

    #for dic in sorted:
        ##for y in dic:
            #print (f"{dic[y]}")
        #    z = z + [dic[y]]

     #   print(f"{dic["char"]}: {dic["num"]}")

main()


    



        