import time
from amazon_scraper import make_url_list, scraper, control
from db_conneciton import db_asin_list, update_product_price

def main():
    while True:
        # Get product infor from amazon.com
        make_url_list(db_asin_list)
        scraper()
        
        # Check for price change.
        for index, row in control.iterrows():  
            if row["db_price"] != row["new_price"]:  
                update_product_price(row["ASIN"], row["new_price"])  
            else:
                pass

        print("Price and stocks are successfully checked.")
        
        time.sleep(60 * 60 * 60)    # Wait for 6 hours. 

if __name__ == "__main__":
    main()
