import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

def get_lat_long(query):
    # Format the search URL with the query
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    
    # Set headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    # Make the request
    response = requests.get(search_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all <div> elements and look for specific text within each
        divs = soup.find_all("div")
        for div in divs:
            div_text = div.get_text(strip=True)
            
            # Check if the div contains both "Latitude" and "Longitude" keywords
            if "Latitude" in div_text and "Longitude" in div_text:
                # Try to match the latitude and longitude in both decimal and DMS formats
                latitude = re.search(r"Latitude[:\s]*([-+]?\d+(\.\d+)?|(\d+°\s*\d+'?\s*\d*\"?)\s*[NS]?)", div_text)
                longitude = re.search(r"Longitude[:\s]*([-+]?\d+(\.\d+)?|(\d+°\s*\d+'?\s*\d*\"?)\s*[EW]?)", div_text)
                
                if latitude and longitude:
                    return latitude.group(1), longitude.group(1)
                
                # Indicate if parsing failed on a matched div
                return None, None

    # If request fails or data not found
    return None, None

