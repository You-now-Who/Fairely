# import module
import requests
from bs4 import BeautifulSoup
import pandas as pd
import validators

main_df = pd.DataFrame()
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# user define function
# Scrape the data
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
  
  
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # display html code
    return (soup)  


def cus_data(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    cus_list = []
  
    for item in soup.find_all("span", class_="a-profile-name"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list

def cus_rev(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
  
    for item in soup.find_all("div", class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
        # print("lol")
        data_str = data_str + item.get_text()
  
    result = data_str.split("\n")
    
    return (result)
  
def product_info(soup):
  
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    pro_info = []
  
    for item in soup.find_all("ul", class_="a-unordered-list a-nostyle\
    a-vertical a-spacing-none detail-bullet-list"):
        data_str = data_str + item.get_text()
        pro_info.append(data_str.split("\n"))
        data_str = ""
    return pro_info

def rev_img(soup):
  
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    cus_list = []
    images = []
    for img in soup.findAll('img', class_="cr-lightbox-image-thumbnail"):
        images.append(img.get('src'))
    return images

def generate_reviews(url):


    soup = html_code(url)

    cus_res = cus_data(soup)

    rev_data = cus_rev(soup)
    rev_result = []

    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

    pro_result = product_info(soup)
    
    # Filter the required data
    for item in pro_result:
        for j in item:
            if j == "":
                pass
            else:
                print(j)
    
    img_result = rev_img(soup)
    img_result

    

    cus_res = [*set(cus_res)]
    # initialise data of lists.
    data = {'Name': cus_res,
            'review': rev_result}
    
    print(len(cus_res))
    print(len(rev_result))

    # print(rev_result)

    # print(cus_res)


    # for i in rev_result:
    #     print('\n\n')
    #     print(i)
    #     print('---------------------------------\n\n')


    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save the output.
    # df.to_csv('amazon_review.csv')
    main_df.append(df)

    return df


if __name__ == "__main__":
    # url = "https://www.amazon.in/Arturia-MiniLab-Controller-Arpeggiator-Production/dp/B0BGMNKCNT/ref=sr_1_4?crid=2SVPBYDFIRJMX&keywords=arturia%2Bminilab%2B3&qid=1674977350&sprefix=arturi%2Caps%2C700&sr=8-4&th=1"
    for i in range (1, 100000):
        url = "https://www.amazon.in/Arturia-MiniLab-Controller-Arpeggiator-Production/product-reviews/B0BGMNKCNT/ref=cm_cr_arp_d_paging_btm_next_" + str(i) + "?ie=UTF8&reviewerType=all_reviews&pageNumber=" + str(i)
        
        if not validators.url(url):
            break
        generate_reviews(url)
        print("Page " + str(i) + " Done")

    main_df.to_csv('amazon_review.csv')