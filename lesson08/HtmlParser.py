import requests
from html.parser import HTMLParser

# 適当なURL
url = 'https://ramendb.supleks.jp/'

# Webページを取得
r = requests.get(url)


class MyParser(HTMLParser):
    
    # 開始タグを扱うメソッド
    def handle_starttag(self, tag, attrs):
        print(f'開始タグ: {tag}')
        for attr in attrs:
            print(f'\t属性: {attr}')

# メインの処理
# パーサー生成
parser = MyParser()

# パーサーにデータを入力 
parser.feed(r.text)
