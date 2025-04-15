import requests
from bs4 import BeautifulSoup
import time
import random

def scrape_api():
    """
    Scrape data from a public API (JSONPlaceholder).
    This function retrieves a list of posts and prints the ID and title.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print("=== Data from Public API ===")
        for item in data[:10]:  # limiting to first 10 items for brevity
            print(f"Post ID: {item['id']}, Title: {item['title']}")
    except requests.RequestException as e:
        print(f"Error fetching API data: {e}")

def scrape_webpage():
    """
    Scrape data from a public webpage.
    This example fetches the BBC News homepage and extracts headlines.
    """
    url = "https://www.bbc.com/news"
    
    # More realistic user agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # BBC headlines are typically in various elements with specific classes
        # These selectors might need updates as website structure changes
        headlines = []
        
        # Look for headlines in multiple possible locations
        headline_containers = [
            soup.select('.gs-c-promo-heading__title'),  # Main promo headlines
            soup.select('.media__title'),               # Other headlines
            soup.select('h3.lx-stream-post__heading'),  # Live updates
        ]
        
        for container in headline_containers:
            for headline in container:
                text = headline.get_text(strip=True)
                if text and text not in headlines:
                    headlines.append(text)
        
        print("\n=== Headlines from BBC News ===")
        for idx, headline in enumerate(headlines[:15], 1):  # Show top 15 headlines
            print(f"{idx}. {headline}")
            
    except requests.RequestException as e:
        print(f"Error fetching webpage data: {e}")

def scrape_weather():
    """
    Scrape weather data from National Weather Service.
    This is a good example of a public data source that allows scraping.
    """
    url = "https://www.weather.gov/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    
    try:
        print("\n=== Weather Data from National Weather Service ===")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for current weather alerts
        alerts = soup.select('.alert-bar')
        if alerts:
            print("Current Weather Alerts:")
            for alert in alerts[:5]:
                print(f"- {alert.get_text(strip=True)}")
        else:
            print("No major weather alerts found.")
            
        # You could expand this to search for specific forecasts, etc.
            
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")

def scrape_quotes():
    """
    Scrape inspirational quotes from Quotes to Scrape, 
    a website specifically designed for practicing web scraping.
    """
    url = "http://quotes.toscrape.com/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quotes = soup.select('.quote')
        
        print("\n=== Inspirational Quotes ===")
        for i, quote in enumerate(quotes[:5], 1):
            text = quote.select_one('.text').get_text(strip=True)
            author = quote.select_one('.author').get_text(strip=True)
            print(f"{i}. {text}")
            print(f"   - {author}\n")
            
    except requests.RequestException as e:
        print(f"Error fetching quotes: {e}")

def be_nice_to_servers():
    """Add a small delay to avoid hammering servers."""
    time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    print("Starting web scraping demonstration...\n")
    
    scrape_api()
    be_nice_to_servers()
    
    scrape_webpage()
    be_nice_to_servers()
    
    scrape_weather()
    be_nice_to_servers()
    
    scrape_quotes()
    
    print("\nWeb scraping completed.")
