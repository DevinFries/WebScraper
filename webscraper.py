import requests
from bs4 import BeautifulSoup

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
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; DataScraper/1.0)'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find headline elements (this may need adjustments based on the page structure)
        headlines = soup.find_all('h3')
        print("\n=== Headlines from BBC News ===")
        for headline in headlines[:10]:  # limiting to first 10 headlines
            text = headline.get_text(strip=True)
            if text:
                print(text)
    except requests.RequestException as e:
        print(f"Error fetching webpage data: {e}")

if __name__ == "__main__":
    scrape_api()
    scrape_webpage()
