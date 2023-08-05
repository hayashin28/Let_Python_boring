def spam():
    eggs = 'spam local' #2
    print(eggs)

def bacon():
    eggs = 'bacon local' #1
    print(eggs)
    spam()
    print(eggs) #3

eggs = 'global' #4
bacon()
print(eggs)