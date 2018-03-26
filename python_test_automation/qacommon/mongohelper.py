# coding=utf-8
import pymongo
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + ".."))
import config


cf = config.get_config()
mongoclient = None

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
    

class MongoKeeper(Singleton):
    def __init__(self):
        global mongoclient
        if not mongoclient:
            mongoclient = pymongo.MongoClient(cf['mongodb']['live_answer_uri'])
            self.db = mongoclient.dbname
            
    def print_items(self):
        coll = self.db.collectionname
        for item in coll.find():
            print item
        
    def __del__(self):
        if mongoclient:
            mongoclient.close()

if __name__ == "__main__":
    MongoKeeper().print_items()