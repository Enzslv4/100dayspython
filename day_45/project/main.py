import requests
from bs4 import BeautifulSoup

movies_link = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url=movies_link)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

titles = soup.find_all(name='h3', class_='title')
titles_list = [title.getText() for title in titles]

titles_list = titles_list[::-1]

with open('day_45/project/movies.txt', mode='w', encoding="utf-8") as file:
    for movie in titles_list:
        file.write(f'{movie}\n')