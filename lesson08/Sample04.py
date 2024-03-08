import pyinputplus as pyip

response = pyip.inputStr('入力検証1：', allowRegexes=['^(|I|V|X|L|C|D|M)+$', 'zero'], blockRegexes=['.'])
print(response)

response = pyip.inputStr('入力検証2：', allowRegexes=['^(i|v|x|l|c|d|m)+$', 'zero'],blockRegexes=['.'])
print(response)

response = pyip.inputNum('入力検証3：', blockRegexes=['[02468]$'])
print(response)

