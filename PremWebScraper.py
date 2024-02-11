from bs4 import BeautifulSoup
import requests
url ='https://www.premierleague.com/stats'
response = requests.get(url)

if response.status_code ==200:
    content = response.content
    print("Success getting content")
    BFS = BeautifulSoup(content, 'html.parser')

    elements = BFS.find_all('div', class_='top-stats__row-stat')
    for element in elements:
        print(element)
else:
    print("Fail: Error getting content")




