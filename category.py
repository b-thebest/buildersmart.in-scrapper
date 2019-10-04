import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.buildersmart.in/#')
soup = BeautifulSoup(page.text, 'html.parser')

category = soup.find(class_='menu-nav-list')

category_list = category.find_all('a')

with open('people.csv', 'a') as writeFile:
    writer = csv.writer(writeFile)
    for artist_name in category_list:
        ls = []
        data = str(artist_name.contents[0])
        soup2 = BeautifulSoup(data, features="html.parser")
        t = soup2.find('span', {'class': 'menu-title'})
        ls.append(t.text)
        ls.append(artist_name.get('href'))
        writer.writerow(ls)
writeFile.close()