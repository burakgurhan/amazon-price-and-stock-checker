import requests
from bs4 import BeautifulSoup
from db_conneciton import * 

new_price_list = []
stock_list = []


# Make list of urls for each products. 
url_list = []
def make_url_list(db_asin_list):
    for asin in db_asin_list:
        url_list.append(f"https://www.amazon.com/dp/{asin}")
    return url_list
make_url_list(db_asin_list)


def scraper():
    # Create a link for each product detail page
    for url in url_list: 
        page_connection = requests.get(url, headers="")
        soup = BeautifulSoup(page_connection.content, "html.parser")

        # Get product Price
        try:
            price_tag = soup.find("span", attrs={"class": "a-offscreen"})
            price = price_tag.text.strip().replace("$", "") if price_tag else "No price"
            new_price_list.append(price)
        except Exception as e:
            print(f"Error getting price for {url}: {e}")

        # Get Stock Count
        try:
            stock_tag = soup.find("span", attrs={"class": "a-size-medium a-color-success"})
            stock = stock_tag.text.strip() if stock_tag else "In stock"
            stock_list.append(stock)
        except Exception as e:
            print(f"Error getting stock for {url}: {e}")

scraper()

scraper_df = pd.DataFrame({
        "ASIN":db_asin_list,
        "new_price": new_price_list,
        "new_stock": stock_list
    })



# Merge db and scrape infos.
control = pd.merge(db_df, scraper_df, on="ASIN")    

