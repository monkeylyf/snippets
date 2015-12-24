"""A script for hacking terminal in fallout4.

Author: madarfacar

This script takes a list of words and yield a sequence of words that has the
best chance to hack the ternimal.

HOWTO:
You are given a number of words, with the same length. The length increases
when the difficulty level increase. You have 4(5 with some cool stuff) attempts
to guess the password. If all attempts fail, the ternimal will be locked down
and you can not try again.

if your chosen password is incorrect, the number of letters that match the
ternimal's password(both letter and position) will be displayed on screen.
"""

import sys
from collections import Counter
from itertools import groupby
from operator import itemgetter

BLACK_SQUARE = u'\u25A0'


def guess(words):
    """

    :param words: tuple, of str in upper case with same length
    """
    length = len(words[0])

    char_freq_per_idx = []
    # Count frequency of char at index i.
    for idx in xrange(length):
        counter = Counter()
        for word in words:
            char = word[idx]
            counter[char] += 1
        char_freq_per_idx.append(counter)

    #print 'rankings:'
    #p(char_freq_per_idx)

    rank_words = []

    for word in words:
        score = sum(char_freq_per_idx[i][char] for i, char in enumerate(word))
        rank_words.append((score, word))

    rank_words.sort(reverse=True)

    #print 'Ranking and words:'
    #p(rank_words)
    iterator = groupby(rank_words, key=itemgetter(0))
    grouped_best_guesses = iterator.next()
    return grouped_best_guesses[1].next()[1]


def feedback(words, attempted, likeness):
    """Re-guess given attempted word and likeness.

    :param words: list, of words
    :param attempted: str, word
    :param likeness: int, likeness with real password
    """
    cal_likeness = lambda x, y: sum(1 if a == b else 0 for a, b in zip(x, y))
    ramained_words = []

    for word in words:
        if word != attempted and cal_likeness(word, attempted) == likeness:
            ramained_words.append(word)
    return ramained_words


def my_print(string):
    """My print.

    :param string: str
    """
    print u'>{}'.format(string)


def input_likeness(word):
    """User input likeness and do type check.

    :param word: str
    :return likeness: int
    """
    likeness = None
    while likeness is None:
        user_input = raw_input('>Likeness=')
        if user_input.isdigit():
            digit = int(user_input)
            if digit < 0:
                my_print('LIKENESS MUST BE NON-NEGATIVE')
            elif digit > len(word):
                my_print('LIKENESS CANNOT BE LARGER THAN {}'.format(len(word)))
            else:
                likeness = digit
                # How to refresh the raw_input stdout by '\r' or it's not stdout?
                my_print(word)
                my_print('Entry denied')
                my_print('Likeness={}'.format(likeness))
        else:
            my_print('LIKENESS MUST BE A NUMBER')
    return likeness


def ensure(words):
    """Ensure all word are upper case and with same length.

    :param words: list, of str
    """
    if len(words) == 0:
        raise ValueError("Input cannot be empty")

    length_of_first_word = len(words[0])
    if not all(len(word) == length_of_first_word for word in words):
        raise ValueError("Input words have different lengths")

    return tuple(word.upper() for word in words)


def main():
    """Main."""
    if len(sys.argv) == 1:
        raise Exception('\nUsage: python script.py <word1> <word2> <word3>...')
    attempt_left = 4

    attempt = None
    likeness = None

    words = ensure(sys.argv[1:])
    while attempt_left > 0 and words:
        squares = ' '.join([BLACK_SQUARE] * attempt_left)
        my_print(u'Attempts Remaining: {}'.format(squares))
        if attempt_left == 1:
            my_print('Warning: last attempt!')
        if attempt is not None and likeness is not None:
            words = feedback(words, attempt, likeness)

        if not words:
            raise Exception('Invalid input or script error')
        attempt = guess(words)
        my_print('SUGGESTED ATTEMPTS={}'.format(attempt))
        likeness = input_likeness(attempt)

        if likeness == len(attempt):
            my_print('HACKED IN SUCCESSFULLY')
            break
        attempt_left -= 1
    else:
        my_print('Terminal locked down...')


if __name__ == '__main__':
    main()
