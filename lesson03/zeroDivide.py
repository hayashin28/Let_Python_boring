#--- ある母数を42で割り、その商を返却する関数 ---
def spam(divide_by):
    try: # try以降に発生した例外は
        return 42 / divide_by
    except ZeroDivisionError: # exceptで指定された例外で拾われる
        print('ゼロ除算が発生しました。\n不正な引数です。')
    #return 暗黙のreturn


#--- メインプログラム ---
print(spam(2))
print(spam(12))
print(spam(0))  # ゼロ除算が発生する
# ZeroDivisionError: division by zero
# ゼロによる割り算エラー : ゼロで割り算した

print(spam(1))