import urllib.request as req
from bs4 import BeautifulSoup as bs

page = req.urlopen('https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input')
soup = bs(page, features="html.parser")

# tables = soup.find_all('table')
# for table in tables:
#   print(table["class"])

input_types_table = soup.find(class_="standard-table")
# print(input_types_table)

thead = input_types_table.find("thead")
ths = thead.find_all("th")
columns=[]

for th in ths:
  columns.append(th.text)

tbody = input_types_table.find('tbody')
rows_tr = tbody.find_all("tr")

content={
  "type": [],
  "description": []
}

for row_tr in rows_tr:
  tds = row_tr.find_all('td')
  if tds :
    content["type"].append(tds[0].text)
    content["description"].append(tds[1].text)


print(columns)
print(content)

# tr = input_types_table.find_all('tbody')

