import requests
from lxml import etree


class LMonkey:
    loginurl = "https://www.mini4k.com/user/login"
    movieurl = "https://www.mini4k.com/user/9131"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }

    def __init__(self):
        self.req = requests.session()
        if self.login():
            self.getinfo()

    def login(self):
        uname = input('username：')
        passw = input('password：')
        data = {
            'username': uname,
            'password': passw
        }
        # Initiate a post request
        res = self.req.post(url=self.loginurl, headers=self.headers, data=data)
        if res.status_code == 200 or res.status_code == 302:
            print('login successful')
            return True

    def getinfo(self):
        res = self.req.get(url=self.movieurl, headers=self.headers)
        html = etree.HTML(res.text)
        with open("info.html", "w") as fp:
            fp.write(res.text)
        user = html.xpath("//h1[@class='name']/text()")[0]
        role = html.xpath("//div[@class='role']/text()")[0]
        print(user, role)


a = LMonkey()
