import json
import time

h ={'Content-Type': 'application/json'}

def newIssue (proj, summ, issueType):
    forCreate ={
                    "fields": {
                        "project": {
                            "key": proj
                        },
                        "summary": summ,
                        "description": "Creating of an issue project keys and issue type names using the REST API",
                        "issuetype": {
                            "name": issueType
                        }
                    }
                }
    return json.dumps(forCreate, indent=4)


def updateSumm (summ):
    forCreate= {
                    "fields": {
                        "summary": summ
                    }
                }
    return json.dumps(forCreate, indent=4)


def updatePriority (priority):
    forCreate={
                    "fields": {
                        "priority": {
                            "name": priority
                        }
                    }
                }
    return json.dumps(forCreate, indent=4)



def generate_summary():
    return time.strftime("_%Y%m%d_%M%S")