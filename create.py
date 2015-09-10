# encoding: utf-8
#!/usr/bin/python

from time import ctime
import time, datetime
import threading
import rrdtool
import re, os
import createsub

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(BASE_DIR,'rrd')
if not os.path.exists(DIR):
    os.mkdir(DIR)
#cur_time=str(int(time.time()))
timeDaysAgo = (datetime.datetime.now() - datetime.timedelta(days = 730))
startStamp = str(int(time.mktime(timeDaysAgo.timetuple())))
def createdb():
    command_hosts = "/testproject/packages/nagios-api-1.2.2/nagios-cli --host='localhost' --port='3721' hosts"
    hosts_resp = os.popen(command_hosts).readlines()
    for hosts in hosts_resp:
        host = "".join(hosts.decode('utf-8')).strip('\n')

        DSS = {"est_tcp":"DS:est_tcp:GAUGE:120:0:U",
          "total_processes":"DS:total_processes:GAUGE:120:0:U",
          "memory":"DS:memory_free:GAUGE:120:0:U,DS:memory_used:GAUGE:120:0:U,DS:memory_percent:GAUGE:120:0:100",
          "disk_free":"DS:root:GAUGE:120:0:U,DS:root_percent:GAUGE:120:0:100,DS:root_dev_shm:GAUGE:120:0:U,DS:root_data:GAUGE:120:0:U",
          "load":"DS:load_1min:GAUGE:120:0:U,DS:load_5min:GAUGE:120:0:U,DS:load_15min:GAUGE:120:0:U",
          "ping":"DS:ping_percent:GAUGE:120:0:100,DS:ping_rta:GAUGE:120:0:U",
          "network_eth0":"DS:network_rx:GAUGE:120:0:U,DS:network_tx:GAUGE:120:0:U"}
        rrddir = os.path.join(DIR,host)
        print rrddir
        if not os.path.exists(rrddir): os.mkdir(rrddir)
        for ds in DSS:
            rrdname = str(os.path.join(rrddir, ds + '.rrd'))
            DS = DSS[ds].split(',')
            if not os.path.isfile(rrdname):
                if len(DS) == 1: createsub.Item01(rrdname, startStamp, DS)
                if len(DS) == 2: createsub.Item02(rrdname, startStamp, DS)
                if len(DS) == 3: createsub.Item03(rrdname, startStamp, DS)
                if len(DS) == 4: createsub.Item04(rrdname, startStamp, DS)
        #        #if len(DS) == 4: createsub.test(rrdname, startStamp, DS)


if __name__ == "__main__":
    createdb() 
