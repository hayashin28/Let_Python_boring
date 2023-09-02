cat_names = []#配列の初期化という（要素数は0）
while True:
    print('猫' + str(len(cat_names) + 1) + 'の名前を入力して下さい\n' + '(終了するにはEnterキーだけを押して下さい\n：)')
    name = input()
    if name == '':
        break
    cat_names += [name] #配列の最後にnameを追加する（要素が増える）
#break した先はここになる。
print('----------------------whileの外-----------------------')
print('猫の名前は以下の通り：')
for name in cat_names:
    print('　' + name)