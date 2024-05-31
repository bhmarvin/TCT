from models.CNN import CNN
import requests

cnn_test = CNN('CNN', 'https://www.cnn.com/', 'https://www.cnn.com/world/middleeast/israel')
data = cnn_test.fetch_soup()
links_and_titles = cnn_test.filter_soup(data)
for link_and_title in links_and_titles:
    print(link_and_title)
