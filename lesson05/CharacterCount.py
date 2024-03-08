message = 'It wa a bright cold day in April,'\
          ' and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    # count-> 辞書型の変数 character-> key 0 -> 初期値

    count[character] = count[character] + 1
    #count[character] += 1
    """********************************
    * 辞書[key] = value値を表す。
    * 辞書は、要素番号の代わりにkeyを指定する。
    * なので、10行目は下記が行われていると同義である。
    * 辞書[key] = value値 + 1
    ********************************"""

print(count)