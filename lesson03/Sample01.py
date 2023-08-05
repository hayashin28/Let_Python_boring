def spam():
    eggs = 99 # 局所変数 
    #ham =
    bacon() # None
    print(eggs)
    #print(ham)

def bacon():
    ham = 101
    eggs = 0 # 局所変数
    #return ham
    #return # 暗黙のリターン
    
spam()