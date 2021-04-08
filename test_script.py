import sys, os,yaml,requests,json,argparse,time
from pycloudbasic import replicationManagement as rm
from pycloudbasic import systemWideManagement as swm
# from py_cloudbasic.replicationManagement import replicationManagement as rm
from common import common as c
cfg = c.load_master_config()

client = c.connect_to_mongo()
cbdb = client.cloudbasic
repList = cbdb.replication_list
latCol = cbdb.latency
curTime = int(time.time())
def main(command_line=None):
    host = cfg['host'] + ":" + cfg['httpPort']
    hostUri = 'http://' + host
    helpText = "Runs API calls against the CloudBasic server"

    #Initiate the parser
    parser = argparse.ArgumentParser('CloudBasic API Tool)',description = helpText)
    subparsers = parser.add_subparsers(dest='api')

    getList = subparsers.add_parser("getList", help="Retrieves the entire list of Replications")
    
    mongoLatest = subparsers.add_parser("MongoLatest", help="Retrieves the latest Replication List from Mongo, if enabled")
    
    repStatus = subparsers.add_parser("repStatus",help="Pulls the status of the given replication ID")
    repStatus.add_argument("-id",'--repId',dest='repId')
    
    latency = subparsers.add_parser("getLatency",help="Pulls the latency of the given Rep ID in Hours")
    latency.add_argument('-id','--repId',dest='repId')
    latency.add_argument('-hrs','--hours',dest='hours',default='48',help="The period of time in hours that you would like average latency to be calculated for: default=48 ")
    
    latencyall = subparsers.add_parser("getLatencyAll",help="Pulls a GetReplicationList, then iterates over each RepID and pulls the latency for each")
    latencyall.add_argument('-hrs','--hours',dest='hours',default='48',help="The period of time in hours that you would like average latency to be calculated for: default=48 ")

    getLogs = subparsers.add_parser("getLogs",help="Pulls the logs of the given replication ID")
    getLogs.add_argument("-id",'--repId',dest='repId')

    repSerStat = subparsers.add_parser("repServiceStatus",help="ReplicationServiceStatus - Retrieves the Status of the ReplicationService process.")

    try:
        args = parser.parse_args(command_line)
    except Exception as e:
        print(e)

    
    if args.api == "getList":
        request_parameters =  '{"replicationId":""}'
        action = "/api/GetReplicationsList"
        endpoint = hostUri + action

        list = rm.repMan.getReplicationsList(rm.repMan(host,action,request_parameters),endpoint)
        if cfg['mongo'] == True:
            print("writing to mongo")
            repList.insert_one(list)
        else:
            with open("ReplicationsList.json",'w+') as outFile:
                json.dump(list,outFile, ensure_ascii=False, indent=4)
            
    elif args.api == "mongoLatest":
        if cfg['mongo'] == True:
            found_doc = c.check_db(repList)
            print(found_doc)
        else:
            print("Mongo Not Enabled, ignoring")
    
    elif args.api == "repServiceStatus":
        action = "/api/ReplicationServiceStatus"
        endpoint = hostUri + action
        request_parameters = ''
        method = 'GET'
        response = swm.sysMan.ReplicationServiceStatus(swm.sysMan(host,action,request_parameters,method),endpoint)
        print(response)

    elif args.api == "repStatus":
        repId = args.repId
        action = "/api/ReplicationStatus"
        endpoint = hostUri + action
        request_parameters =  '{"Id":"'+ repId + '"}'
        
        response = rm.repMan.replicationStatus(rm.repMan(host,action,request_parameters),endpoint)
        
        print(response)

    elif args.api == "getLogs":
        repId = args.repId
        action = "/api/GetLogs"
        endpoint = hostUri + action
        request_parameters =  '{"Id":"'+ repId + '"}'
        response = rm.repMan.getLogs(rm.repMan(host,action,request_parameters),endpoint)
        with open("Logs_"+ repId + ".json",'w+') as outFile:
            json.dump(response,outFile, ensure_ascii=False, indent=4)

    elif args.api == "getLatency":
        repId = args.repId
        hours = args.hours
        action = "/api/GetLatency"
        endpoint = hostUri + action
        
        request_parameters =  '{"replicationId":"'+repId + '","Period":' + hours + '}'
        response = rm.repMan.getLatency(rm.repMan(host,action,request_parameters),endpoint)
        print(response)

    elif args.api == "getLatencyAll":
        request_parameters =  '{"replicationId":""}'
        action = "/api/GetReplicationsList"
        endpoint = hostUri + action

        list = rm.repMan.getReplicationsList(rm.repMan(host,action,request_parameters),endpoint)

        hours = args.hours
        action = "/api/GetLatency"
        endpoint = hostUri + action
        latencyList = []
        for x in list["replications"]:
            repId = x["replicationId"]
            request_parameters =  '{"replicationId":"'+repId + '","Period":' + hours + '}'
            response = rm.repMan.getLatency(rm.repMan(host,action,request_parameters),endpoint)
            latencyList.append(response)
        print(latencyList)
        if cfg['mongo'] == True:
            print("writing to mongo")
            latCol.insert_many(latencyList)
        else:
            with open("LatencyList_" +str(curTime) + ".json",'w+') as outFile:
                json.dump(latencyList,outFile, ensure_ascii=False, indent=4)
    

if __name__ == "__main__":
    main()