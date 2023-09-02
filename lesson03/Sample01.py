def spam():
    eggs = 99 # 局所変数 
    #ham =
    bacon() # None
    print(eggs)
    #print(ham)
    #return #暗黙のリターン => noneを返す 

def bacon():
    ham = 101
    eggs = 11 # 局所変数
    #return ham
    #return # 暗黙のリターン

#------------------------------------------------------------
eggs = 0
spam()
print(eggs)

if True:
    eggs = 10

print(eggs)