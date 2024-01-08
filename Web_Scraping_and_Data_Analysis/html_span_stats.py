"""
html_span_stats.py - Extract and calculate statistics from numeric content within HTML span tags.

This script fetches HTML content from a specified URL, utilizes BeautifulSoup for
HTML parsing, and extracts numeric data from span tags. It then calculates and
prints statistics including the count and sum of the numeric content.

Usage:
    python html_span_stats.py
"""

import urllib.request
from bs4 import BeautifulSoup
import ssl

def extract_and_calculate_stats(url):
    """
    Fetches HTML content from the provided URL, parses it, and calculates statistics.

    Parameters:
        url (str): The URL from which to fetch HTML content.

    Returns:
        tuple: A tuple containing the count and sum of numeric content within span tags.
    """
    # Create an SSL context
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Fetch HTML content from the URL
    html = urllib.request.urlopen(url).read()

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Get all span tags
    tags = soup('span')

    # Initialize counters
    count = 0
    total = 0

    # Iterate through span tags
    for tag in tags:
        number = int(tag.contents[0])
        total += number
        count += 1

    return count, total

if __name__ == "__main__":
    # Replace the URL with the actual URL from which you want to extract data
    target_url = "http://py4e-data.dr-chuck.net/comments_1945889.html"
    count, total = extract_and_calculate_stats(target_url)

    # Print the results
    print("Count:", count)
    print("Sum:", total)
