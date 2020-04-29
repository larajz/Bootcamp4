import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.mass.gov/info-details/covid-19-response-reporting#covid-19-cases-in-massachusetts-")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_ = "ma__table--responsive__wrapper")
cases = list(table.children)[1]
print(cases.get_text())
