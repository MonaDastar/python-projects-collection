import xml.etree.cElementTree as ET
import urllib.request, urllib.parse, urllib.error

def parse_xml_comments(url):
    """
    Parses XML data containing comments from the specified URL.

    Args:
        url (str): The URL from which to fetch XML data.

    Returns:
        None. Prints the count and sum of comments.

    Examples:
        Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
        Actual data: http://py4e-data.dr-chuck.net/comments_1945891.xml (Sum ends with 73)
    """
    try:
        # Fetch XML data from the specified URL
        input_data = urllib.request.urlopen(url).read()

        # Parse XML data
        stuff = ET.fromstring(input_data)

        # Extract comments from XML
        lst = stuff.findall("comments/comment")

        # Calculate count and sum of comments
        counts = sum(int(item.find("count").text) for item in lst)

        # Print results
        print("Retrieved", len(input_data), "characters")
        print("Count:", len(lst))
        print("Sum:", counts)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    user_url = input("Enter URL: ")
    parse_xml_comments(user_url)
