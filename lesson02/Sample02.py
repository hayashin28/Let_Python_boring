# 条件式 if文

name = 'Alice'
password = 'swordfish'

if name == 'Mary':
    print("Maryさんこんにちは")
    if password == 'swordfish':
        print('認証しました')
    else:
        print('パスワードが間違っています')
elif name == 'Alice':
    print('初めましてAliceさん')
else:
    print('失礼いたしました')