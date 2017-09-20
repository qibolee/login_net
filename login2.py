#!/usr/bin/env python
# -*- coding: gbk -*-


###########################################  
# File Name     : login.py
# Author        : liqibo(qibolee@163.com)
# Created Time  : 2017/9/10
# Brief         : log in to internet
###########################################


__revision__ = '0.1'
import sys
import urllib
import urllib2



def run(url, userid, passwd):
    '''
    login to Internet
    '''
    data = {"DDDDD":userid, "upass":passwd, "0MKKey":""}
    data = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=data)
    response = urllib2.urlopen(request)
    result = response.read()

    print "response code: %d, userid: %s" % (response.code, userid)

    if response.code != 200:
        return 1
    else:
        #print result
        return 0


def main():
    url = "http://10.3.8.211"
    dict_uid_passwd = {
        "2011211534": "207310", "2011211535": "123456", "2011211544": "gzc12345",
        "2011211545": "067514", "2011211654": "122118","2012211325": "214527", "2013140848": "122533"
    }
    for uid in dict_uid_passwd:
        passwd = dict_uid_passwd[uid]
        res = run(url, uid, passwd)
        if res == 0:
            break


if __name__ == "__main__":
    main()






