from bs4 import BeautifulSoup
import requests
from job_objects import job_object as jo

date_sort = "date"

def parse_indeed_job(url):
    try:
        soup = download_soup(url)
        page_content = soup.find("body")
        if page_content == None:
            print("Error has occured. Cannot parse")
            return None
        job_title = page_content.find("b", {"class" : "jobtitle"})
        description = page_content.find("span", {"id" : "job_summary"})
        company = page_content.find("span", {"class" : "company"})
        location = page_content.find("span", {"class" : "location"})
        if job_title == None or company == None or location == None or description == None or len(description.text) < 25:
            print("Error has occured. Cannot parse")
            return None
        document = job_title.text + "\n" + company.text + "\n" + description.text
        return jo.Job(url, document, title=job_title.text, location=location.text, company=company.text)
    except:
        return None



def spider_indeed(url):
    job_index = 0
    urls = []
    urls.append(url + "&start=" + str(job_index) + "&sort=" + date_sort)
    while page_has_next(url + "&start=" + str(job_index) + "&sort=" + date_sort):
        print(job_index)
        job_index+=10
        urls.append(url + "&start=" + str(job_index) + "&sort=" + date_sort)


    job_links = []
    for job_page in urls:
        job_links.extend(get_indeed_jobs(download_soup(job_page)))

    return job_links


def get_indeed_jobs(list_page_soup):
    job_links = []
    job_objects = list_page_soup.findAll("h2", { "class" : "jobtitle" })

    for job in job_objects:
        href = job.find('a')['href']
        job_links.append(href.replace("/rc/clk", "http://no.indeed.com/viewjob"))

    return job_links

def download_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")

##returns true if the finn_page has a next-button in it.
def page_has_next(url):
    soup = download_soup(url)
    buttons = soup.findAll("span", { "class" : "np" })
    for pagination_button in buttons:
        if "Neste" in pagination_button.text:
            return True

    return False