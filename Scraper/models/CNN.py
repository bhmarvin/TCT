from models.Source import Source  # Relative import
import requests
from bs4 import BeautifulSoup
import logging


class CNN(Source):
    #https://www.cnn.com/middleeast/live-news/israel-hamas-war-gaza-news-05-30-24/index.html
    #seems to be the URL
    #https://www.cnn.com/world/middleeast/israel another URL, the main one
    # a with class container__link
    def fetch_soup(self):
        try:
            response = requests.get(self.scrape_url)
            response.raise_for_status()  # Raise for bad status codes
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None
        except Exception as e:  # This block will only catch unexpected errors
            logging.error(f"An unexpected error occurred: {e}")
            return None

    def filter_soup(self, soup):
        #card container__item container__item--type-media-image container__item--type-section container_list-headlines-with-images__item container_list-headlines-with-images__item--type-section  
        #card container__item container__item--type-media-image container__item--type-section container_lead-plus-headlines-with-images__item container_lead-plus-headlines-with-images__item--type-section 
        #THE TWO CLASSES I NEED TO GET DIVS OF TO GET LINKS/TITLES TOGETHER 
        pass


        
    def store_data(self, data):
        pass