from abc import ABC, abstractmethod

class Source:
    def __init__(self, name, link_prefix, scrape_url):
        self.name = name
        self.link_prefix = link_prefix
        self.scrape_url = scrape_url

    @abstractmethod
    def fetch_soup(self):
        pass
    
    @abstractmethod
    def filter_soup(self, data):
        pass
    
    @abstractmethod
    def store_data(self, data):
        pass
    
    
