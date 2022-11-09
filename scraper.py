import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site=site

    def scrape(self):
        r=urllib.request.urlopen(self.site)#ファイルを扱うときと同じ感じ
        html=r.read()#ファイルを扱うときと同じ感じ
        parser="html.parser"#もっと良いパーサーもあるhtml5lib(要インストール)
        sp=BeautifulSoup(html,parser)#bsはパーサーを内部で使いパーサーを単独で
                                     #使うより簡単にできる
        for tag in sp.find_all("a"):#bsオブジェクト(読み込んだhtml全体)からaタグ
            #print(tag)              #を含むtagオブジェクトの集合(イテラブルオブジェクト)を返す
            url=tag.get("href")#tagオブジェクトからhref(html属性値)をゲット
            #print(url)
            if url is None:
                continue
            if "/articles" in url:#hrefの値がhttpsで始まってない為以下書き換える
                new_url=url.replace("./articles","https://news.google.com/articles")
                print("\n"+new_url)
                #ダブりもあり元サイトがむず過ぎたため完璧でないかもしれないがこれで一応良い事にする

news="https://news.google.com/topstories?hl=ja&gl=JP&ceid=JP:ja"
Scraper(news).scrape()


