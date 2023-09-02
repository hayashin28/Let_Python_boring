# 配列の要素を初期化
#        [0]    [1]    [2]       [3]
spam = ['cat', 'bat', 'rat', 'elephant']
try:
    print(spam[10000])
except IndexError:
    print('インデックスエラー\nリストのインデックス範囲外')