import json

def getdata(name):
    try:
        return json.load(open(name))['_state']['favorites']
    except Exception as e:
        print(e)
        return None

def removeduplicates(dict):
    final = []
    for key in dict:
        if(key not in final):
            final.append(key)

    return {"_state":{"favorites":final,"timesFavorited":len(final)},"_version":2}

def parse(name):
    text = getdata(name)
    if text != None:
        return removeduplicates(text)
    else:
        print('An exception has occurred, please see the error listed above.')

def validate(data):
    try:
        # catch all bad conditions and return false, return true if not caught
        
        # if the top level of the json does not have '_state' and '_version' with '_version' equaling 2
        if(not "_state" in data and not "_version" in data):
            return False
        elif(type(data['_version']) != int or data['_version'] != 2):
            return False

        # if '_state' does not contain 'favorites' and 'timesFavorited' with 'favorites' being a list and 'timesFavorited' being a int
        if(not "favorites" in data['_state'] or not "timesFavorited" in data['_state']):
            return False
        elif(type(data['_state']['favorites']) != list):
            return False
        elif(type(data['_state']['timesFavorited']) != int):
            return False
        
        # check that every item in '_state' > 'favorites' is a dict
        for key in data['_state']['favorites']:
            if(type(key) != dict):
                return False

        # default to returning true
        return True
    except:
        return False

def merge(file, data):
    return removeduplicates(data['_state']['favorites'] + getdata(file))