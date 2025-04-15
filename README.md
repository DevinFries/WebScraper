# Web Scraper

A versatile Python web scraper that collects meaningful data from various real-world data sources.

## Overview

This tool demonstrates how to collect and display useful data from multiple public sources:

1. **Space Data** - Real-time information about the International Space Station (ISS) location and astronauts currently in space
2. **Cryptocurrency Market** - Current prices, 24h changes, and market caps for top cryptocurrencies
3. **News Headlines** - Current headlines from BBC News
4. **Weather Information** - Current weather conditions for specified locations (requires API key)
5. **Inspirational Quotes** - Collection of quotes from a scraping-friendly website

## Features

- Clean, modular code organization with separate functions for each data source
- Mix of API-based data collection and HTML scraping techniques
- Responsible scraping practices including realistic headers and request delays
- Error handling to gracefully manage connection issues
- Pretty-printed output for easy reading of results

## Requirements

```
requests>=2.28.1
beautifulsoup4>=4.11.1
```

## Installation

1. Clone this repository or download the script
2. Install the required packages:

```bash
pip install requests beautifulsoup4
```

## Usage

1. For the weather function, sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api) and replace `YOUR_API_KEY` in the code with your actual key.

2. Run the script:

```bash
python web_scraper.py
```

The script will sequentially fetch data from all sources and display the results in your terminal.

## Data Sources

### Open Notify API
Shows real-time data about the International Space Station (ISS) and astronauts currently in space. This demonstrates working with a simple, no-authentication JSON API.

### CoinGecko API
Displays current market data for top cryptocurrencies including price, 24-hour change percentage, and market capitalization. Shows how to work with financial APIs and handle parameters.

### BBC News
Scrapes current headlines from the BBC News website, demonstrating HTML parsing with BeautifulSoup and extraction of text content from web pages.

### OpenWeatherMap API
Retrieves current weather conditions for a specified city. This demonstrates using an API that requires an API key for authentication.

### Quotes to Scrape
Collects inspirational quotes from a website specifically designed for web scraping practice.

## Customization

You can easily modify the script to:

- Change the city for weather data
- Adjust the number of cryptocurrencies displayed
- Add new data sources by creating additional scraping functions
- Modify the parsing logic to extract different elements from pages

## Ethical Considerations

This script demonstrates responsible data collection by:

1. Using appropriate user-agent headers to identify itself
2. Adding delays between requests to avoid overwhelming servers
3. Only accessing publicly available data and APIs
4. Using APIs according to their terms of service

Always review a website's robots.txt file and terms of service before scraping to ensure compliance with their policies.

## Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring their use of this script complies with applicable laws and website terms of service.

## License

GPL-3.0
