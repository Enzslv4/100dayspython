import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')
scores = soup.find_all(name='span', class_='score')

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get('href')
    # print(article_tag, '\n')
    article_links.append(link)

articles_upvotes = [int(score.getText().split()[0]) for score in scores]

# print(article_texts[0])
# print(article_links[0])
# print(articles_upvotes[0])

highest_score = max(articles_upvotes)
score_index = articles_upvotes.index(highest_score)

print(f'The article with the highest score:\n{article_texts[score_index]}\nLink to the article: {article_links[score_index]}\nNumbers of votes: {articles_upvotes[score_index]}')