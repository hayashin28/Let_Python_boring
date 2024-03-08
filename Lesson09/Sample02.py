from pathlib import Path

my_file = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_file:
    print(Path(r'C:\Users\AI', filename))