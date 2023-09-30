#イミュータブルなデータ型
name = 'Zophie a cat'
# 7番目の要素に文字列を追加しようとしている
#name[7] = 'the'
new_name = name[:7] + 'the' + name[8:] 

print(name)
print(new_name)

eggs = [1, 2, 3]
eggs[2] = 6