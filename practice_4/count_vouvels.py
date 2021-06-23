import collections
from collections import defaultdict

vouvels = 'eouaiy'
some_str = "Hello world!"

long_test = "Lorem Ipsum is simply dummy text of axa the printing and typesetting industry. Lorem Ipsum has been the " \
            "industry's standard dummy text ever coollooc since the 1500s, when An unknown printer took a galley of type and " \
            "scrambled it to make a type specimen book aa"


# count_vowels = {'e': 0, 'o': 3, 'u': 0, 'a': 0, 'i': 0, 'y': 0}

# count_vowels = {}
# for letter in vouvels:
#     count_vowels[letter] = 0
#
# print(count_vowels)
#
# for letter in some_str:
#     if letter in count_vowels:
#         count_vowels[letter] += 1
#
# print(count_vowels)
#



# count_vowels = defaultdict(int)
#
# for letter in some_str:
#     count_vowels[letter] += 1
#
# print(count_vowels)

from collections import Counter
import string

for char in string.punctuation + string.digits:
    long_test = long_test.replace(char, "")

rez = Counter(long_test.split())
print(rez)

rez2 = dict(rez.most_common(2))
print(rez2 )