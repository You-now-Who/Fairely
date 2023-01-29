from flask import Flask, request, jsonify, render_template
from webscraper import generate_reviews
from domain_parser import get_domain_name
from reviews_detect import get_secondary_response

app = Flask(__name__)

global url 
url = ""
global complete_dict
complete_dict = {}
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
global fake_reviews
fake_reviews = 0

def master_change_func(url):
    reviews = []
    global fake_reviews

    domain = get_domain_name(url)
    trusted = False
    if domain in trusted_domains:
        trusted = True
        if 'amazon' in domain:
            return {"trusted": "true", "reviews": 10, "fake_reviews": 5}
            reviews = generate_reviews(url)        
            
            # total_reviews = len(reviews)
            fake_reviews = 0
            for i in reviews:
                x = generate_reviews(reviews[i]['review'])
                if x == 'YES':
                    fake_reviews += 1

    
    return {
        "trusted": trusted,
        "reviews": reviews,
        # "total_reviews": total_reviews,
        "fake_reviews": fake_reviews

        }


@app.route('/get-reviews', methods=['GET'])
def get_reviews():
    
    return complete_dict

@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date": "12/12/2020", 
        "programming":"python"
        }

@app.route('/set-url', methods=['POST'])
def set_url():
    global complete_dict
    global url

    print('Reached Here')
    # print(request.get_json())
    # content = request.get_json()
    content = request.form.get("url")

    url = content
    print(url)
    complete_dict = master_change_func(url)
    
    return render_template('demo.html', complete_dict=complete_dict)

@app.route('/demo')
def demo():
    return render_template('demo.html', complete_dict={})

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)