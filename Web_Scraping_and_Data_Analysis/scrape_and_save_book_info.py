"""
scrape_and_save_book_info.py - A script to scrape book information from a webpage and save it to a CSV file.

This script uses Selenium to open a webpage, waits for dynamic content to load,
and then uses BeautifulSoup to parse the HTML and extract information about a book.
The extracted data (title, author, and price) is then written to a CSV file.

Usage:
    python scrape_and_save_book_info.py
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import csv

def scrape_and_save_book_info(url, csv_filename='book_data.csv'):
    """
    Scrapes book information from the provided URL, extracts data using BeautifulSoup,
    and saves it to a CSV file.

    Parameters:
        url (str): The URL of the webpage containing book information.
        csv_filename (str): The filename for the CSV file to save the data. Default is 'book_data.csv'.

    Returns:
        None
    """
    # Use Selenium to open the webpage
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for dynamic content to load (adjust the wait time as needed)
    driver.implicitly_wait(10)

    # Get the page source after dynamic content is loaded
    html_source = driver.page_source

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_source, 'html.parser')

    # Extract the information
    title = soup.find('h1').text.strip()
    author = soup.find('p', class_='instock availability').find_next('p').text.strip()
    price = soup.find('p', class_='price_color').text.strip()

    # Write the information to the CSV file
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Author', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        writer.writerow({'Title': title, 'Author': author, 'Price': price})

    # Close the Selenium WebDriver
    driver.quit()

if __name__ == "__main__":
    # Replace the URL with the actual URL of the webpage containing book information
    webpage_url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    scrape_and_save_book_info(webpage_url)
