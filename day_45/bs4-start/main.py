from bs4 import BeautifulSoup

with open('./day_45/bs4-start/website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')

# a_tags = soup.find_all(name='a')

# for tag in a_tags:
#     print(tag.getText())