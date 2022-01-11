#Web scrape the UW news website
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://uwaterloo.ca/news/home').text
soup = BeautifulSoup(html_text, 'lxml')

#Find most recent news articles on the website
news = soup.find_all('div', class_ = 'entity entity-paragraphs-item paragraphs-item-featured-stories')

#Create a boolean for when to show the news
show_news = False

for article in (news):
   #Find the title of the article
   title = article.h2.text.upper()

   #Key words concerning the pandemic
   if 'COVID' in title:
       show_news = True
   elif 'VACCINE' in title:
       show_news = True
   elif 'PANDEMIC' in title:
       show_news = True
   elif 'OMICRON' in title:
       show_news = True
   elif 'CORONAVIRUS' in title:
       show_news = True

   #If key words show up in the title show the news
   if show_news:
       #Find the date, blurb, and link to the article
       date = article.find('span', class_ = 'article-date').text
       about = article.p.text
       link = article.a['href']

       #Output key info
       print(title)
       print(f'Date: {date}')
       print(f'About: {about}')
       print(f'Read more: https://uwaterloo.ca{link}')
       print('')
       show_news = False

#If key words are not in any of the recent news articles, output a message
if not show_news:
   print('There is no recent UW news concerning COVID-19')

print('')
print('See other UW news articles at: https://uwaterloo.ca/news/home')
