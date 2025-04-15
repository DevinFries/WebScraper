# Web Scraper

A versatile Python web scraper that demonstrates how to collect data from various public web sources.

## Overview

This tool demonstrates ethical web scraping techniques for several types of online resources:

1. **Public API** - Fetches and displays data from JSONPlaceholder
2. **News Headlines** - Retrieves current headlines from BBC News
3. **Weather Information** - Collects alerts from the National Weather Service
4. **Inspirational Quotes** - Gathers quotes from a scraping-friendly website

## Features

- Clean, modular code organization with separate functions for each data source
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

 install dependencies directly:

```bash
pip install requests beautifulsoup4
```

## Usage

Simply run the script:

```bash
python web_scraper.py
```

The script will sequentially scrape data from all sources and display the results in your terminal.

## Customization

You can easily modify the script to:

- Add new data sources by creating additional scraping functions
- Adjust the number of items retrieved by changing the slicing parameters
- Modify the parsing logic to extract different elements from the pages
- Change the delay parameters to be more or less aggressive

## Ethical Considerations

This script demonstrates responsible web scraping by:

1. Using appropriate user-agent headers to identify itself
2. Adding delays between requests to avoid overwhelming servers
3. Only scraping publicly accessible data
4. Limiting the number of requests made during each run

Always review a website's robots.txt file and terms of service before scraping to ensure compliance with their policies.

## Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring their use of this script complies with applicable laws and website terms of service.

## License

GPL-3.0
