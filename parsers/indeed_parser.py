from bs4 import BeautifulSoup
import requests
from job_objects import job_object as jo

def parse_indeed_job(url):
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
        return print("Error has occured. Cannot parse")
    document = job_title.text + "\n" + company.text + "\n" + description.text
    return jo.Job(url, document, title=job_title.text, location=location.text, company=company.text)

def download_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")