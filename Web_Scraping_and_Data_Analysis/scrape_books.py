"""
scrape_books.py - A script to scrape book information from a bookstore website.

This script sends an HTTP request to a specified URL, scrapes book information
from the HTML content, and stores the data in a pandas DataFrame. The DataFrame
is then saved to a CSV file.

Usage:
    python scrape_books.py
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(url):
    """
    Scrapes book information from the provided URL and saves it to a CSV file.

    Parameters:
        url (str): The URL of the bookstore website.

    Returns:
        None
    """
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information about books (hypothetical example)
        book_titles = [title.text for title in soup.find_all('h1', class_='book-title')]
        book_authors = [author.text for author in soup.find_all('p', class_='book-author')]
        book_prices = [price.text for price in soup.find_all('span', class_='book-price')]

        # Create a DataFrame using pandas
        books_df = pd.DataFrame({
            'Title': book_titles,
            'Author': book_authors,
            'Price': book_prices
        })

        print(books_df)  # the output is empty; I need to learn why the books_df is empty, so I go back to Coursera lessons for Python web application. Commit up to here.
        # Save the DataFrame to a CSV file
        books_df.to_csv('book_data.csv', index=False)
        print("Scraping and data analysis completed. Data saved to 'book_data.csv'.")
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")

if __name__ == "__main__":
    # Replace the URL with the actual URL of the bookstore website
    bookstore_url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    scrape_books(bookstore_url)
