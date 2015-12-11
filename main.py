import argparse
import spider
import parse
import json
from _datetime import datetime
import elastic_handler
from time import sleep

##if url is in elastic, dont add.

def main():
    ##args = vars(parser.parse_args())
    ##download_soup(args['url']

    links = spider.spider_finn("http://www.finn.no/finn/job/fulltime/result?sort=0&INDUSTRY=2&keyword=english&location=1%2F20001%2F20061")

    content_tuples = []
    for link in links:
        sleep(0.15)
        link = trimFinnLink(link)
        print(link)
        content_tuples.append(parse.parse_finn_job(link))

    json_strings = jsonifyTuples(content_tuples)
    elastic_handler.sendJson(json_strings)





##cut "POLE-position etc" from top link.
def trimFinnLink(link):
    return link.split('&ecType')[0]

def jsonifyTuples(content_tuples):
    json_strings = []
    for urlDoc in content_tuples:
        if urlDoc == None or urlDoc[1] == None:
            continue
        tupleDict = {
            "url" : urlDoc[0],
            "document":urlDoc[1],
            "date":datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "deadline":urlDoc[2]
        }
        output = json.dumps(tupleDict)
        print(output)
        json_strings.append(output)
    return json_strings


def sendTuples(content_tuples):

    for urlDoc in content_tuples:
        if urlDoc == None:
            continue
        if urlDoc[1] == None:
            continue
        elastic_handler.sendValue(urlDoc[0], urlDoc[1])


def sendJsonToElastic(json_array):
    return





if __name__ == "__main__":
   ## parser = argparse.ArgumentParser("Parses a site and outputs json-objects.")
   ## parser.add_argument('-u','--url', help='url for parsing', required=True)
    main()

