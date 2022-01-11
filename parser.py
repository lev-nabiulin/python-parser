import requests
from bs4 import BeautifulSoup as bs


URL_TEMPLATE = "https://www.python.org/"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
blocks = soup.find_all("div", class_="shrubbery")
for block in blocks:
    title = block.find("h2", class_="widget-title").get_text()
    if title == "Upcoming Events":
        print(title)
        events = block.find_all("li")
        for event in events:
            print(event.find("time").text, event.find("a").text)