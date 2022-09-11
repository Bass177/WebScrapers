from platform import python_branch
import requests as r 
from bs4 import BeautifulSoup as bs 


URL = "https://pythonjobs.github.io/"
page = r.get(URL)

soup = bs(page.content, "html.parser")

results = soup.find_all(id = "main")


# print(results.prettify)

# finds all html for all job listings on page 

job_elements = results.find_all("div", class_="col")
print(job_elements)

# looking at all the job_element(s) in job elements
# for job_element in job_elements:
#     print(job_element, end="\n"*2)


# targeting child elements (like h2, h3) using class
# for job_element in job_elements:
#     title_element = job_element.find("a", href_="")
#     company_element = job_element.find("span", class_="i-company")
#     location_element = job_element.find("span", class_="i-globe")
#     # added .text and .strip() to extract pure text from html and then strip whitespace
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
# python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
# print((python_jobs))

# python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# )

# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs

# ]


# for job_element in python_job_elements:
#     # -- snip --
#     links = job_element.find_all("a")
#     for link in links:
#         link_url = link["href"]
#         print(f"Apply here: {link_url}\n")




