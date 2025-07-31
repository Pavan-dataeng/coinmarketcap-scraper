import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Main scraping script for CoinMarketCap

if __name__ == "__main__":
    print("Starting CoinMarketCap scraper...")

    url = 'https://coinmarketcap.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    # Find the main table and extract the top 10 rows
    table = soup.find('table')
    if not table:
        print('Could not find the main table on CoinMarketCap.')
        exit(1)
    tbody = table.find('tbody')
    rows = tbody.find_all('tr', limit=10) if tbody else []

    data = []
    for row in rows:
        try:
            cols = row.find_all('td')
            # Defensive: check enough columns
            if len(cols) < 8:
                continue
            name = cols[2].find('p', attrs={'color': 'text'})
            name = name.text if name else cols[2].find('a').text
            symbol = cols[2].find_all('p')[-1].text
            price = cols[3].text.strip()
            market_cap = cols[7].text.strip()
            volume_24h = cols[8].text.strip() if len(cols) > 8 else ''

            data.append({
                'Name': name,
                'Symbol': symbol,
                'Price': price,
                'Market Cap': market_cap,
                '24h Volume': volume_24h
            })
        except Exception as e:
            print(f"Error extracting data: {e}")

    df = pd.DataFrame(data)
    df.to_csv('coinmarketcap_top10.csv', index=False)
    print(df.head())
