from bs4 import BeautifulSoup
import requests
import tkinter as tk
url ='https://www.premierleague.com/stats'
response = requests.get(url)

if response.status_code ==200:
    content = response.content
    print("Success getting content")
    BFS = BeautifulSoup(content, 'html.parser')

    elements = BFS.find_all('div', class_='top-stats__row-stat')
    window = tk.Tk()
    for element in elements:
        text =tk.Text(window)
        text.insert(tk.END, element)
        text.pack()
        print(element)


    window.mainloop()
else:
    print("Fail: Error getting content")




