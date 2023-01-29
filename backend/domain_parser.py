from urllib.parse import urlparse

trusted_domains = [
    'www.amazon.com',
    'www.ebay.com',
    'www.walmart.com',
    'www.bestbuy.com',
    'www.target.com',
    'www.newegg.com',
    'www.bhphotovideo.com',
    'www.adorama.com',
    'www.amazon.in',
    'www.amazon.co.uk',
    'www.amazon.ca',
    'www.amazon.com.au',
    'www.amazon.com.br',
    'www.amazon.com.mx',
    'www.amazon.com.sg',
    'www.amazon.com.tr',
    'www.amazon.ae',
    'www.amazon.sa',
    'www.amazon.cn',
    'www.amazon.co.jp',
    'www.amazon.de',
    'www.amazon.es',
    'www.amazon.fr',
    'www.amazon.it',
    'www.amazon.nl',
    'www.amazon.se',
    'www.flipkart.com',
    'www.snapdeal.com',
    'www.shopclues.com',
    'www.aliexpress.com',
    'www.alibaba.com',
    'www.alibaba.in',
    'www.myntra.com',
    'www.shopify.com',
    'www.shopify.in',
    'www.etsy.com',
    'www.indiamart.com',
]



def get_domain_name(url):
    domain = urlparse(url).netloc
    return domain



# function to return webscraped data of an amazon site
def get_amazon_data(url):
    pass


if __name__ == '__main__':
    print(get_domain_name('https://www.amazon.com.tr/search/lol'))