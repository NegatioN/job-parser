from bs4 import BeautifulSoup
import requests
from job_objects import job_object as jo

date_sort = "1"


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


def spider_finn(url):
    page = 1
    urls = []
    while page_has_next(url + "&page=" + str(page) + "&sort=" + date_sort):
        urls.append(url + "&page=" + str(page) + "&sort=" + date_sort)
        page+=1

    job_links = []
    for job_page in urls:
        job_links.extend(get_finn_jobs(download_soup(job_page)))

    return job_links


def get_finn_jobs(list_page_soup):
    job_links = []
    job_objects = list_page_soup.findAll("div", { "class" : "jobobject" })

    for job in job_objects:
        job_links.append(job.find('a')['href'])

    return job_links


def download_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")

##returns true if the finn_page has a next-button in it.
def page_has_next(url):
    soup = download_soup(url)
    return soup.find("a", { "class" : "lastItem" }) != None