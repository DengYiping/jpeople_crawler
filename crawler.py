import requester
from string import ascii_lowercase
from pymongo import MongoClient
import time

def existed(userinfo, collection):
    if collection.find({"eid": userinfo["eid"]}).count() > 0:
        return True
    else:
        return False

def main_func():
    # connect to the database
    client = MongoClient('mongodb://localhost:27017/')
    db = client.jacobs
    collection = db.jpeople
    for c in ascii_lowercase:
        # time.sleep(2)
        print("crawling under alphabet: {}".format(c))
        results = requester.searchName(c)["results"]
        print("results size: {}".format(len(results)))
        for result in results:
            if not existed(result, collection):
                print("inserting {} {}".format(result['firstName'], result['lastName']))
                collection.insert_one(result)

if __name__ == '__main__':
    main_func()