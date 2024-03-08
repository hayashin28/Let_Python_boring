import re

xmas_regx = re.compile(r'\d+\s\w+')
print(xmas_regx.findall(
        '12 drummers \
        ,11 pipers \
        ,10 lords \
        ,09 loads \
        ,08 maids \
        ,07 swans \
        ,06 geese \
        ,05 rings \
        ,04 birds \
        ,03 hans \
        ,02 doves \
        ,01 partridge' 
    ))

print('\n--------------------------------------------------------\n')

vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats boby food. BABY FOOD.'))

print('\n--------------------------------------------------------\n')

value_regex = re.compile(r'[^aeiouAEIOU]')
value_regex = print(value_regex.findall('RoboCop eats boby food. BABY FOOD.'))

print('\n--------------------------------------------------------\n')

value_regex = re.compile(r'^\d+\w+\d+$')
value_regex = print(value_regex.findall('01234xyz56789'))