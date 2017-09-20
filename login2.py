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


url = "http://10.3.8.211"
path_file = "./userid_passwd"

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


def load_data():
    dict_uid_passwd = {}
    with open(path_file) as file:
        for line in file:
            line = line.strip()
            ll = map(lambda x:x.strip(), line.split("\t"))
            if len(ll) != 2:
                continue
            userid = ll[0]
            passwd = ll[1]
            dict_uid_passwd[userid] = passwd
    return dict_uid_passwd


def main():
    dict_uid_passwd = load_data()
    for uid in dict_uid_passwd:
        passwd = dict_uid_passwd[uid]
        res = run(url, uid, passwd)
        if res == 0:
            break


if __name__ == "__main__":
    main()






