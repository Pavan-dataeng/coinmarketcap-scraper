# CoinMarketCap Scraper

A Python project to scrape cryptocurrency data from CoinMarketCap and save it as CSV.

## Structure
- `src/scraper.py`: Main scraping script
- `data/`: Output CSVs
- `logs/`: Log file for errors
- `.gitignore`: Ignore cache, logs, CSVs, and environment files

## Usage
1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 pandas lxml
   ```
2. Run the scraper:
   ```bash
   python src/scraper.py
   ```
