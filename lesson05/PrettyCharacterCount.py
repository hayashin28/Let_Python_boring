import pprint

message = 'It wa a bright cold day in April,'\
          ' and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
print(pprint.pformat(count))