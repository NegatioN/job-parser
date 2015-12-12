import requests
from time import sleep
from elasticsearch import Elasticsearch
import json

elasticsearchHost = "104.155.89.25"

def sendJson(job_objects):
    for counter, job in enumerate(job_objects):
        r = requests.post('http://' + elasticsearchHost + ':5514', str(job))
        print("STATUS=" + str(r.status_code))
        sleep(0.2)


def aggregatedInElasticsearch(url):
    es = Elasticsearch(elasticsearchHost+":9200")
    es_dict_response = es.search(index="_all", body={
    "query" : {
        "match" : { "url" : {
            "query" : url,
            "cutoff_frequency" : 0.0001
        }}}})
    return es_dict_response["hits"]["total"] == 0



