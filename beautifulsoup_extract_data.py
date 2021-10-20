import requests
from bs4 import BeautifulSoup
import json


class Bs4movie():
    url = "https://4k-hdr.org/"

    headers = {
        "User-Agnet": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }
    varlist = []

    def __init__(self):
        self.res = requests.get(url=self.url, headers=self.headers)
        if self.res.status_code == 200:
            if self.parse_data():
                self.write_data()
        else:
            print('Request failed!')

    def parse_data(self):
        try:
            soup = BeautifulSoup(self.res.text, 'lxml')
            divs = soup.find_all(class_='main-news-title')
            for item in divs:
                movie = item.find(class_="main-news-title2")
                # print(movie.text.strip('\n'))
                m_type = item.find(class_="main-news-cat")
                # print(m_type.text.strip('\n'))
                m_url = item.find('a')['href']
                # print(m_url)
                vardict = {
                    "movie": movie.text.strip('\n'),
                    "type": m_type.text.strip('\n'),
                    "url": m_url
                }
                self.varlist.append(vardict)
            return True
        except:
            return False

    def write_data(self):
        with open("4kmovie.json", "w") as fp:
            json.dump(self.varlist, fp)


a = Bs4movie()
