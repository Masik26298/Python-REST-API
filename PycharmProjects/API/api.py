from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
headers = {"accept": "*/*",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.4.25 Yowser/2.5 Safari/537.36"
          }

base_url = "https://news.tut.by/world/"


@app.route('/news', methods=['GET'])
class SiteScraper():
    def __init__(self, news):
        self.news = news

    def tut(self):
        session = requests.Session()
        request = session.get(base_url, headers=headers)
        soup = bs(request.content, "html.parser")
        spans = soup.find_all('span', attrs={'class': 'entry-cnt'})
        name = 'tut.by'
        link = 'https://news.tut.by/world'
        for span in spans:
            header = span.find("span", attrs={'class': 'entry-head _title'}).text
            text = span.find("span", attrs={'class': 'entry-note'})
            news = {"news": [{'name': name,
                               'link': link,
                               'header': header,
                               'text': text}]}

            return jsonify(news)



    def cnn(self):
        session = requests.Session()
        request = session.get(base_url, headers=headers)
        soup = bs(request.content, "html.parser")
        spans = soup.find_all('div', attrs={'class': 'cd__wrapper'})
        name_2 = 'cnn.com'
        link_2 = 'https://edition.cnn.com/world'
        for span in spans:
            header_2 = span.find("span", attrs={'class': 'cd__headline-text'}).text
            text_2 = span.find("p", attrs={
                'class': 'Text-sc-1amvtpj-0-p render-stellar-contentstyles__Paragraph-sc-9v7nwy-2 fAchMW'}).text
            news_2 = {"news": [{'name': name_2,
                                'link': link_2,
                                'header': header_2,
                                'text': text_2}]}

            return jsonify(news_2)


news = SiteScraper('news')
news.tut()
news_2 = SiteScraper('news')
news_2.cnn()


@app.route('/news/tut.by', methods=['GET'])
class TUTSiteScraper(SiteScraper):
   def __init__(self, news):
       super().__init__(news)

   def tut_by(self):
       session = requests.Session()
       request = session.get(base_url, headers=headers)
       soup = bs(request.content, "html.parser")
       spans = soup.find_all('span', attrs={'class': 'entry-cnt'})
       name_3 = 'tut.by'
       link_3 = 'https://news.tut.by/world'
       for span in spans:
           header_3 = span.find("span", attrs={'class': 'entry-head _title'}).text
           text_3 = span.find("span", attrs={'class': 'entry-note'})
           news_3 = {"news": [{'name': name_3,
                             'link': link_3,
                             'header': header_3,
                             'text': text_3}]}

           return jsonify(news_3)


news_3 = TUTSiteScraper('news')
news_3.tut_by()


@app.route('/news/cnn.com', methods=['GET'])
class CNNSiteScraper(SiteScraper):
    def __init__(self, news):
       super().__init__(news)

    def cnn_com(self):
        session = requests.Session()
        request = session.get(base_url, headers=headers)
        soup = bs(request.content, "html.parser")
        spans = soup.find_all('div', attrs={'class': 'cd__wrapper'})
        name_4 = 'cnn.com'
        link_4 = 'https://edition.cnn.com/world'
        for span in spans:
            header_4 = span.find("span", attrs={'class': 'cd__headline-text'}).text
            text_4 = span.find("p", attrs={
                'class': 'Text-sc-1amvtpj-0-p render-stellar-contentstyles__Paragraph-sc-9v7nwy-2 fAchMW'}).text
            news_4 = {"news": [{'name': name_4,
                                'link': link_4,
                                'header': header_4,
                                'text': text_4}]}

            return jsonify(news_4)


news_4 = CNNSiteScraper('news')
news_4.cnn_com()


if __name__ == '__main__':
    app.run(debug=True)