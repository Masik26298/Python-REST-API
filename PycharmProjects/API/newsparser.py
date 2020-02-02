import requests
from bs4 import BeautifulSoup as bs


headers = {"accept": "*/*",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.4.25 Yowser/2.5 Safari/537.36"
          }

base_url = ("https://news.tut.by/world")


def news_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        spans = soup.find_all('span', attrs={'class': 'entry-cnt'})
        for span in spans:
            title = span.find("span", attrs={'class': 'entry-head _title'}).text
            print(title)
        for div in spans:
            href = div.find("div", attrs={'class': 'news-entry big annoticed time ni'})
            print(href['href'])
    else:
        print("ERROR")


news_parse(base_url, headers)