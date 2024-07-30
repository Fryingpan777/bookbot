def main():
    path_to_book = "books/frankenstein.txt"
    text = get_text(path_to_book)
    number_of_words = count_words(text)
    number_of_letters = count_letters(text)
    name_of_book = get_name_of_book(path_to_book)

    number_of_letters_list = [{"char": key, "num": value} for key, value in number_of_letters.items()]
    number_of_letters_list.sort(reverse=True, key=sort_on)

    print(f"Report of the book {name_of_book}")
    print(f"Number of words found: {number_of_words}")

    for i in number_of_letters_list:
        print("The symbol", i["char"], "was found", i["num"], "times")
        #print(f"The symbol '{i["char"]}' was found {i["num"]} times")
    print("---End of report!---")

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

def sort_on(dict_list):
    return dict_list["num"]


main()

    