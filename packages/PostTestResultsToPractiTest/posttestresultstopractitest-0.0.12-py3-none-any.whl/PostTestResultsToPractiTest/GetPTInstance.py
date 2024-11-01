import json,ast
from PostTestResultsToPractiTest import PT_APIRequest
from PostTestResultsToPractiTest import GetConfigValues
from PostTestResultsToPractiTest import GetPTProjectId
from PostTestResultsToPractiTest import Constants

def RetrieveInstanceId(filterByTestSetId, filterByTestId, bddParams):
    GetConfigValues.GetConfigValues()
    projectId = GetPTProjectId.RetrieveProjectId()
    
    res = PT_APIRequest.getRequest(Constants.PT_API_BASEURL+ "/projects/" + projectId + "/instances.json?set-ids=" + filterByTestSetId)

    if res.status_code == 200:
        allInstances = json.loads(res.content)
        allInstancesData = allInstances['data']
        myInstanceData = list(filter(lambda myData:myData['attributes']['test-id']==int(filterByTestId), allInstancesData))
        if bddParams is not None:
            for instanceData in myInstanceData:
                instanceDataString = str(instanceData)
                if(bddParams.lower() in instanceDataString.lower()):
                    myInstanceData = ast.literal_eval(instanceDataString)
                    myInstanceId = myInstanceData['id']
                    return myInstanceId
        else:
            if len(myInstanceData) != 0:
                myInstanceId = myInstanceData[0]['id']
                return myInstanceId
            else:
                return None
    else:
        raise Exception ("Call to get a list of instances is unsuccessful with status code", res.status_code)
