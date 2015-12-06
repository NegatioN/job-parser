from bs4 import BeautifulSoup
import requests
import argparse
import spider

##if url is in elastic, dont add.

def main():
    ##args = vars(parser.parse_args())
    ##download_soup(args['url']

    links = spider.spider_finn("http://www.finn.no/finn/job/fulltime/result?sort=0&INDUSTRY=2&keyword=english&location=1%2F20001%2F20061")

    for link in links:
        print(link)







if __name__ == "__main__":
   ## parser = argparse.ArgumentParser("Parses a site and outputs json-objects.")
   ## parser.add_argument('-u','--url', help='url for parsing', required=True)
    main()

