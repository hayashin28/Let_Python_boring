def a():
    print('a() starts')
    b()#=>def b へ 1
    d()#=>def d へ 3
    #return => 呼び出し元a()に戻る
    print('a() returns')
def b(): #1'
    print('b() starts')
    c()#=>def c へ 2
    print('b() returns')
    #return def a():に戻る
def c(): #2'
    print('c() starts')
    print('c() returns')
    #return =>def b():に戻る
def d(): #3'
    print('d() starts')
    print('d() return')
    #return => def a(): へ

a()