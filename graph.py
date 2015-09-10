# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
import rrdtool
import time,os
import graphsub

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#RRD = os.path.join(BASE_DIR,'rrdb')
#PNG = os.path.join(BASE_DIR,'png')
BASE_RRD = "/testproject/draw/draw/rrdb/"
BASE_PNG = '/testproject/monitor/static/png/'

def graph():
    #services = ['est_tcp', 'total_processes', 'memory_usage', 'root_partition', 'load_5min', 'ping_package_loss','network_eth0']
    #date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    strtime = str(int(time.time()- 86400))
    DSS = {"est_tcp":"DS:est_tcp:GAUGE:600:0:U",
          "total_processes":"DS:total_processes:GAUGE:600:0:U",
          "memory":"DS:memory_free:GAUGE:600:0:U,DS:memory_used:GAUGE:600:0:U",
          "disk_free":"DS:root:GAUGE:600:0:U,DS:root_dev_shm:GAUGE:600:0:U,DS:root_data:GAUGE:600:0:U",
          "load":"DS:load_1min:GAUGE:600:0:U,DS:load_5min:GAUGE:600:0:U,DS:load_15min:GAUGE:600:0:U",
          "ping":"DS:ping_rta:GAUGE:600:0:U",
          "network_eth0":"DS:network_rx:GAUGE:600:0:U,DS:network_tx:GAUGE:600:0:U",
          "memory_percent":"DS:memory_percent:GAUGE:120:0:100",
          "disk_percent":"DS:root_percent:GAUGE:120:0:100,DS:data_percent:GAUGE:120:0:100",
          "ping_percent":"DS:ping_percent:GAUGE:120:0:100",
          "api_ops":"DS:api_ops:GAUGE:60:0:U"}
    for host in os.listdir(BASE_RRD):
        data = {}
        #pitem = []
        rrddir = os.path.join(BASE_RRD, host)
        pngdir = os.path.join(BASE_PNG, host)
        if not os.path.exists(pngdir):
    	        os.mkdir(pngdir)
        for rrdfile in os.listdir(rrddir):
            rrdpath = os.path.join(rrddir, rrdfile)
            service = rrdfile.split('.')[0]
            DS = DSS[service]
                
            pitem = [i.split(':')[1] for i in DS.split(',') ]
                #for d in ds:
                    
            pngfile = os.path.join(pngdir, service + '.png')
            #title="%s for %s  (update:%s)" % (service, host, date)
            #if service == 'est_tcp':
                
            gdata = {'pname':pngfile, 'gname':service, 'rrdpath':rrdpath, 'pitem':pitem, 'flag':'Daily', 'stime':strtime, 'host':host, 'cols':'', 'itypes':''}
            if len(pitem) == 1: graphsub.dItem01(gdata)
            if len(pitem) == 2: graphsub.dItem02(gdata)
            if len(pitem) == 3: graphsub.dItem03(gdata)
            if len(pitem) == 4: graphsub.dItem04(gdata)

if __name__ == "__main__":
    graph()
