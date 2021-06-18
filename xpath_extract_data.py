import requests
from lxml import etree
import json


class Extract:
    url = "https://news.yahoo.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }
    filepath = "./yahoo.json"

    def __init__(self):
        self.data = []
        res = requests.get(url=self.url, headers=self.headers)
        if res.status_code == 200:
            print("Web page read successfully")
            with open("yahoo.html", "w") as fp:
                fp.write(res.text)
            if self.parse_data():
                self.write_data()

    def parse_data(self):
        html = etree.parse("yahoo.html", etree.HTMLParser())
        title = html.xpath("//*[contains(@id, 'YDC-Stream')]/ul//h3/a/text()")
        source = html.xpath("//*[@id='YDC-Stream']//div[@class='C(#959595) Fz(11px) D(ib) Mb(6px)']/text()")
        region = html.xpath(
            "//*[@id='YDC-Stream']//div[@class='Fz(12px) Fw(b) Tt(c) D(ib) Mb(6px) C($c-fuji-blue-1-a) Mend(9px) Mt(-2px)']/text()")
        for i in range(len(title)):
            res = {'title': title[i], 'source': source[i], 'region': region[i]}
            self.data.append(res)
        if self.data:
            print("Parsed successfully")
        return True

    def write_data(self):
        with open(self.filepath, 'w') as fp:
            json.dump(self.data, fp)
        print("Write successfully")


a = Extract()
