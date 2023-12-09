birthdays = {'アリス':'4/1', 'ボブ':'12/12', 'キャロル':'4/4',}

while True:
    print('名前を入力してください（終了するにはEnterだけ押してください）:', end = "")
    name = input() # キーを入力
    
    if name == '':
        break
    
    if name in birthdays:
        print(name + ' の誕生日は ' + birthdays[name])
    else:
        print(name + ' の誕生日は未登録です。') # 入力したキーが存在しなかった
        print('誕生日を登録してください：', end = "")
        bday = input() # 5行目で入力したキーに対するバリューを入力
        birthdays[name] = bday
        print(birthdays[name]) # Map名['キー'] -> バリュー値を取得できる。
        print(birthdays)  # birthdaysの中身を全て出力する。
        print('誕生日の辞書を更新しました。')
    