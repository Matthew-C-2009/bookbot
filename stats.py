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

 

