import mysql.connector
import pandas as pd

# Connect to database
connection = mysql.connector.connect(host="localhost", 
                                    user="root", 
                                    password="your-password", 
                                    database="your-database")

result_list = []
db_asin_list, db_prices_list = [], []

def get_products():
        # Create a Cursor
    cursor = connection.cursor()
        # Make a query for asins
    cursor.execute("SELECT asin, buy_price FROM inventory")

        # Fetch Results
    results = cursor.fetchall()
        
    for result in results:
        result_list.append(result)
    db_asin_list = ', '.join([tup[0] for tup in result_list]).split(", ")
    db_prices_list = [price[1].replace('$', '') for price in result_list]
        # Close the cursor.
    cursor.close()
    return db_asin_list, db_prices_list

db_df = pd.DataFrame({
    "ASIN": db_asin_list,
    "db_price": db_prices_list}) 



def update_product_price(asin, update_price):
    cursor = connection.cursor()    
    update_query = "UPDATE inventory SET buy_price = %s WHERE asin = %s"   # Standart query.
            
    cursor.execute(update_query, (update_price, asin,))  
    connection.commit()
    cursor.close()