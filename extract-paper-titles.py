with open('pldi2024.html', 'r') as f:
  html_doc = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

for strong in soup.find_all('strong'):
    print(strong.get_text())
