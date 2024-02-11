from bs4 import BeautifulSoup
import requests
url ='https://www.premierleague.com/stats'
response = requests.get(url)

if response.status_code ==200:
    content = response.content
    print("Success getting content")
    print(content)
    BFS = BeautifulSoup(content, 'html.parser')
else:
    print("Fail: Error getting content")


