import urllib.request as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver

page = req.urlopen('https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API')
soup = bs(page)

# title = soup.body.find_all('h1')

title = soup.body.find('h1')

# subtitle = soup.find(id="fetch_interfaces")

subtitles = soup.find_all("h2")

for subtitle in subtitles:
  print(subtitle.text)

# tables = soup.find_all("table")

# print(subtitles)
