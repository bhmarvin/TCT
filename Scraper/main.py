from models.CNN import CNN
from models.Fox import Fox
from models.AP import AP
from models.BBC import BBC
import requests
"""
cnn_test = CNN('CNN', 'https://www.cnn.com/', 'https://www.cnn.com/world/middleeast/israel')
data = cnn_test.fetch_soup()
links_and_titles = cnn_test.filter_soup(data)
fox_test = Fox('Fox', 'https://www.foxnews.com/', 'https://www.foxnews.com/category/world/world-regions/israel')
data = fox_test.fetch_soup()
links_and_titles = fox_test.filter_soup(data)
AP_test = AP('AP', 'https://apnews.com/', 'https://apnews.com/hub/israel-hamas-war')
data = AP_test.fetch_soup()
links_and_titles = AP_test.filter_soup(data)"""
BBC_test = BBC('BBC', 'https://bbc.com/', 'https://www.bbc.com/news/topics/c2vdnvdg6xxt')
data = BBC_test.fetch_soup()
links_and_titles = BBC_test.filter_soup(data)
print(links_and_titles)
#https://www.theguardian.com/world/israel-hamas-war
#Adding dates to link/titles is an issue