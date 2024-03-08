import re

name_regex = re.compile(r'First Name: (.*) LastName: (.*)')
mo = name_regex.search('First Name: AI LastName: Sweigart')
print(mo.group()  if mo else "該当なし")
print(mo.group(1) if mo else "該当なし")
print(mo.group(2) if mo else "該当なし")

print('\n-----------------------------------------------------------------\n')
print("【非貪欲】")
nongreedy_regex = re.compile(r'<.*?>') # ? を外すとできる限り短い文字
mo = nongreedy_regex.search('<To Serve man> for dinner.>')
print(mo.group() if mo else "該当なし")

print("【貪欲】")
nongreedy_regex = re.compile(r'<.*>') # ? を外すとできる限り長い文字
mo = nongreedy_regex.search('<To Serve man> for dinner.>')
print(mo.group() if mo else "該当なし")
^0[987]0$[0-9]{8}