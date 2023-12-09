message = 'It wa a bright cold day in April,'\
          ' and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    # count-> 辞書型の変数 character-> key 0 -> 初期値

    count[character] = count[character] + 1
    # 辞書[key] = (value値 + 1)
    # key : (value値 + 1)

print(count)