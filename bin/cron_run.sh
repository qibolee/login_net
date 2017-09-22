#!/bin/bash
# -*- coding: gbk -*-


################################################
# File Name		: cron_run.sh
# Author		: liqibo(qibolee@163.com)
# Create Time	: 2017/09/10
# Brief			: crontab task
################################################



# global config
static_date=`date +"%Y%m%d"`
static_time=`date +"%H:%M:%S"`
local_dir="/home/gitlab/develop/python/net_login"
log_dir="${local_dir}/log"
bin_dir="${local_dir}/bin"

# path config
path_log="${log_dir}/cron_${static_date}.log"
path_bin="${bin_dir}/login2.py"

# run
[[ ! -f ${path_log} ]] && touch ${path_log}

echo ">>>>>>>>>>>>>>>>>>> ${static_time} >>>>>>>>>>>>>>>>>" >>${path_log}

python ${path_bin} >>${path_log} 2>>${path_log}

echo -e "<<<<<<<<<<<<<<<<<<< ${static_time} <<<<<<<<<<<<<<<<<\n" >>${path_log}



