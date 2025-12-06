# Journal Article Web Scraper - SAGE Publications Metadata Extractor

An automated web scraping tool that extracts academic research metadata from SAGE Publications' Journal of Marketing. This Python-based scraper uses Selenium WebDriver to navigate dynamic web pages and collect structured data for research and analysis purposes.

## Features

- **Automated Data Extraction**: Extracts comprehensive metadata from academic journal articles
- **Dynamic Content Handling**: Interacts with JavaScript-rendered pages and dynamic elements
- **Robust Error Handling**: Gracefully handles missing data fields and malformed HTML structures
- **Structured Output**: Exports clean, organized data suitable for research and analysis
- **Multiple Data Points**: Collects titles, authors, abstracts, DOIs, and publication dates

## Extracted Data

The scraper automatically extracts the following information for each article:

- **Article Titles**: Full title of research papers
- **Author Information**: Author names and affiliations
- **Abstracts**: Complete article abstracts
- **DOIs**: Digital Object Identifiers for citation
- **Publication Dates**: First published dates

## Technologies

- **Python 3**: Core programming language
- **Selenium WebDriver**: Browser automation framework
- **Chrome WebDriver**: Chrome browser automation
- **WebDriverWait**: Intelligent wait strategies for dynamic content
- **CSS Selectors**: Precise element targeting

## Installation

### Prerequisites

- Python 3.x installed on your system
- Google Chrome browser installed
- ChromeDriver executable (compatible with your Chrome version)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd journal-web-scraper-main
   ```

2. **Install required Python packages**
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**
   - Download ChromeDriver from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Ensure the version matches your Chrome browser version
   - Place `chromedriver.exe` in the `Flask/` directory (or update the path in `web_scraper.py`)

4. **Update ChromeDriver path** (if needed)
   - Open `Flask/web_scraper.py`
   - Update `chrome_driver_path` variable with your ChromeDriver location

## Usage

1. Navigate to the Flask directory:
   ```bash
   cd Flask
   ```

2. Run the scraper:
   ```bash
   python web_scraper.py
   ```

3. The script will:
   - Open Chrome browser 
   - Navigate to the Journal of Marketing current issue page
   - Extract metadata from all articles
   - Display extracted data in the console

## Project Structure

```
journal-web-scraper-main/
├── Flask/
│   ├── web_scraper.py      # Main scraping script
│   └── chromedriver.exe    # ChromeDriver executable
└── README.md               
```

## Error Handling

The scraper includes robust error handling for:
- Missing article elements
- Network timeouts
- Dynamic content loading delays
- Variations in HTML structure
- Missing data fields

When data is unavailable, the scraper outputs placeholder text (e.g., "Title not found", "Authors not found") to maintain data structure integrity.

## Output Format

Currently, the scraper prints extracted data to the console. Each article's information is displayed with:
- Title
- Authors 
- Published Date
- DOI
- Abstract

## Future Enhancements

- CSV export functionality for structured data storage
- Support for multiple journal sources
- Database integration for data persistence

---

## Demo
<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGo4ODgxOTQxajQ1ZWM2dGV1cmg1MDliNzFjZW10d3J2NTY3bGI2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3B6PVJUpQu8oLgzMWQ/giphy.gif' />
