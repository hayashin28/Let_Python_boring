#---spam()関数---
def spam():#2'
    eggs = 'spam local' #spamの変数
    print(eggs)
    #return=>#3 spam()の位置へ戻る
#---spam()関数終わり---
# ↑
# 別々の関数
# ↓
#--bacon()---
def bacon():#1'
    eggs = 'bacon local' #baconの変数
    print(eggs) 
    spam() #=>def spam(): へ #2
    #3'
    print(eggs) #baconの変数
    #return => メインプログラムに戻る
#---bacon()---

#------メインプログラムの開始位置----------------#

#グローバル変数(どの関数にも属さない)
eggs = 'global'

bacon() #=>def bacon(): へ  #1

print(eggs)#グローバル変数のeggsの中身を出力
