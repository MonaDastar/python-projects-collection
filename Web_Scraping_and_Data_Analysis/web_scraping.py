# scrape_books.py
#import libraries required for requesting, parsing the HTML and storing data
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the bookstore website
url = 'http://books.toscrape.com/'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information about books (hypothetical example)
    book_titles = [title.text for title in soup.find_all('h2', class_='book-title')]
    book_authors = [author.text for author in soup.find_all('p', class_='book-author')]
    book_prices = [price.text for price in soup.find_all('span', class_='book-price')]

    # Create a DataFrame using pandas
    books_df = pd.DataFrame({
        'Title': book_titles,
        'Author': book_authors,
        'Price': book_prices
    })

    print(books_df) # the output is empty, I need to learn why the books_df is empty so i go back to Coursera lessons for python web application. commit up to here. 
    # Save the DataFrame to a CSV file
    books_df.to_csv('book_data.csv', index=False)
    print("Scraping and data analysis completed. Data saved to 'book_data.csv'.")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
