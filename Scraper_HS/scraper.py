import requests
from bs4 import BeautifulSoup
import string
import os

pages = input()
pg = int(pages) + 1
comp = input()
for i in range(1, pg):
    print(i)
    stru = f"Page_{i}"
    if not os.path.exists(stru):
        os.mkdir(stru)
    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        list = soup.find_all('li', {'class': 'app-article-list-row__item'})
        for a in list:
            b = a.find('span', {'class': 'c-meta__type'}).text
            if b == comp:
                urlnew = "https://www.nature.com"
                urlsite = a.find('a', {'itemprop': 'url'})["href"]
                kok = urlnew + urlsite
                kik = a.find('a', {'itemprop': 'url'}).text
                for character in string.punctuation:
                    kik = kik.replace(character, '')
                # for charactir in kik:
                #     if charactir == "’":
                #         kik = kik.replace(charactir, "")

                foles = stru + "/" + kik.replace(" ", "_") + ".txt"
                #print(foles)
                responses = requests.get(kok)
                soups = BeautifulSoup(responses.content, 'html.parser')
                lol = soups.find('div', {'class': 'c-article-body u-clearfix'}).text
                #print(lol.replace("\r\n", ""))

                file = open(foles, 'wb')
                file.write(lol.encode("utf-8"))
                file.close()
                #print(f"File {foles} created!")
    except:
        print("Error, try again.")

print("Saved all articles.")
