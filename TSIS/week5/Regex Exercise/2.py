import re

string = input("Enter a string: ")

pattern = r'a{1}b{2,3}'

match = re.search(pattern, string)

if match:
    print("Match found!")
else:
    print("Match not found!")