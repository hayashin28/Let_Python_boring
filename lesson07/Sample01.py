import re


bat_regex = re.compile(r"Bat(wo)?man")
mo1 = bat_regex.search("The Adventures of Batman")
print(mo1.group() if mo1 else "該当なし")

mo2 = bat_regex.search("The Adventures of Batwoman")
print(mo2.group() if mo2 else "該当なし")

print("\n------------------------------------------------------------------\n")

bat_regex = re.compile(r"Bat(wo)*man")
mo1 = bat_regex.search("The Adventures of Batman")
print(mo1.group() if mo1 else "該当なし")

mo2 = bat_regex.search("The Adventures of Batwowowowowowowowowoman")
print(mo2.group() if mo2 else "該当なし")

print("\n------------------------------------------------------------------\n")

bat_regex = re.compile(r"Bat(wo)+man")
mo1 = bat_regex.search("The Adventures of Batwoman")
print(mo1.group() if mo1 else "該当なし")

mo2 = bat_regex.search("The Adventures of Batwowowowowowowowowoman")
print(mo2.group() if mo2 else "該当なし")

mo3 = bat_regex.search("The Adventures of Batman")
print(mo3.group() if mo3 else "該当なし")

print("\n------------------------------------------------------------------\n")

bat_regex = re.compile(r"(Ha){3}")
mo1 = bat_regex.search("HaHaHa")
print(mo1.group() if mo1 else "該当なし")

mo1 = bat_regex.search("Ha")
print(mo1.group() if mo1 else "該当なし")

bat_regex = re.compile(r"(Ha){3,5}?")
mo2 = bat_regex.search("HaHaHaHaHa")
print(mo2.group() if mo2 else "該当なし")
