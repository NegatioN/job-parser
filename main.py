import argparse
from parsers import finn_parser, indeed_parser
import elastic_handler
from time import sleep

sleepVar = 0.15

def main():
    args = vars(parser.parse_args())
    try:
        elastiHandler = elastic_handler.ElasticHandler(args["host"])
    except:
        return

    url = args["url"]
    jobs_collection = []

    if "finn" in url:
        links = finn_parser.spider_finn(url)
        for link in links:
            sleep(sleepVar)
            link = trimFinnLink(link)
            print(link)
            if elastiHandler.aggregatedInElasticsearch(link):
                continue
            jobs_collection.append(finn_parser.parse_finn_job(link))

    elif "indeed" in url:
        links = indeed_parser.spider_indeed(url)
        for link in links:
            sleep(sleepVar)
            print(link)
            if elastiHandler.aggregatedInElasticsearch(link):
                continue
            job_object = indeed_parser.parse_indeed_job(link)
            if job_object != None:
                jobs_collection.append(job_object)

    if len(jobs_collection) > 0:
        elastiHandler.sendJson(jobs_collection)




##cut "POLE-position etc" from top link.
def trimFinnLink(link):
    return link.split('&ecType')[0]



if __name__ == "__main__":
    parser = argparse.ArgumentParser("Parses a site and outputs json-objects.")
    parser.add_argument('-u','--url', help='url for parsing', required=True)
    parser.add_argument('-ho','--host', help='host without ports for elasticsearch-host', required=True)
    main()

