import argparse
from parsers import finn_parser, indeed_parser
import elastic_handler
from time import sleep

##if url is in elastic, dont add.

def main():
    ##args = vars(parser.parse_args())
    ##download_soup(args['url']

    url = "http://no.indeed.com/jobs?q=bank&l=Oslo"
    jobs_collection = []

    if "finn" in url:
        links = finn_parser.spider_finn(url)
        for link in links:
            sleep(0.15)
            link = trimFinnLink(link)
            print(link)
            jobs_collection.append(finn_parser.parse_finn_job(link))

    elif "indeed" in url:
        links = indeed_parser.spider_indeed(url)
        for link in links:
            sleep(0.15)
            print(link)
            job_object = indeed_parser.parse_indeed_job(link)
            if job_object != None:
                jobs_collection.append(job_object)

    elastic_handler.sendJson(jobs_collection)




##cut "POLE-position etc" from top link.
def trimFinnLink(link):
    return link.split('&ecType')[0]



if __name__ == "__main__":
   ## parser = argparse.ArgumentParser("Parses a site and outputs json-objects.")
   ## parser.add_argument('-u','--url', help='url for parsing', required=True)
    main()

