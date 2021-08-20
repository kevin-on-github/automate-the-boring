from re import compile

message = 'Call my phone number 555-515-4545, or my office at 555-515-1234.'

phoneNumRegex = compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search(message)
moall = phoneNumRegex.findall(message)

print(moall)
print(mo.group(1))
print(mo.group(2))