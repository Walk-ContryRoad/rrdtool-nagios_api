# encoding: utf-8
#!/usr/bin/python

import time
import rrdtool
import re, os
import json
#from pprint import pprint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(BASE_DIR,'rrdb')
def task():
    #starttime=int(time.time())
    #url = "curl http://localhost:3721/state"
    #command_hosts = "nagios-cli --host='localhost' --port='3721' hosts"
    command_hosts = "/testproject/packages/nagios-api-1.2.2/nagios-cli --host='localhost' --port='3721' hosts"
    #command_state = "nagios-cli --host='localhost' --port='3721' --raw state"
    command_state = "/testproject/packages/nagios-api-1.2.2/nagios-cli --host='localhost' --port='3721' --raw state"
    states = os.popen(command_state).readlines()
    hosts_all = os.popen(command_hosts).readlines()
    #hosts = ['ebs-ali-beijing-tools18','ebs-ali-beijing-tools19','ebs-ali-beijing-app1']
    #for host in hosts_all:
    #    host_list.append("".join(host.strip('\n')))
    for state in states:
        resp_states = json.loads(state.decode('utf-8'))
        for hosts in hosts_all:
            host = str("".join(hosts.strip('\n')))
            rrddir = str(os.path.join(DIR, host))
            a1=a2=a3=b1=b2=b3=c1=c2=d1=d2=e1=e2=e3=e4=f1=g1=0
            content = resp_states[host]
            for key, value in content['services'].iteritems():
                #之所以从嵌套字典先判断再取值这么麻烦，是因为有些services里没有Load等项，直接用content['services']['Load']['plugin_output']取会报key error
                v = value['plugin_output']
                if key == 'Load':##OK - load average: 0.35, 0.25, 0.11
                    a = re.findall('\d*\.?\d+', v)
                    a1 = str(a[0])
                    a2 = str(a[1])
                    a3 = str(a[2])
                elif key == 'Memory usage':#Free memory is 8021,  used 7926, free memory 50%
                    b = re.findall('\d*\.?\d+', v)
                    b1 = str(b[0])
                    b2 = str(b[1])
                    b3 = str(b[2])#use percent
                elif key == 'Network eth0':#network is critical, RX/s is 85846 kb, TX/s is 5220 kb
                    c = re.findall('\d*\.?\d+', v)
                    c1 = str(c[0])
                    c2 = str(c[1])
                elif key == 'PING':#PING OK - Packet loss = 0%, RTA = 0.28 ms
                    d = re.findall('\d*\.?\d+', v)
                    d1 = str(d[0])#loss percent
                    d2 = str(d[1])
                elif key == 'Root Partition':#DISK OK - free space: / 14266 MB (74% inode=82%): /dev/shm 7974 MB (100% inode=99%): /data 34623 MB (72% inode=99%):
                    e = re.findall('\d*\.?\d+', v)
                    e1 = str(e[0])
                    e2 = str(e[3])
                    e66 = [e[6] if len(e)>6 else 0]
                    e77 = [e[7] if len(e)>7 else 0]
                    e3 = str(e66[0])#/dev/shm
                    e4 = str(e[1])#/root_use percent
                    e5 = str(e77[0])#/data_use_percent
                elif key == 'Total Processes':#PROCS OK: 116 processes
                    f = re.findall('\d*\.?\d+', v)
                    f1 = str(f[0])
                elif key == 'est tcp':#184 sockets in established state. ok!
                    g = re.findall('\d*\.?\d+', v)
                    g1 = str(g[0])
            rrdtool.update(rrddir + '/est_tcp.rrd', 'N:%s' % g1)
            rrdtool.update(rrddir + '/total_processes.rrd', 'N:%s' % f1)
            rrdtool.update(rrddir + '/memory.rrd', 'N:%s:%s' % (b1,b2))
            rrdtool.update(rrddir + '/disk_free.rrd', 'N:%s:%s:%s' % (e1,e2,e3))
            rrdtool.update(rrddir + '/load.rrd', 'N:%s:%s:%s' % (a1,a2,a3))
            rrdtool.update(rrddir + '/ping.rrd', 'N:%s' % (d2))
            rrdtool.update(rrddir + '/network_eth0.rrd', 'N:%s:%s' % (c1,c2))
            rrdtool.update(rrddir + '/memory_percent.rrd', 'N:%s' % (b3))
            rrdtool.update(rrddir + '/ping_percent.rrd', 'N:%s' % (d1))
            rrdtool.update(rrddir + '/disk_percent.rrd', 'N:%s:%s' % (e4,e5))
            #print "@@@@@@@@@@",update1, update2, update3, update4,update5,update6,update7,"@@@@@@@@@@@" 
                #else:
                #    pass
            #a = re.findall('\d*\.?\d+', a1)
            #b = re.findall('\d*\.?\d+', b1)
            #c = re.findall('\d*\.?\d+', c1)
            #d = re.findall('\d*\.?\d+', d1)
            #e = re.findall('\d*\.?\d+', e1)
            #f = re.findall('\d*\.?\d+', f1)
            #g = re.findall('\d*\.?\d+', g1)
            #print a1,b1,c1,d1,e1,f1,g1
            #print "==a:",a,"==b:",b,"==c:",c,"==d:",d,"==e:",e,"==f:",f,"==g:",g
            #print "leng of e:",len(e)
            #ee = [e[6] if len(e)>6 else 0]
            #for i in [a,b,c,d,e,f,g]:
            #    if len(i)==1: print i[0]
            #    if len(i)==2: print i[0],i[1]
            #    if len(i)==3: print "3:",i[0],i[1],i[2]
            #    if len(i)>=4: print "4:",i[0],i[1],i[3],ee[0]
            #print "g[0]: ", g[0], type(str(g[0]))
            #a = re.findall('\d*\.?\d+', content['services']['Load']['plugin_output'])
            #b = re.findall('\d*\.?\d+', content['services']['Memory usage']['plugin_output'])
            #c = re.findall('\d*\.?\d+', content['services']['Network eth0']['plugin_output'])
            #d = re.findall('\d*\.?\d+', content['services']['PING']['plugin_output'])
            #e = re.findall('\d*\.?\d+', content['services']['Root Partition']['plugin_output'])
            #f = re.findall('\d*\.?\d+', content['services']['Total Processes']['plugin_output'])
            #g = re.findall('\d*\.?\d+', content['services']['est tcp']['plugin_output'])
            #rrddir = str(os.path.join(DIR, host.strip('\n')))
            #if not os.path.exists(rrddir): os.mkdir(rrddir)
            #update1=rrdtool.updatev(rrddir + '/est_tcp.rrd', 'N:%s' % g1)
            #update2=rrdtool.updatev(rrddir + '/total_processes.rrd', 'N:%s' % f1)
            #update3=rrdtool.updatev(rrddir + '/memory.rrd', 'N:%s:%s:%s' % (str(b[0]), str(b[1]), str(b[2])))
            #update4=rrdtool.updatev(rrddir + '/disk_free.rrd', 'N:%s:%s:%s:%s' % (str(e[0]), str(e[1]), str(e[3]), str(ee[0])))
            #update5=rrdtool.updatev(rrddir + '/load.rrd', 'N:%s:%s:%s' % (a1,a2,a3))
            #update6=rrdtool.updatev(rrddir + '/ping.rrd', 'N:%s:%s' % (str(d[0]), str(d[1])))
            #update7=rrdtool.updatev(rrddir + '/network_eth0.rrd', 'N:%s:%s' % (str(c[0]), str(c[1])))
            #print "@@@@@@@@@@",update1, update2, update3, update4,update5,update6,update7,"@@@@@@@@@@@"
            #print "+++++++++++++++", update5,"++++++++++++++++"
            #print "=====",rrddir + '/est_tcp.rrd', 'N:%s' % str(g[0])
            #print "=====",rrddir + '/total_processes.rrd', 'N:%s' % str(f[0])
            #print "=====",rrddir + '/memory.rrd', 'N:%s:%s:%s' % (str(b[0]), str(b[1]), str(b[2]))
            #print "=====",rrddir + '/disk_free.rrd', 'N:%s:%s:%s:%s' % (str(e[0]), str(e[1]), str(e[3]), str(ee[0]))
            #print "=====",rrddir + '/load.rrd', 'N:%s:%s:%s' % (a1,a2,a3)
            #print "=====",rrddir + '/ping.rrd', 'N:%s:%s' % (str(d[0]), str(d[1]))
            #print "=====",rrddir + '/network_eth0.rrd', 'N:%s:%s' % (str(c[0]), str(c[1]))
       
#def timer(n):
#    while True:
#        print "++++++++++++++", time.strftime('%Y-%m-%d %X',time.localtime()),"+++++++++++++++++++"
#        task()
#        time.sleep(n)

if __name__ == '__main__':
    task()
    #timer(5) 
