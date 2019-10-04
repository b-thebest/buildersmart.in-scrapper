import requests
from bs4 import BeautifulSoup

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

for link in links:

    category_name = link.split('/')[-1]
    print(category_name, link)

    i = 1
    while True:
        page = requests.get(link + '?p=' + str(i))
        soup = BeautifulSoup(page.text, 'html.parser')

        pages = soup.find(class_='pages')

        page_list = pages.find_all('a')
        next = str(page_list[0])[-5]

        if next != i:
            products = soup.find(class_ = 'product-image')
            product_link = products.find_all('a')
            print(product_link)
            for product in product_link:
                print(product.get('href'))

        i+=1

