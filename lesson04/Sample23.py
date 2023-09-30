spam = ['0', '1', '2', '3', '4', '5']
print('spam = ' + str(spam))
print('---------------------------')

cheese = spam
cheese[1] = 'Hello!'
print('spam = ' + str(spam))
print('cheese = ' + str(cheese))
print('---------------------------')

print('spam = ' + str(spam))
print('cheese = ' + str(cheese))
