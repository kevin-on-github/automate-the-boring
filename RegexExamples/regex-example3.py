import re


# This script is essentially a find and replace using regular expressio strings.

message = 'Agent Alice gave the secret formula to Agent Bob.'
#namesRegex = re.compile(r'Agent \w+')
namesRegex = re.compile(r'Agent (\w)(\w*)') # Takes the raw string beginning with Agent breaks the name into 2 groups
mo = namesRegex.findall(message)
for i in mo:
    print(i)

mo1 = namesRegex.sub(r'Agent \1****', message) # \1 means use the text from group 1 ['A', 'B']
print(mo1)
