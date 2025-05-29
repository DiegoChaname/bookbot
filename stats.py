def word_count(book_text):
    word_list = book_text.split()
    count = len(word_list)
    return count

def character_count(book_text):
    characters = {   }
    for char in book_text:
        character = char.lower()
        is_character_present = character in characters
        if is_character_present == False:
            characters[character] = 1
        elif is_character_present == True:
            characters[character] += 1          
    return characters

def sort_on(dict):
    return dict["num"]

def big_to_small(dictionary):
    dictionary_list = []
    for pair in dictionary:
        count = dictionary[pair]
        small_dictionary = {"char" : pair ,"num" : count}
        dictionary_list.append(small_dictionary)

    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list