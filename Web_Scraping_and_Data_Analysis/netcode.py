from selenium import webdriver
from bs4 import BeautifulSoup
import csv

url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

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

# Write the information to 'book_data.csv'
with open('book_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Author', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write data
    writer.writerow({'Title': title, 'Author': author, 'Price': price})

# Close the Selenium WebDriver
driver.quit()
