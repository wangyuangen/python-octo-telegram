#--encoding:utf-8-- #

import urllib2
from bs4 import BeautifulSoup
url = "https://cn.bing.com/"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page,'html.parser')
value = soup.find('div',attrs={'id':'bgDiv'})
print value.text