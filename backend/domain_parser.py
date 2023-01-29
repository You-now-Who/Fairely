from urllib.parse import urlparse



def get_domain_name(url):
    domain = urlparse(url).netloc
    return domain



# function to return webscraped data of an amazon site
def get_amazon_data(url):
    pass


if __name__ == '__main__':
    print(get_domain_name("https://www.amazon.in/Arturia-MiniLab-Controller-Arpeggiator-Production/dp/B0BGMNKCNT/ref=sr_1_4?crid=2SVPBYDFIRJMX&keywords=arturia%2Bminilab%2B3&qid=1674977350&sprefix=arturi%2Caps%2C700&sr=8-4&th=1"))