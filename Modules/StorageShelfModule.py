#============================================================
#
#
# Copyright (c) 2017 NetApp, Inc. All rights reserved.
# Specifications subject to change without notice.
#
# This sample code is provided AS IS, with no support or
# warranties of any kind, including but not limited to
# warranties of merchantability or fitness of any kind,
# expressed or implied.
#
# Min Python Version = python 2.7
#
#============================================================


#!/usr/bin/python

from ansible.module_utils.basic import *

import requests
import warnings
import sys
import json
import time
warnings.filterwarnings("ignore")


def get():
    url_path        = "/api/2.0/ontap/"

    flag=0

    url_path+="storage-shelfs"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if shelf_model != None:
        if flag is 0:
            url_path+="?shelf_model="+shelf_model
            flag=1
        else:
            url_path+="&shelf_model="+shelf_model
    if shelf != None:
        if flag is 0:
            url_path+="?shelf="+shelf
            flag=1
        else:
            url_path+="&shelf="+shelf
    if shelf_id != None:
        if flag is 0:
            url_path+="?shelf_id="+shelf_id
            flag=1
        else:
            url_path+="&shelf_id="+shelf_id
    if shelf_uid != None:
        if flag is 0:
            url_path+="?shelf_uid="+shelf_uid
            flag=1
        else:
            url_path+="&shelf_uid="+shelf_uid
    if stack_id != None:
        if flag is 0:
            url_path+="?stack_id="+stack_id
            flag=1
        else:
            url_path+="&stack_id="+stack_id
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
    if sortBy != None:
        if flag is 0:
            url_path+="?sortBy="+sortBy
            flag=1
        else:
            url_path+="&sortBy="+sortBy
    if maxRecords != None:
        if flag is 0:
            url_path+="?maxRecords="+maxRecords
            flag=1
        else:
            url_path+="&maxRecords="+maxRecords
    if nextTag != None:
        if flag is 0:
            url_path+="?nextTag="+nextTag
            flag=1
        else:
            url_path+="&nextTag="+nextTag
    response=http_request_for_get(url_path)
    json_response=response.json()
    return json_response

def post():
    url_path        = "/api/2.0/ontap/"
    url_path+="storage-shelfs"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (shelf_model != None) & (shelf_model != key):
        payload['shelf_model']=shelf_model
    if (shelf != None) & (shelf != key):
        payload['shelf']=shelf
    if (shelf_id != None) & (shelf_id != key):
        payload['shelf_id']=shelf_id
    if (shelf_uid != None) & (shelf_uid != key):
        payload['shelf_uid']=shelf_uid
    if (stack_id != None) & (stack_id != key):
        payload['stack_id']=stack_id
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag

    response=http_request_for_post(url_path,**payload)
    json_response=response.headers
    return json_response

def put():
    url_path        = "/api/2.0/ontap/"
    url_path+="storage-shelfs/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (shelf_model != None) & (shelf_model != key):
        payload['shelf_model']=shelf_model
    if (shelf != None) & (shelf != key):
        payload['shelf']=shelf
    if (shelf_id != None) & (shelf_id != key):
        payload['shelf_id']=shelf_id
    if (shelf_uid != None) & (shelf_uid != key):
        payload['shelf_uid']=shelf_uid
    if (stack_id != None) & (stack_id != key):
        payload['stack_id']=stack_id
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag
    if key != None:
        url_path+=key
        response=http_request_for_put(url_path,**payload)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key"

def delete():
    url_path        = "/api/2.0/ontap/"
    url_path+="storage-shelfs/"

    if key != None:
        url_path+=key
        response=http_request_for_delete(url_path)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key for deletion"

def http_request_for_get(url_path,**payload):
	response = requests.get("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_put(url_path,**payload):
	response = requests.put("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_post(url_path,**payload):
	response = requests.post("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_delete(url_path,**payload):
	response = requests.delete("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response



def main():
        fields = {
                "action" : {
                        "required": True,
                        "choices": ['get', 'put', 'post', 'delete'],
                        "type": 'str'
                        },
                "host" : {"required": True, "type": "str"},
                "port" : {"required": True, "type": "str"},
                "user" : {"required": True, "type": "str"},
                "password" : {"required": True, "type": "str"},
                "key" : {"required": False, "type": "str"},
                "shelf_model" : {"required": False, "type": "str"},
                "shelf" : {"required": False, "type": "str"},
                "shelf_id" : {"required": False, "type": "str"},
                "shelf_uid" : {"required": False, "type": "str"},
                "stack_id" : {"required": False, "type": "str"},
                "cluster_key" : {"required": False, "type": "str"},
                "sortBy" : {"required": False, "type": "str"},
                "maxRecords" : {"required": False, "type": "str"},
                "nextTag" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password

        global lun_key
        global nfs_share_key
        global cifs_share_key
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global key
        key = module.params["key"]
        global shelf_model
        shelf_model = module.params["shelf_model"]
        global shelf
        shelf = module.params["shelf"]
        global shelf_id
        shelf_id = module.params["shelf_id"]
        global shelf_uid
        shelf_uid = module.params["shelf_uid"]
        global stack_id
        stack_id = module.params["stack_id"]
        global cluster_key
        cluster_key = module.params["cluster_key"]
        global sortBy
        sortBy = module.params["sortBy"]
        global maxRecords
        maxRecords = module.params["maxRecords"]
        global nextTag
        nextTag = module.params["nextTag"]

        global json_response

        # Actions
        if module.params["action"] == "get":
                result=get()
                module.exit_json(changed=False,meta=result)
        elif module.params["action"] == "put":
                result=put()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "delete":
                result=delete()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])


if __name__ == '__main__':
    main()