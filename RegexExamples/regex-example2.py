import re  # module containing regular expression functions

# batRegex = re.compile(r'Bat(wo)?man') # ? means match 0 or 1 times to match pattern
batRegex = re.compile(r'Bat(wo)*man')  # * means match 0 or more patterns.
mo = batRegex.search('The adventures of Batwowowowowoman.')
mo.group()
print(mo.group())


phoneRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo1 = phoneRegex.findall(
    'My phone number is 555-515-5454, or my office is 525-1234')
for i in mo1:
    print(i)


nameRegex = re.compile(r'First Name: (.*?) Last Name: (.*)')
mo2 = nameRegex.findall('First Name: Kevin Last Name: On-Github')
for i in mo2:
    print(i)
