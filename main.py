def main():
    path_to_book = "books/frankenstein.txt"
    text = get_text(path_to_book)
    number_of_words = count_words(text)
    number_of_letters = count_letters(text)
    name_of_book = get_name_of_book(path_to_book)
    print(f"Report of the book {name_of_book}")
    print(f"number of words: {number_of_words}")
    print(f"number of individual letters: {number_of_letters}")

def get_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def count_words(file):
    words = file.split()
    return len(words)

def count_letters(string):
    letter_count = {}
    lowered_string = string.lower()
    for i in lowered_string:
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1
    return letter_count

def get_name_of_book(book):
    name = book[6:-4]
    return name




main()

    