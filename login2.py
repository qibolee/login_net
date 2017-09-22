#!/usr/bin/env python
# -*- coding: gbk -*-


###########################################  
# File Name     : login2.py
# Author        : liqibo(qibolee@163.com)
# Created Time  : 2017/9/10
# Brief         : log in to internet
###########################################


__revision__ = '0.1'
import sys
import urllib
import urllib2
import check_flow


url = "http://10.3.8.211"
path_dir = "/home/gitlab/develop/python/net_login"
file_name = "userid_passwd"
path_file = "%s/%s" % (path_dir, file_name)

def do_login(url, userid, passwd):
    '''
    do login to Internet
    '''
    data = {"DDDDD":userid, "upass":passwd, "0MKKey":""}
    data = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=data)
    response = urllib2.urlopen(request)
    result = response.read()

    return response.code == 200


def load_data():
    '''
    get uid-passwd data from file
    '''
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
    '''
    check is login first
    '''
    result = check_flow.get_login_data()
    if check_flow.is_logged(result):
        print "already logged in, don't need login again"
        check_flow.show_flow_data(result)
        return 0
    dict_uid_passwd = load_data()
    for uid in dict_uid_passwd:
        passwd = dict_uid_passwd[uid]
        res = do_login(url, uid, passwd)
        if not res:
            print "login request failed: %s %s" % (uid, passwd)
            continue
        result = check_flow.get_login_data()
        if check_flow.is_logged(result):
            print "login success: %s" % uid
            check_flow.show_flow_data(result)
            break
        else:
            print "login result failed: %s %s" % (uid, passwd)


if __name__ == "__main__":
    main()






