from pathlib import Path

print(Path('spam') / 'bacon' / 'eggs')

print(Path('Spam') / Path('bacon/eggs'))

print(Path('Spam') / Path('bacon', 'eggs'))

home_folder = r'C:\Users\AI'
sub_folder = 'spam'
print(home_folder + '\\' + sub_folder)
print('\\' .join([home_folder, sub_folder]))