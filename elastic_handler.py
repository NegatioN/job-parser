import requests
from time import sleep
from elasticsearch import Elasticsearch


class ElasticHandler():
    def __init__(self, host):
        self.elasticsearchHost = host

    def sendJson(self, job_objects):
        for counter, job in enumerate(job_objects):
            r = requests.post('http://' + self.elasticsearchHost + ':5514', str(job))
            print("STATUS=" + str(r.status_code))
            sleep(0.2)


    def aggregatedInElasticsearch(self, url):
        es = Elasticsearch(self.elasticsearchHost+":9200")
        es_dict_response = es.search(index="_all", body={
        "query" : {
            "match" : { "url" : {
                "query" : url,
                "cutoff_frequency" : 0.0001
            }}}})
        return es_dict_response["hits"]["total"] != 0



