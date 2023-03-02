from bs4 import BeautifulSoup
from lxml import etree
import requests

URL = "https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of"
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
  
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")



dom = etree.HTML(str(soup))
print(dom.xpath('//*[@class="CmkY1Ag0tJDfnFXbGgju"]/img/@src'))