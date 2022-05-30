#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import json
import pprint
import os

def token(password):
    obj = { 'APIPassword': password }
    json_data = json.dumps(obj).encode('utf8')

    url = 'http://localhost:18080/kabusapi/token'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            print (content['ResultCode'])
            print (content['Token'])
            result=''
            if (content['ResultCode']==0):
                result=content['Token']
            with open('kabutoken.txt','w') as entry:
                entry.write(result)
    
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
    

def register(tkey,symbol):

    obj = { 'Symbols':[ 
            
            {'Symbol': symbol, 'Exchange': 2}
            
        ] }
    json_data = json.dumps(obj).encode('utf8')

    url = 'http://localhost:18080/kabusapi/register'
    req = urllib.request.Request(url, json_data, method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
	


#***********************main***********	
if __name__ == '__main__':

	path = os.getcwd()
	tkfilenm=path+"\\kabutoken.txt"
	sakimonofile=path+"\\sakimono.txt"
	password=input("password:")
	token(password)
	with open(tkfilenm,'r') as token:
		tkey=token.read(100)
	with open(sakimonofile,'r') as saki:
		sakimono=saki.read(100)
		fsymbol=sakimono 
	register(tkey,fsymbol)
	
	
    