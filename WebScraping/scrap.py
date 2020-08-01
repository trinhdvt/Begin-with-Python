import json
import sys

import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news?p="


class Story(object):

    def __init__(self, title, link, score, writer):
        self.title = title
        self.link = link
        self.score = score
        self.writer = writer


def crawl_page(page_number: int):
    res = requests.get(url + str(page_number))
    soup = BeautifulSoup(res.text, 'html.parser')
    story = soup.select(".storylink")
    subtext = soup.select(".subtext")

    for index, item in enumerate(story):
        title = item.getText()
        link = item['href']
        vote = subtext[index].select(".score")
        score = None
        if len(vote):
            score = int(vote[0].getText().split(" ")[0])
        blogger = None
        writer = subtext[index].select(".hnuser")
        if len(writer) > 0:
            blogger = writer[0].getText()
        yield Story(title, link, score, blogger)


def run(number_of_pages):
    for i in range(1, number_of_pages + 1):
        yield crawl_page(i)


argv = sys.argv
number_page = 1
if len(argv) > 1 and int(argv[1]) > 0:
    number_page = int(argv[1])
    if number_page > 20:
        print("Too greedy!")
        exit()

if __name__ == '__main__':
    with open("hacker_new_scrapy.txt", "w") as file:
        file.writelines(f"## First {number_page} pages!\n")
        for page in run(number_page):
            for detail in page:
                file.writelines(json.dumps(detail.__dict__, indent=3))
                file.write(",\n")
    file.close()
