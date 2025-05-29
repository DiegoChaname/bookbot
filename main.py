import sys

def get_book_text(file_path):
    with open(file_path) as f:
        full_text = f.read()
    return full_text

from stats import word_count

from stats import character_count

from stats import sort_on

from stats import big_to_small

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        file_path = sys.argv[1]
        frankenstein_text = get_book_text(file_path)
        num_words = word_count(frankenstein_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        full_character_count = character_count(frankenstein_text)
        sorted_character_count = big_to_small(full_character_count)
        for i in range(0,len(sorted_character_count)):
            small_dict = sorted_character_count[i]
            char = small_dict["char"]
            num = small_dict["num"]
            if char.isalpha() == True:
                print(f"{char}: {num}")
        print("============= END ===============")
    except Exception as e:
        print(f"An error ocurred: {e}")
    

main()