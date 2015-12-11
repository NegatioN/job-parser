from elasticsearch import Elasticsearch
import requests
from time import sleep
'''
def sendJson(json_strings):
    es = Elasticsearch([{'host': '104.155.89.25', 'port': 9200}])
    for counter, string in enumerate(json_strings):
        print(string)
        print(es.index(index="finn", doc_type="job", body=string))

        '''''

def sendJson(json_strings):
    for counter, string in enumerate(json_strings):
        r = requests.post('http://104.155.89.25:5514', string)
        print("STATUS=" + str(r.status_code))
        sleep(0.2)


def sendValue(idLink, body):
    ##print("Link=" + idLink +"\nBody=" + body)
    es = Elasticsearch([{'host': '104.155.89.25', 'port': 9200}])
    print(es.index(index="finn2", doc_type="string", id=idLink, body=body))


def testEs():
    es = Elasticsearch([{'host': '104.155.89.25', 'port': 9200}])
    return es.search(index="logstash-2015.12.10", body={  "query": { "match_all": {} },"_source": ["document", "url"]})

