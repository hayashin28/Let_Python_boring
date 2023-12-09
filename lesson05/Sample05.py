print('\n--------------- get()メソッド ---------------')
public_item = {'apples' : 5, 'cups' : 9}
print('I am bringing ', end = '')
print(public_item.get('cups', 0), end = '')
print(' cups.')
print('I am bringing ', end = '')
print(public_item.get('eggs', 0), end = '')
print(' eggs.')

print('\n--------------- setdefault()メソッド ---------------')
spam = {'name' : 'Pooka', 'age' : 5}
print(spam.setdefault('color', 'black'))
print(spam)

print(spam.setdefault('color', 'white'))
print(spam)
