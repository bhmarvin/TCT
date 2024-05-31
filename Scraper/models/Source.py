from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
import logging

class Source:
    def __init__(self, name, link_prefix, scrape_url):
        self.name = name
        self.link_prefix = link_prefix
        self.scrape_url = scrape_url

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
    
    @abstractmethod
    def filter_soup(self, data):
        pass
    
    @abstractmethod
    def store_data(self, data):
        pass
    
    
