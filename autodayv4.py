#!/usr/bin/env python
import sys
import csv
import os
import time
import datetime
from datetime import timedelta
import random
from datetime import date
import urllib.request
import json
import pprint
from datetime import datetime
import pytz


#***************************************** 
def send_first_order_daya(pwd,tkey,sakimono,yobi,direction,qnum,night):

    fsymbol=sakimono    
    exchange=23
    
    obj = { 'Password': pwd,
        'Symbol': fsymbol,
        'Exchange': exchange,
        'TradeType': 1,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': direction, #Uri=1 kai=2
        'Qty': qnum,
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    json_data = json.dumps(obj).encode('utf-8')
    print (json_data)
    
    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
         
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
#**************************************************
def read_econfig(configfnm):
    
        
    with open(configfnm,'r') as ff:
        wconfig=ff.read(100)
    print (wconfig)
    confs=wconfig.split(';')
    return confs
def read_topix(topixfile):
        
    with open(topixfile,'r') as ff:
        wconfig=ff.read(100)
    print (wconfig)
    confs=wconfig.strip()
    return confs


def sendmsg2topix(topixfile,tag):

    with open(topixfile,'w') as entry:
        cont=tag
        entry.write(cont)  
          

def get_nk225mini_quote(tkey,sakimono,tdate):
    #fsymbol='166060019' 
    #print ("get quote")
    fsymbol=sakimono   
    url = 'http://localhost:18080/kabusapi/board/'+fsymbol+'@2'    
    #url = 'http://localhost:18080/kabusapi/board/166030019@2'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)
    cprice=[]
    try:
        
        
        with urllib.request.urlopen(req) as res:
            #print(res.status, res.reason)
            for header in res.getheaders():
                #print(header)
                pass
            #print()
            content = json.loads(res.read())
            #pprint.pprint(content)
            #print (content['CurrentPrice'])
            #print (content["CurrentPriceTime"])
            fulltime=str(content["CurrentPriceTime"])
            ctime=fulltime[11:16]
            #print (ctime)
            cprice=[tdate,content['CurrentPrice'],ctime]
            #print ("cprice",cprice)
            return cprice

       
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
#********************************************



def send_order4a(pwd,tkey,sakimono,yobi,direction,hold,qnum,night):


    fsymbol=sakimono   

    corder=0
    
    iqnum=1
    #daytrade
    exflag=23
    hold=''
    corder=0
    #******************************************
    if (direction=='1'):
        hensai='2'
    elif (direction=='2'):
        hensai='1'
    if (hold):
        obj = { 'Password': pwd,
        'Symbol': fsymbol,
        'Exchange': exflag,
        'TradeType': 2,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': hensai, #Uri=1 kai=2
        'Qty': iqnum,
        'ClosePositions':arrhid,  #for Tuesday
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    else:     
        obj = { 'Password': pwd,
        'Symbol': fsymbol,
        'Exchange': exflag,
        'TradeType': 2,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': hensai, #Uri=1 ksi=2
        'Qty': iqnum,
        'ClosePositionOrder':corder,  #for Tuesday
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    json_data = json.dumps(obj).encode('utf-8')
    print (json_data)
    
    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
         
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

def auto402a(pwd,tkey,sakimono,begintime,endtime,actionyobi,direction,initq,qnum,jdate2,eki,loss,ekionly,night,sent,hold,rinitq,maisu):
    tdate=jdate2
    yobi=actionyobi
    breakflag=0
    
    #debug '0'
    stdate=tdate

    sent='1'
    hold=''
    qnum=1
    
    print ("hold:",hold)
    print ('actionyobi,direction,initq,qnum,jdate2,eki,loss,hold')
    print (actionyobi,direction,initq,qnum,jdate2,eki,loss,hold)


    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jdate=dt_j.strftime('%Y%m%d')
    jdate2=dt_j.strftime('%Y-%m-%d')
    dt_j=datetime.now(timeZ_J)
    jtime=dt_j.strftime('%H:%M')
    
    jj=0
    
    breakflag=5
    night='2'
    print ("begintime",begintime)
    while (jtime>=begintime and jtime<=endtime ):    
    
        jj+=1
            
        
        
    


        
        cprice=get_nk225mini_quote(tkey,sakimono,tdate)
        #******************
        quote=float(cprice[1])
                
        print ("price",quote)
        if (not quote or quote==0):
            breakflag=5
            
            #continue to night session
            print ("NO quote because break session")

            
        elif (quote<=(initq-eki) and direction=='1'):
                yobi=actionyobi
                mbuy=quote
                meki=1
                msell=initq
                
                ekiv=initq-mbuy
                print ('ekidahi-1',jdate2,yobi,msell,quote,ekiv,'EKI-1')                
                #actions.append([tdate,yobi,qtime,msell,quote,ekiv,hanten,'EKI',direction])
                if (sent=='1'):
                    
                    eflag=send_order4a(pwd,tkey,sakimono,actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    
                    
                    breakflag=1
                    break 
                    
               


        elif (quote>=(initq+loss)  and direction=='1' ):
                yobi=actionyobi
                mbuy=quote
                msell=initq
                mlss=1
                lossv=initq-mbuy
                print ('losscut-1',jdate2,yobi,msell,quote,lossv,'LCUT')
                #actions.append([tdate,yobi,qtime,msell,quote,lossv,hanten,'LCUT',direction])
                print ("action loscut-1")
                #*******************NO LOSSCUT????***************************
                if (sent=='1'):
                    

                    
                    eflag=send_order4a(pwd,tkey,sakimono,actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    
                    breakflag=1
                    break 
                    
                        
  
                

        elif (quote>=(initq+eki)  and  direction=='2'):
                print ("limit quote ",mlimit,quote)
                msell=quote
                mbuy=initq
                meki=1
                ekiv=msell-initq
                print ('ekidahi-2',jdate2,mbuy,quote,ekiv,'EKI-2')                
                #actions.append([tdate,yobi,qtime,mbuy,quote,ekiv,hanten,'EKI',direction])
                if (sent=='1'):
                    
                    eflag=send_order4a(pwd,tkey,sakimono,actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    
                    breakflag=1
                    break 
                              
                
                
        
                              
        elif (quote<=(initq-loss)  and  direction=='2' ):
                
                msell=quote
                mbuy=initq
                mlss=1
                lossv=initq-msell
                print ('losscut-2',jdate2,mbuy,quote,lossv,'LCUT')                
                
                if (sent=='1'):
                   
                    eflag=send_order4a(pwd,tkey,sakimono,actionyobi,direction,hold,qnum,night)
                    print (eflag)
                    
                    breakflag=1
                    break 
                    
                       

                    
                    
                

        else:
                          
            print ("NO losscut/ekidashi")

                

                
        
        timeZ_J=pytz.timezone('Asia/Tokyo')
        dt_j=datetime.now(timeZ_J)
        #print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
            
        dt_j=datetime.now(timeZ_J)
        jtime=dt_j.strftime('%H:%M')
        ltime=time.strftime('%H:%M')
        #print ('night?: ',night)
        time.sleep(10)
        #10-> 2                       
    #exit from while                            
    else:
        print ("end of session  ",breakflag)
        breakflag=5
    return breakflag



def read_action(filenm):
  with open(filenm) as g:
    lg=g.read(100)
    
    wlg=lg.strip()
    print (wlg)
    return wlg
#************************
def hensai_order_topix(pwd,tkey,sakimono,direction,night):

    fsymbol=sakimono   
    #url = 'http://localhost:18080/kabusapi/board/'+fsymbol+'@2'      
    corder=0
    
    iqnum=1
    #daytrade
    if (night=='1'):
        exflag=24
    else:
        exflag=23
    
    
    
        
    
    hold=''
    corder=0
    #******************************************
    if (direction=='1'):
        hensai='2'
    elif (direction=='2'):
        hensai='1'
    if (hold):
        obj = { 'Password': pwd,
        'Symbol': fsymbol,
        'Exchange': exflag,
        'TradeType': 2,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': hensai, #Uri=1 kai=2
        'Qty': iqnum,
        'ClosePositions':arrhid,  #for Tuesday
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    else:     
        obj = { 'Password': pwd,
        'Symbol': fsymbol,
        'Exchange': exflag,
        'TradeType': 2,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': hensai, #Uri=1 ksi=2
        'Qty': iqnum,
        'ClosePositionOrder':corder,  #for Tuesday
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    json_data = json.dumps(obj).encode('utf-8')
    print (json_data)
    
    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
         
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
#***************************************** 
def send_first_order_topix(pwd,tkey,topix,direction,qnum,night):
    #*********************************

    fsymbol=topix
    qnum=1

    if (night=='1'):
        exchange=24
    else:
        exchange=23
    
    obj = { 'Password': pwd,
        'Symbol': fsymbol,
        'Exchange': exchange,
        'TradeType': 1,  #1:shinki 2:hensai
        'TimeInForce': 2,
        'Side': direction, #Uri=1 kai=2
        'Qty': qnum,
        'Price': 0,
        'ExpireDay': 0,
        'FrontOrderType': 120 } #nariyuki
    json_data = json.dumps(obj).encode('utf-8')
    print (json_data)
    
    url = 'http://localhost:18080/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', tkey)

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
         
            content = json.loads(res.read())
            pprint.pprint(content)
    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
#**************************************************        
#**************************
if __name__ == '__main__':
    
    args = sys.argv
    sendflag=args[1]
    sendtopix=args[2]
    #sendflag='1'
    print ("sendflag",sendflag)
    path = os.getcwd()
    efilenm=path+"\\econfig.txt"    
    econfig=read_econfig(efilenm)
    ieki=float(econfig[0])
    iloss=float(econfig[1])
    aftereki=float(econfig[2])
    afterloss=float(econfig[3])
    revlimit=float(econfig[4])
    maisu=int(econfig[5])    
    print ('eki,loss,aftereki,afterloss,revlimit,maisu')
    print (econfig)
    #**************************

    pwdfilenm=path+"\\pwd.txt"    
    pwd=read_action(pwdfilenm)
    topixnofile=path+"\\topixno.txt"    
    topix=read_action(topixnofile)
    print ("topixno:",topix)
    eki=ieki
    loss=iloss
    #****************************
    mlss=0
    mloss=0
    meki=0
    mlimit=0
    mend=0
    initq=0
    holds=[]
    hanten='0'        
    ekionly='NO'

    holdposiiton=0
#***Do not use holds*************************
    hold=''
    hqty=0
    #************default 1*****************
    qnum=1
    #topix='167060006'
#**************************************************************
    

    #direction='2'   
    #***********************if night '1' otherwise '0'
    night='2'
    ekionly='NO'        
    only15m='NO'        
    exchange=23
    #all time     
    starttime='00:00'
    endtime='25:00'
    
    #****************************************
    path = os.getcwd()
    #****************************************
    tkfilenm=path+"\\kabutoken.txt"
    sakimonofile=path+"\\sakimono.txt"
    #set prediction score such as 1.0 or -1.0
    actionfile=path+"\\action.txt"
    topixfile=path+"\\topix.txt"
    with open(tkfilenm,'r') as token:
        tkey=token.read(100)
    #06-03-2021 fsymbol from sakimono
    with open(sakimonofile,'r') as saki:
        sakimono=saki.read(100)

    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jtime=dt_j.strftime('%H:%M')
    jyobi=dt_j.strftime('%w')
    j=0
    
    #wait until 08:40 
   
    while (jtime<'08:40' and j<6*120):
        j+=1
        dt_j=datetime.now(timeZ_J)
        print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
        jtime=dt_j.strftime('%H:%M')
        time.sleep(10)          
    
   
    
    confs=read_action(actionfile)    
    print ("action score:",confs)
    fscore=float(confs)
    if (fscore>0):
        direction='2'
        directionrev='1'
    elif (fscore<0):
        direction='1'
        directionrev='2'
    else:
        direction=directionrev='0'
    #default
    qnum=1
    
    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jdate=dt_j.strftime('%Y%m%d')
    jdate2=dt_j.strftime('%Y-%m-%d')
    jtime=dt_j.strftime('%H:%M')
    jyobi=dt_j.strftime('%w')
    print ("jyobi",jyobi)
    #read mdayconfig.txt  and set direction and qnum
    actionyobi=jyobi     
    exchange=23
      
    
    sendmsg2topix(topixfile,'0')
    
       
   
    
    

    
    
    print ("actionyobi,direction,qnum,night")
    print (actionyobi,direction,qnum,night)
    #send order
    #this is for getting intiq
    entrytime='08:45'
    if (sendflag=='1'):
        k=0
        res=send_first_order_daya(pwd,tkey,sakimono,actionyobi,direction,qnum,night)
        if (sendtopix=='1'):
            pass
            #if you need to send topix
            #rest=send_first_order_topix(pwd,tkey,topix,directionrev,qnum,night)
    else:
        #k=6*100+2
        k=0
        sendflag='0'
        sendtopix='0'
        print ('set current price as the initq ')
        entrytime='00:00'
    print ("END of new order issued then set entry data, can wait for 20 minutes")      
    
#***************************************
    
    
    
    while (k<6*100):
        k+=1
        
        dt_j=datetime.now(timeZ_J)
        print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))    
        jdate2=dt_j.strftime('%Y-%m-%d')
        jhm=dt_j.strftime('%H:%M')
        print (jhm)

        if (jhm<=entrytime):
            print ("No entry yet")
            time.sleep(10)
            continue   
     
        else:
            cprice=get_nk225mini_quote(tkey,sakimono,jdate2)
            
            #set initial quote
            print ('cprice',cprice)
            if (cprice[1]>0): 
                initq=cprice[1] 
                break
            else:
                print ('No cprice')
                time.sleep(10)
                continue
    
#**************************end of xend order and set entryq******
    mbuy=tbuy=msell=tsell=0
    x = date.today()
    nextd=x+timedelta(days=1)

    dx=nextd.strftime("%Y-%m-%d")
    tdate=dx

    #******************************************
    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)
    print ("Japan-time:",dt_j.strftime('%Y-%m-%d %H:%M:%S'))
    jdate=dt_j.strftime('%Y%m%d')
    jdate2=dt_j.strftime('%Y-%m-%d')
    jtime=dt_j.strftime('%H:%M')
    ltime=time.strftime('%H:%M')
    jyobi=dt_j.strftime('%w')
    j=0
    #2hours
    
    
    #***************************************
    kk=0
    res=0
    
    
    
    print ("finally get initq and direction",initq,direction)
    if (initq>0):     
        print ("start monitoring")
        

        #************************monitoring *****************************************
        qnum=1
        
        sent='1'
       
        rinitq=0
        
        #loop inside until the end of daysession   

        res=auto402a(pwd,tkey,sakimono,starttime,endtime,jyobi,direction,initq,qnum,jdate2,eki,loss,ekionly,night,sent,hold,rinitq,maisu)
        print ("result code:",res)
    else:
        print ("ERROR:initq is wrong!, no monitoring and stop") 
        res=9
        
    
    #after monitoring
    #************if add new order,then update ordered qnum**04-11-2021
    if (res==1 or res==9):
        print ("loscut or ekidashi is done fully or no start yet, no further action")
        sendmsg2topix(topixfile,'1') 

        if (sendtopix=='1' and res==1):
            eflag=hensai_order_topix(pwd,tkey,topix,directionrev,night)    

               
    else: 
        #daytrade   
        night='2'                      
        hold=''
        qnum=1
        print ("kessai must be done, send last order")
        eflag=send_order4a(pwd,tkey,sakimono,actionyobi,direction,hold,qnum,night)
        print (eflag)
        if (sendtopix=='1'):                       
            eflagt=hensai_order_topix(pwd,tkey,topix,directionrev,night)            
    
    
    print ('END of session')