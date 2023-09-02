# 配列の要素を初期化
#        [0]    [1]    [2]       [3]
spam = ['cat', 'bat', 'rat', 'elephant']
try:
    print(spam[1])
    print(spam[1.0]) # type: ignore
except TypeError:
    print('型エラー\nリストのインデックスは浮動小数点でなく整数がスライスでかければならない')
    
print(spam[int(1.0)])