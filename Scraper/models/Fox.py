from models.Source import Source  # Relative import
import requests
from bs4 import BeautifulSoup
import logging


class Fox(Source):
    #https://www.foxnews.com/category/world/world-regions/israel
    def filter_soup(self, soup):
        #maybe mvoe the classes to a DB and fetch from there, can keep updated and such
        classes = ['article']
        articles = soup.find_all('article', class_=classes)
        links_and_titles = []
        for article in articles:
            link,title = self.get_link_and_title(article)
            links_and_titles.append((link,title))
        return links_and_titles
        
    def store_data(self, data):
        pass

    def get_link_and_title(self, article):
        link = article.find('a').get('href')
        title = article.find('h4').get_text(strip=True)
        return link,title