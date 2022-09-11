# this was buitl following a tech with time video found at https://www.youtube.com/watch?v=gRLHr664tXA
from platform import python_branch
from bs4 import BeautifulSoup as bs
import requests as r 

URL = "https://pythonjobs.github.io/"
page = r.get(URL)

soup = bs(page.text, "html.parser")
# print(soup.prettify())

tags = soup.find(["section"], class_ = "job_list" )

for tag in tags:
    print(tag) 



# print(tags.prettify())

# title = tags.find_all(["h1"], class_ ="go-button" )







# print(tags)