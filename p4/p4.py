import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the e-commerce page to scrape (replace with actual product page URL)
url = 'https://example.com/products'

# Send a request to the website
response = requests.get(url)
# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Lists to store the extracted data
product_names = []
product_prices = []
product_ratings = []

# Loop through the product items and extract the required details
for product in soup.find_all('div', class_='product-item'):
    # Extract the product name
    name = product.find('h2', class_='product-title').text.strip()
    product_names.append(name)
    
    # Extract the product price
    price = product.find('span', class_='product-price').text.strip()
    product_prices.append(price)
    
    # Extract the product rating, if available
    rating_tag = product.find('div', class_='product-rating')
    rating = rating_tag.text.strip() if rating_tag else 'No rating'
    product_ratings.append(rating)

# Create a pandas DataFrame to store the data
data = pd.DataFrame({
    'Product Name': product_names,
    'Price': product_prices,
    'Rating': product_ratings
})

# Save the data to a CSV file
data.to_csv('product_data.csv', index=False)
print("Product information saved to 'product_data.csv'")
