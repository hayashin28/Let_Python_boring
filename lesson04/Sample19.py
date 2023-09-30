## シーケンス型
# 文字列型（String）は、文字型（char）の集合（リスト）である
name = 'Zophie'

print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('p' not in name)

for i in name:
    print('* * * ' + i + ' * * *')