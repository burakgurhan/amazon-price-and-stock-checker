# amazon-price-and-stock-checker

E-commerce seller requires tools to find profitable products and inspect market needs. It is important to track product prices and stocks to find profitable opportunities and also it is important to track stocks to manage inventory.
There are a lot of useful Amazon seller tools but, it is not cheap for low budgets. All tools based on a pattern, scrape, and store data for each product.
This is a helpful tool for dropshippers and arbitrage sellers. I use it to track prices and stock my inventory.

It is based on product ASINs(Amazon Standard Identification Number) in inventory. Stores the ASIN, title, buy_price, and sell_price in a local database.
Regularly (4 times a day) visits the product detail pages for each ASIN and scrapes the current price and stock. 
If there is a price change, it will update the old price with the new price.
