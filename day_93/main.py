import requests
from bs4 import BeautifulSoup
import csv

def scrape_steam_games():
    url = "https://store.steampowered.com/search/?filter=topsellers"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    games = []
    
    for game in soup.select(".search_result_row"):
        title = game.select_one(".title").text
        price_element = game.select_one(".search_price")
        price = price_element.text.strip() if price_element else "Free or Unavailable"
        link = game["href"]
        
        games.append([title, price, link])
    
    with open("steam_games.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Link"])
        writer.writerows(games)
    
    print("Scraped data saved to steam_games.csv")

scrape_steam_games()