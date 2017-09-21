#!/usr/bin/env python
# -*- coding: gbk -*-


###########################################  
# File Name     : logout.py
# Author        : liqibo(qibolee@163.com)
# Created Time  : 2017/9/10
# Brief         : log out from internet
###########################################


__revision__ = '0.1'
import sys
import urllib
import urllib2


url = "http://10.3.8.211"

def get_flow_msg():
    '''
    get flow data from 10.3.8.211
    '''
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    result = response.read()

    print "response code: %d" % response.code

    if response.code != 200:
        return ""
    else:
        return result


def parse_msg(msg):
    if not msg:
        print "message is empty"
        return 1
    dict_data = {"time": "", "flow": "", "fee": ""}
    for key in dict_data:
        idx = msg.find("%s=" % key)
        if idx != -1:
            idx += len(key) + 2
            while msg[idx] == " ":
                idx += 1
            while msg[idx] in "0123456789":
                dict_data[key] += msg[idx]
                idx += 1

    for key in dict_data:
        print "%s: %s" % (key, dict_data[key])
    return 0


def main():
    msg = get_flow_msg()
    parse_msg(msg)

if __name__ == "__main__":
    main()






