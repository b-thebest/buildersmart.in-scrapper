import requests
from bs4 import BeautifulSoup
import urllib
import os
import csv

links = ['https://www.buildersmart.in/cement',
         'https://www.buildersmart.in/sand',
         'https://www.buildersmart.in/tmt-steel',
         'https://www.buildersmart.in/bricks-blocks',
         'https://www.buildersmart.in/electrical',
         'https://www.buildersmart.in/plumbing-html',
         'https://www.buildersmart.in/wooden-products',
         'https://www.buildersmart.in/tiles',
         'https://www.buildersmart.in/bathroom-accessories',
         'https://www.buildersmart.in/hardware-fixtures',
         'https://www.buildersmart.in/paints-and-finishes',
         'https://www.buildersmart.in/lighting-products',
         'https://www.buildersmart.in/naturalstones',
         'https://www.buildersmart.in/rmc-151',
         'https://www.buildersmart.in/roofing-solutions',
         'https://www.buildersmart.in/upvcdoors-windows',
         'https://www.buildersmart.in/home-automation',
         'https://www.buildersmart.in/home-decor',
         'https://www.buildersmart.in/modular-kitchen',
         'https://www.buildersmart.in/construction-chemicals',
         'https://www.buildersmart.in/glass-hardware']

resume_file = open('lastSession.txt', 'r')
start = int(resume_file.read())
for index, link in enumerate(links[start:]):
    write_resume = open('lastSession.txt', 'w+')
    write_resume.write(str(index+start))

    category_name = link.split('/')[-1]
    print(category_name, link)
    if not os.path.exists('images/' + category_name):
        os.makedirs('images/' + category_name)

    with open('csvFiles/' + str(category_name) + '.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        for page_number in range(1, 30, 1):
            empty = []
            print(page_number)
            page = requests.get(link + '?limit=12&p=' + str(page_number))
            soup = BeautifulSoup(page.text, 'html.parser')

            pages = soup.find(class_='pages')

            page_list = soup.find_all('a', {'class': 'next i-next'})
            #print(page_list)

            product_block = soup.find('div', {'id' : 'category-products-wrap'})
            product_link = product_block.find_all('div', {'class': 'item-inner'})
            # product_link = products.find_all('a')
            #print('productlink', len(product_link))

            for product in product_link:
                if len(product.div['class']) == 1:
                    #print(product.a['href'])
                    product_page = requests.get(product.a['href'])
                    product_soup = BeautifulSoup(product_page.text, 'html.parser')
                    name = product_soup.find_all('div', {'class' : 'product-name'})[0].h1.text
                    price = product_soup.find_all('span', {'class' : 'price'})[-1].text
                    description = product_soup.find_all('div', {'class' : 'std'})[-1].text
                    description = description.replace(',', '')
                    description = description.replace('\n', ' ')
                    img_link = product_soup.find_all('div', {'class' : 'more-views'})
                    img_link = img_link[0].ul.li.a['href']
                    urllib.request.urlretrieve(img_link, 'images/' + category_name + '/' + name)
                    arr = [str(name), str(price), str(description), str(category_name), str(img_link)]
                    writer.writerow(arr)
            if page_list == empty:
                break
    csv_file.close()