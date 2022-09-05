# Web scrape the UW news website
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://uwaterloo.ca/news/home').text
soup = BeautifulSoup(html_text, 'lxml')

# Find most recent news articles on the website
news = soup.find_all('div', class_='uw_ct_story')

# Create a boolean for when to show the news
show_news = False

for article in news:
    # Find the title of the article
    title = article.h2.text.upper()

    # Key words concerning the pandemic
    key_words = ['COVID', 'VACCINE', 'PANDEMIC', 'OMICRON', 'CORONAVIRUS']
    for key_word in key_words:
        if key_word in title:
            show_news = True
            break

    # If a key word shows up in the title, show the news article
    if show_news:
        # Find the date, blurb, and link to the article
        date = article.find('span', class_='article-date').text
        about = article.p.text
        link = article.a['href']

        # Output key info
        print('')
        print(title)
        print(f'Date: {date}')
        print(f'About: {about}')
        print(f'Read more: https://uwaterloo.ca{link}')
        print('')
        show_news = False
        printed_news = True

# If key words are not in any of the recent news articles, output a message
if not printed_news:
    print('\nThere is no recent UW news concerning COVID-19\n')

print('See other UW news articles at: https://uwaterloo.ca/news/home')
print('')
