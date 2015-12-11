import json
from _datetime import datetime

class Job():
    def __init__(self, url, document, deadline=None, company=None, location=None, title=None):
        self.title = title
        self.document = document
        self.url = url
        self.deadline = deadline
        self.company = company
        self.location = location
        self.date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


    def __str__(self, *args, **kwargs):
        outputDict = {}
        if self.url != None:
            outputDict["url"] = self.url
        if self.title != None:
            outputDict["title"] = self.title
        if self.document != None:
            outputDict["document"] = self.document
        if self.deadline != None:
            outputDict["deadline"] = self.deadline
        if self.company != None:
            outputDict["company"] = self.company
        if self.location != None:
            outputDict["location"] = self.location
        outputDict["date"] = self.date


        return json.dumps(outputDict)

