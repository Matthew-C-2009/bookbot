def num_words(text):
    word = text.split()
    return len(word)


def character_count(text):
    lower = text.lower()
    list_of_characters = list(lower)
    characters = {}
    
    for letter in list_of_characters:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
   
    return characters

def sort_on(item):
    return item["num"]


def character_dictionary(dictionary):
    list_of_dictionaries = []
    set = {}
    for c in dictionary:
        letter = dictionary[c]
        set = {"char": c, "num":letter}
        #print(f"{set}")
        list_of_dictionaries.append(set) 
    #print(list_of_dictionaries)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries
