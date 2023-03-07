import re

# define the pattern to match
pattern = r'a*b*'

# test strings
test_strings = ['ab', 'aab', 'abb', 'aabb', 'ac', 'abc']

# loop through the test strings and print the matches
for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")