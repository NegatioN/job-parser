import argparse
import spider
import parse
import elastic_handler
from time import sleep

##if url is in elastic, dont add.

def main():
    ##args = vars(parser.parse_args())
    ##download_soup(args['url']

    links = spider.spider_finn("http://www.finn.no/finn/job/fulltime/result?sort=0&INDUSTRY=2&keyword=english&location=1%2F20001%2F20061")

    jobs_collection = []
    for link in links:
        sleep(0.15)
        link = trimFinnLink(link)
        print(link)
        jobs_collection.append(parse.parse_finn_job(link))

    elastic_handler.sendJson(jobs_collection)


##cut "POLE-position etc" from top link.
def trimFinnLink(link):
    return link.split('&ecType')[0]



if __name__ == "__main__":
   ## parser = argparse.ArgumentParser("Parses a site and outputs json-objects.")
   ## parser.add_argument('-u','--url', help='url for parsing', required=True)
    main()

