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
import check_flow


url = "http://10.3.8.211/F.htm"

def do_logout():
    '''
    do logout from Internet
    '''
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    result = response.read()

    return response.code == 200


def main():
    '''
    check is login first
    '''
    result = check_flow.get_login_data()
    if check_flow.is_logged(result):
        check_flow.show_flow_data(result)
        if do_logout():
            print "logout success"
        else:
            print "logout failed"
    else:
        print "---------------------------"
        print "not login now, don't need logout"
        print "---------------------------"


if __name__ == "__main__":
    main()






