from models.Source import Source  # Relative import
import requests
from bs4 import BeautifulSoup
import logging


class CNN(Source):

    def filter_soup(self, soup):
        #maybe mvoe the classes to a DB and fetch from there, can keep updated and such
        classes = ['card container__item container__item--type-media-image container__item--type-section container_list-headlines-with-images__item container_list-headlines-with-images__item--type-section',
                   'card container__item container__item--type-media-image container__item--type-section container_lead-plus-headlines-with-images__item container_lead-plus-headlines-with-images__item--type-section'
                   ]
        articles = soup.find_all('div', class_=classes)
        links_and_titles = []
        for article in articles:
            link,title = self.get_link_and_title(article)
            links_and_titles.append((link,title))
        return links_and_titles
        
    def store_data(self, data):
        pass

    def get_link_and_title(self, article):
        link = article.find('a').get('href')
        title = article.find('span',class_='container__headline-text').get_text(strip=True)
        return link,title