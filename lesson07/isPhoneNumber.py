import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('私の電話番号は415-555-4242です。')
print('電話番号が見つかりました：' + mo.group() if mo else '電話番号はみつかりませんでした。')

print('--------------------------------------------------------\n')
phone_num_regex = re.compile(r'((\d\d\d))-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('私の電話番号は415-555-4242です。')
print(mo.group() if mo else '電話番号が見つかりませんでした。')

print('\n--------------------------------------------------------\n')
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_num_regex.search('私の電話番号は415-555-4242です。')
print('電話番号が見つかりました：' + mo.group() if mo else '電話番号はみつかりませんでした。')

print('--------------------------------------------------------\n')
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.findall('私の電話番号は415-555-4242か012-044-4444です。')
print(mo if mo else '電話番号が見つかりませんでした。')