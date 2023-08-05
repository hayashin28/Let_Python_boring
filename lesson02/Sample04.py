# あなたの名前 と入力しないと抜けられ#ループ
#name = ''
#while name != 'あなたの名前':
#    print('あなたの名前を入力して下さい')
#    name = input()
#print(name + 'さん、どうも！')

name = ''
while True:
    print('あなたの名前を入力して下さい')
    name = input()
    if name == '林宏典':
        break
print(name + 'さん、どうも！')
