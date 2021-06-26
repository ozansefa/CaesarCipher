#!/usr/bin/env python

import string
import collections

def caesar(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))

our_string = "Bu betik mükemmel!"

for i in range(len(string.ascii_uppercase)):
    print(i, "|", caesar(our_string, i))
