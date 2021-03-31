import sys,os,yaml,time
from pymongo import MongoClient, errors,ASCENDING

class common:
    def load_master_config():
        try:
            with open('config.yaml') as ymlfile:      
                cfg = yaml.load(ymlfile,yaml.FullLoader)
                return cfg
        except Exception as e:
            print("Unable to open Config File -  Exitting")
            exit()

    def connect_to_mongo():
        try:
            for url in cfg['mongo_url_list']:
                client = MongoClient(url)
                if client.is_primary:
                    # log.info("Set Mongo URL to: %s",url)
                    return client
        except Exception as e:
            print("Unable to Connect To Mongo: %s",e)
            sys.exit(1)

    def send_to_db(RepId,payload=None,db=None,name=None):
        """
        Used for inserting a new document OR updating an existing one(i.e. non-Historical data insertion)
        """
        epoch = int(time.time())
        found_doc = common.check_db(RepId,db,name)
        if found_doc:
            query = {"_id":found_doc}
            if payload != None:
                final = {"$set":{"TimeInserted":epoch,name:payload}}
            else:
                final = {"$set":{"TimeInserted":epoch}}
            db.update_one(query, final)
        else:
            # log.debug(payload)
            final = {"RepId":RepId,"TimeInserted":epoch,name:payload}
            db.insert_one(final)

    def check_db(db):
        try:
            for x in db.find().sort('_id',-1).limit(1):
                return x
        except:
            print("Something Happened")
            raise
cfg = common.load_master_config()