"""Get all <article> tags on New York Times homepage"""

import requests
from bs4 import BeautifulSoup

def get_articles(address):
	page = requests.get(address)
	soup = BeautifulSoup(page.text, "html.parser")
	return list(soup.find_all("article"))
		
if __name__ == "__main__":
	print get_articles("http://www.nytimes.com/")

