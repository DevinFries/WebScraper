import requests
from bs4 import BeautifulSoup
import time
import random
import json

def scrape_api():
    """
    Scrape data from Open Notify API which provides real-time information 
    about the International Space Station (ISS) and the astronauts in space.
    """
    # Get current astronauts in space
    astronaut_url = "http://api.open-notify.org/astros.json"
    # Get current ISS location
    iss_location_url = "http://api.open-notify.org/iss-now.json"
    
    try:
        # Get astronaut data
        astronaut_response = requests.get(astronaut_url)
        astronaut_response.raise_for_status()
        astronaut_data = astronaut_response.json()
        
        # Get ISS location data
        iss_response = requests.get(iss_location_url)
        iss_response.raise_for_status()
        iss_data = iss_response.json()
        
        # Display astronaut information
        print("=== Real-time Space Data from Open Notify API ===")
        print(f"There are currently {astronaut_data['number']} people in space:")
        for person in astronaut_data['people']:
            print(f"- {person['name']} on board {person['craft']}")
        
        # Display ISS location
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        timestamp = iss_data['timestamp']
        
        print(f"\nCurrent ISS Location:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Timestamp: {timestamp} (Unix time)")
        
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

def scrape_cryptocurrency():
    """
    Scrape current cryptocurrency prices from CoinGecko's public API.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': '10',
        'page': '1',
        'sparkline': 'false'
    }
    
    try:
        print("\n=== Current Cryptocurrency Prices ===")
        response = requests.get(url, params=params)
        response.raise_for_status()
        crypto_data = response.json()
        
        # Display cryptocurrency information
        print(f"{'Name':<15} {'Symbol':<8} {'Current Price':>12} {'24h Change':>12} {'Market Cap':>15}")
        print("-" * 65)
        
        for coin in crypto_data:
            name = coin['name'][:14]
            symbol = coin['symbol'].upper()
            current_price = f"${coin['current_price']:,.2f}"
            price_change = f"{coin['price_change_percentage_24h']:.2f}%"
            market_cap = f"${coin['market_cap']:,.0f}"
            
            print(f"{name:<15} {symbol:<8} {current_price:>12} {price_change:>12} {market_cap:>15}")
            
    except requests.RequestException as e:
        print(f"Error fetching cryptocurrency data: {e}")

def scrape_weather():
    """
    Scrape weather data from OpenWeatherMap API (free tier).
    Note: Replace 'YOUR_API_KEY' with an actual API key from openweathermap.org
    """
    # You need to sign up for a free API key at openweathermap.org
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    city = "London"
    
    if api_key == "YOUR_API_KEY":
        print("\n=== Weather Data ===")
        print("To use the weather API, you need to:")
        print("1. Sign up for a free API key at openweathermap.org")
        print("2. Replace 'YOUR_API_KEY' in the code with your actual API key")
        print("3. Optionally change the city from 'London' to your preferred location")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        
        print(f"\n=== Current Weather in {city} ===")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Feels Like: {weather_data['main']['feels_like']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        
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
    
    scrape_cryptocurrency()
    be_nice_to_servers()
    
    scrape_webpage()
    be_nice_to_servers()
    
    scrape_weather()
    be_nice_to_servers()
    
    scrape_quotes()
    
    print("\nWeb scraping completed.")
