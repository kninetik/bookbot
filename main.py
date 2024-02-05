
def main():
    book_path = "books/frankenstein.txt"
    
    print(f"--- Begin report of books/{book_path}")

    text = get_book_text(book_path)
    print(f'{get_word_count(text)} words found in the document \n')

    letter_count_dict = count_letters(text)
    letter_count_listdict = []
    for i in letter_count_dict:
        temp_dict = {'letter':i,'count':letter_count_dict[i]}
        letter_count_listdict.append(temp_dict)

    letter_count_listdict.sort(reverse=True, key=sort_on)
    
    for i in range(0,len(letter_count_listdict)):
        test = letter_count_listdict[i]
        if test['letter'].isalpha():
            print(f"The '{test['letter']}' character was found {test['count']} times")
    
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

# def count_letters(text):
#     basetext = text.lower()
#     basetext_list = list(basetext)
#     list_alphabet = list(map(chr, range(97, 123)))
#     letter_count_dict = {}
#     for letter in list_alphabet:
#         count = 0
#         for i in range(0, len(basetext_list)):
#             if letter == basetext_list[i]:
#                 count += 1
#         letter_count_dict[letter]=count
#     print(letter_count_dict)

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def sort_on(dict):
    return dict["count"]

main()




