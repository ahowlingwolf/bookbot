def count_characters(text):
    char_count = {}  
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in char_count:  
                char_count[letter] = 1
            else:
                char_count[letter] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    word_count = len(words)
    
    character_count = count_characters(file_contents)
    
    char_list = []
    for char, count in character_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info["num"]} times")
    

main()