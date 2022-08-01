"""
File: boggle.py
Name: Tina
----------------------------------------
This file simulates the boggle game. It asks the user to enter 4X4 English letters
and displays all the possible words using those letters.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

word_list = {}


def main():
    read_dictionary()
    letter_d = {}
    for i in range(4):
        letter = str(input(f'{i + 1} row of letters: '))
        letter = letter.split()
        if len(letter) != 4:
            print('Illegal input. ')
            return
        letter_d[i] = letter  # i stands for the row
        for j in range(len(letter)):
            ch = letter[j]
            if not ch.isalpha() or len(ch) != 1:
                print('Illegal input. ')
                return
            if ch.isupper():
                ch = ch.lower()
    start = time.time()
    ch_d = create_word_dictionary(letter_d)
    find_words(letter_d, ch_d)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.split()
            word_list[line[0]] = 1


def create_word_dictionary(letter_d):
    """
    :param letter_d: (dictionary) Containing all the letters, separated as lists.
    :return: ch_d: (dictionary) Containing all letters(keys), paired with neighboring letters.
    """
    ch_d = {}
    for x in range(4):
        for y in range(4):
            ch_d[(x, y)] = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < 4 and 0 <= y + j < 4:
                        if i != 0 or j != 0:
                            ch_d[(x, y)].append((x + i, y + j))
    return ch_d


def find_words(letter_d, ch_d):
    """
    :param letter_d: (dictionary) Containing all the letters(keys), separated in lists.
    :param ch_d: (dictionary) Containing all coordinate of letters, paired with neighboring coordinates.
    :return: (list) Containing all possible words.
    """
    ans_lst = []
    for position in ch_d:
        visited = [position]
        x, y = position
        word = letter_d[x][y]
        find_words_helper(ch_d, position, word, letter_d, ans_lst, visited)
    print(f'There are {len(ans_lst)} words in total. ')


def find_words_helper(position_d, position, word, letter_d, ans_lst, visited):
    """
    :param position_d: (dictionary) Containing all letters(keys), paired with neighboring letters.
    :param position: (str) Every letter entered by the user.
    :param word: (str) Current string.
    :param letter_d: (dictionary) Containing all the letters(keys), separated in lists.
    :param ans_lst: (list) Containing all possible words.
    :param visited: (list) Containing all chosen spots.
    :return: (list) Containing all possible words starting with ch.
    """
    if len(word) >= 4 and word in word_list and word not in ans_lst:
        print('Found: ' + str(word))
        ans_lst.append(word)
        find_words_helper(position_d, position, word, letter_d, ans_lst, visited)
    else:
        for spot in position_d[position]:
            if spot not in visited:
                visited.append(spot)
                x, y = spot
                word += letter_d[x][y]
                find_words_helper(position_d, spot, word, letter_d, ans_lst, visited)
                # Un-choose
                word = word[0:len(word) - 1]
                visited.pop()


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    global word_list
    for word in word_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
