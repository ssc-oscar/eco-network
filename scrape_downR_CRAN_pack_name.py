# scrape down the R CRAN PACKAGE list:
from bs4 import BeautifulSoup
import requests

r = requests.get(
    'https://cran.r-project.org/web/packages/available_packages_by_name.html')
t = r.text.encode('utf-8')
soup = BeautifulSoup(t, 'html.parser')
for row in soup.body.table.findAll('tr'):
    cols = row.findAll('td')
    if len(cols) == 0:
        continue
    # print(len(cols))
    # print(cols)
    a = cols[0].find('a')
    if a:
        print(a.contents[0])
