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


url = "http://10.3.8.211/F.htm"

def main():
    '''
    logout from 10.3.8.211/F.htm
    '''
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    result = response.read()

    print "response code: %d" % response.code

    if response.code != 200:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()






