from bs4 import BeautifulSoup
import requests

date_sort = "1"

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