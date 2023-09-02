import random

pets   = ['Dog', 'Cat', 'Moose']
people = ['Alice', 'Bob', 'Carol', 'David']

print(random.choice(pets))

random.shuffle(people)
print(people)