import re

input_string ="aff sdssfsdf dfsfsf fasdfasf ddasdasdsad"

pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, input_string)


print(matches)