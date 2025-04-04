# Data Scraper Python Program

This program demonstrates two approaches for scraping data using Python:

1. **Public API Scraping:** Fetches and displays data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts).
2. **Web Scraping:** Retrieves and parses headlines from the BBC News homepage using BeautifulSoup.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Disclaimer](#disclaimer)
- [License](#license)

## Overview

This program is designed as an example of how to extract data from external sources using two common techniques:
- **API Scraping:** Using the `requests` library to interact with a public REST API.
- **Web Scraping:** Using the `requests` and `BeautifulSoup` libraries to retrieve and parse HTML content from a website.

## Features

- **API Data Extraction:**  
  Retrieves a list of posts from JSONPlaceholder and prints the post ID and title for the first 10 posts.

- **Web Scraping:**  
  Scrapes the BBC News homepage for headlines by extracting text from `<h3>` elements (adjustable based on page structure).

- **Error Handling:**  
  Includes basic error handling to catch and display HTTP request errors.

## Requirements

- **Python Version:** Python 3.6 or higher
- **Libraries:**
  - `requests`
  - `beautifulsoup4`

## Installation

Before running the program, install the required libraries using pip:

```bash
pip install requests beautifulsoup4
