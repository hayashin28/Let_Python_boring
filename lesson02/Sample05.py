# 無限ループを発生させる
while True:
    print('あなたは誰ですか？')
    name = input()
    if len(name) == 0:
        # ループの直ぐ下に戻る
        continue
    else:
        print(name + 'さん、こんにちは！')
        # ループを抜ける
        break
        