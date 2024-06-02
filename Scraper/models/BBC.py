from models.Source import Source  # Relative import
import requests
from bs4 import BeautifulSoup


class BBC(Source):
    def filter_soup(self, soup):
        a_divs = soup.find_all('a', attrs={"data-testid":'internal-link'})
        links_and_titles = []
        for div in a_divs:
            if self.is_article(div):
                link,title = self.get_link_and_title(div)
                links_and_titles.append((link,title))
        return links_and_titles
        
    def store_data(self, data):
        pass

    def get_link_and_title(self, article):
        link = article.get('href')
        title = article.find('h2', attrs={"data-testid":'card-headline'}).get_text()
        return link,title
    
    def is_article(self,article):
        title = article.find('h2', attrs={"data-testid":'card-headline'})
        return title is not None
