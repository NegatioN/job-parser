from bs4 import BeautifulSoup
import requests
from job_objects import job_object as jo


def parse_finn_job(url):
    soup = download_soup(url)
    page_content = soup.find("div", { "id" : "ObjectContent" })
    if page_content == None:
        print("Error has occured. Cannot parse")
        return (url, None)
    ingress = page_content.find("div", {"class" : "ingress"})
    body = page_content.find("div", {"id" : "description"})
    heading = page_content.find("header")
    deadline = page_content.find("dd", {"data-automation-id" : "application-deadline"})
    if deadline == None or deadline.text == "Snarest":
        deadline == None
    if heading == None or body == None or ingress == None:
        return print("Error has occured. Cannot parse")
    document = ingress.text + "\n" + heading.text + "\n" + body.text
    if deadline == None:
        return jo.Job(url, document)
    else:
        return jo.Job(url, document, deadline=deadline.text.replace("\"", "").strip())



def download_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")
