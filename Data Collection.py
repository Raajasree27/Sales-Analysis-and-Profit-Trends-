#Install the nescessary libraries foe scraping
pip install beautifulsoup4
pip install requests
#Wriring the web scraper: Use Python’s BeautifulSoup to extract product details from Amazon.
#Focus on gathering information such as: Product Name, Product Price, Product Reviews
import requests
from bs4 import BeautifulSoup
import csv

# URL of the Amazon product page (change to your target URL)
url = 'https://www.amazon.com/s?k=laptops'

# Set up headers to mimic a browser request (Amazon blocks some scraping attempts)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all products on the page
products = soup.find_all('div', {'class': 's-main-slot s-result-list s-search-results sg-row'})

# Open a CSV file to save the results
with open('amazon_laptops.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product_Name', 'Product_Price', 'Product_Review'])

    # Loop through products and extract details
    for product in products:
        name = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        price = product.find('span', {'class': 'a-price-whole'})
        review = product.find('span', {'class': 'a-size-base'})

        if name and price and review:
            writer.writerow([name.text.strip(), price.text.strip(), review.text.strip()])

print("Data scraping completed and saved to amazon_laptops.csv")
