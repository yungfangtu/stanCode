"""
File: anagram.py
Name: Tina
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
word_list = {}


def main():
    print(f'Welcome to stanCode "Anagram Generator!" (or {EXIT} to quit)')
    read_dictionary()
    word = str(input('Find anagrams for: '))
    start = time.time()
    find_anagrams(word)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global word_list
    with open(FILE, 'r') as f:
        for line in f:
            line = line.split()
            word_list[line[0]] = 0


def find_anagrams(s):
    """
    :param s: str, the input entered by user
    """
    # global word_list
    if s in word_list:
        ch_lst = []
        for ch in s:
            ch_lst.append(ch)
        anagram_lst = []
        find_anagrams_helper(s, ch_lst, '', anagram_lst)
        print(str(len(anagram_lst))+' anagrams: ', end='')
        print(anagram_lst)


def find_anagrams_helper(s, ch_lst, current_str, anagram_lst):
    """
    :param s: the word user entered
    :param ch_lst: list, word s split in characters
    :param current_str: empty str to append characters
    :param anagram_lst: list containing all anagrams
    """
    global word_list
    if ch_lst == [] and current_str not in anagram_lst and current_str in word_list:
        # print('Searching...')
        print('Found: ' + str(current_str))
        anagram_lst.append(current_str)
    else:
        for ch in ch_lst:
            ch = ch_lst.pop(0)
            current_str += ch
            # if has_prefix(current_str):
            find_anagrams_helper(s, ch_lst, current_str, anagram_lst)
            current_str = current_str[0:len(current_str)-1]
            ch_lst.append(ch)


def has_prefix(sub_s):
    """
    :param sub_s: str, the possible prefix of anagrams
    :return: boolean
    """
    global word_list
    for word in word_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
