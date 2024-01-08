"""
follow_link.py - A script to follow links in HTML and retrieve information.

This script takes a URL, follows a specified number of links at a given position,
and prints the content of the final page.

Usage:
    python follow_link.py
"""

import urllib.request
from bs4 import BeautifulSoup

def follow_links_and_print(url, position, count):
    """
    Follows links in HTML, retrieves information, and prints the content of the final page.

    Parameters:
        url (str): The starting URL.
        position (int): The position of the link to follow.
        count (int): The number of links to follow.

    Returns:
        None
    """
    print(f"Retrieving {url}..")

    for _ in range(count):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")

        tags = soup('a')
        url = tags[position - 1].get('href', None)

        print(f"Retrieving {url}")

    last_name = soup.find('h1').contents[0]
    print(f"\nThe answer to the assignment is: {last_name}")

if __name__ == "__main__":
    # Get input from the user
    url = input("Enter URL: ")
    count = int(input("Enter count: "))
    position = int(input("Enter position: "))

    follow_links_and_print(url, position, count)
