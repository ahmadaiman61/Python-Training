
import requests
import pandas as pd
import math
import time
import random

base_url = 'https://www.lazada.com.my/face-treatments-serums/?ajax=true&page=1&spm=a2o4k.pdp_revamp.cate_4_1.4.746c7234OR2oBC'

def get_urls():
    req = requests.get(base_url).json()
    total = req['mainInfo']['totalResults']
    page = req['mainInfo']['pageSize']
    total_list = int(total)
    page_size = int(page)
    total_page = math.ceil(total_list/page_size)

    urls = []
    for i in range(1,5):
        url = 'https://www.lazada.com.my/face-treatments-serums/?ajax=true&page={}&spm=a2o4k.pdp_revamp.cate_4_1.4.746c7234OR2oBC'.format(i)
        urls.append(url)
    return urls

def scrape(url):
    req = requests.get(url).json()
    rows = req['mods']['listItems']

    product_detail = []

    for row in rows:
        product = row.get('name', '')
        brand = row.get('brandName', '')
        is_sponsored = row.get('isSponsored', '')
        location = row.get('location', '')
        price = row.get('price', '')
        seller = row.get('sellerName', '')
        review_count = row.get('review', '')
        rating_score = row.get('ratingScore', '')
        sold_count = row.get('itemSoldCntShow', '')

        product_detail.append((product, brand, is_sponsored, location, price, seller, review_count, rating_score, sold_count))
    return product_detail

def data_frame(data):
    df = pd.DataFrame(data, columns=['Product', 'Brand', 'Is Sponsored', 'Location', 'Price', 'Seller', 'Review Count', 'Rating Score', 'Sold Count'])
    return df

def save_to_xls(df):
    df.to_excel('Commerce.xlsx', index=False)
    print("Success")

if __name__ == '__main__':   
    urls = get_urls()

    all_product = []
    for i in range(0,len(urls)):
        product = scrape(urls[i])
        time.sleep(random.randint(2,9))
        all_product.extend(product)

    df = data_frame(all_product)
    print(df)
    save_to_xls(df)





