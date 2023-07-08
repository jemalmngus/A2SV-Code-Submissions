from bs4 import BeautifulSoup
import requests

# Make an HTTP GET request
response = requests.get('https://www.familysooq.com')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title
title = soup.find_all('a')

# Print the title
print(soup.get_text())

x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)