import pyinputplus as pyip

response = pyip.inputNum('Enter num:', min=4)
print(response)

response = pyip.inputNum('Enter num(４より大きい値):', greaterThan=4)
print(response)

response = pyip.inputNum('>', min=4, lessThan=6)
print(response)