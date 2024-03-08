from pathlib import Path
import os

print(Path.cwd())

os.chdir(r'C:\Windows\System32')
print(Path.cwd())