import requests as r
import re
from bs4 import BeautifulSoup
import ast
import base64
import threading


class Game:
    def __init__(self, title, link):
        self.title = title
        self.link = link


class BTS:
    def __init__(self, category):
        self.url_root = 'http://blacktiesports.net'
        self.url_init = '/category/'
        self.url_category = category
        self.games = []
        self.threads = []
        self.scrape()

    def links(self):
        for game in self.games:
            print(game.title)
            print(game.link)

    def scrape(self):
        soup = BeautifulSoup(r.get(self.url_root + self.url_init + self.url_category).text, features='html.parser')
        link_elements = soup.findAll(name='a', attrs='btn-facebook')
        if len(link_elements) == 0:
            print("No links")
            return
        games = soup.findAll(name='div', attrs='card-user')
        for game in games:
            t = threading.Thread(target=self.scrape_game, args=[game])
            t.start()
            self.threads.append(t)
        for t in self.threads:
            t.join()

    def scrape_game(self, game):
        title = game.find('p', 'description').text.replace('\n', '')

        url_directory = game.find('a')
        url = self.url_root + url_directory.get('href')
        headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0'}
        soup2 = BeautifulSoup(r.get(url, headers=headers).text, features='html.parser')
        iframe = BeautifulSoup(r.get(soup2.find('iframe', {'id': 'stream'}).get('src')).text,
                               features='html.parser')
        scripts = iframe.find_all('script')
        c = str(scripts[-1].contents)
        a = re.search('var (.*?) = \"\"', c)
        b = re.search(' = (\[.*?\])', c)
        try:
            msg = a.group(1)
        except:
            return
        subtrahend = int(re.search('\- (.*?)\);', c).group(1))
        code = ast.literal_eval(b.group(1).replace('\\n', ''))
        message = ""

        for c in code:
            message += chr(int(re.sub('\D', '', base64.b64decode(c).decode('utf-8'))) - subtrahend)
        try:
            m3u8 = re.search('source: \'(.*?)\'', message).group(1)
        except:
            m3u8 = base64.b64decode(re.search('source: window\.atob\(\'(.*?)\'', message).group(1)).decode('utf-8')
        self.games.append(Game(title, m3u8))
        # print(f'#EXTINF:-1 tvg-id="NBA.us" tvg-country="US" tvg-language="English" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/NBA_TV.svg/1200px-NBA_TV.svg.png" group-title="{title}",{title}')

    def generate_m3u(self):
        with open(self.url_category + '.m3u', 'w') as f:
            f.write("#EXTM3U\n")
            for g in self.games:
                f.write(
                    f'#EXTINF:-1 tvg-id="NBA.us" tvg-country="US" tvg-language="English" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/NBA_TV.svg/1200px-NBA_TV.svg.png" group-title="{g.title}",{g.title}\n')
                f.write(g.link)
                f.write('\n')

