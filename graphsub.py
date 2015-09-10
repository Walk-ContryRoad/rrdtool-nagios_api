#!/usr/bin/env python
#coding=utf-8
import rrdtool
 
def dItem01(data):
    pngname = str(data['pname'])
    start = data['stime']
    graphname = str(data['gname'] + "(" + data['host'] + ")" + "(" + data['flag'] + ")")
    DEF = str(r"DEF:a="+data['rrdpath']+r':'+data['pitem'][0]+r":AVERAGE")
    if data['cols'] or data['itypes']:
        if not data['cols']:
            dtype = str(data['itypes'][0][0]+r":a#EAAF00FF:"+data['pitem'][0][1])
        elif not data['itypes']:
            dtype = str(r"AREA:a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
        else:
            dtype = str(data['itypes'][0][0]+r":a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
    else:
        dtype = str(r"AREA:a#EAAF00FF:"+data['pitem'][0])
    unit = str(data['pitem'][0][2])
    if not unit:
        unit = ' '
    max = 'GPRINT:a:MAX:Max\:%.2lf %s'
    min = 'GPRINT:a:MIN:Min\:%.2lf %s'
    avg = 'GPRINT:a:AVERAGE:Avg\:%.2lf %s'
    now = 'GPRINT:a:LAST:Now\:%.2lf %s'
    rrdtool.graph(pngname, '-w', '600', '-h', '144', '-l', '0', '-s', start,
                '-t', graphname, '-v', unit, DEF, 'COMMENT: \\n', dtype, now, avg, min, max, 'COMMENT: \\n')
###################################################################################################################
def dItem02(data):
    pngname = str(data['pname'])
    start = data['stime']
    graphname = str(data['gname']  + "(" + data['host'] + ")" + "(" + data['flag'] + ")")
    DEFa = str(r"DEF:a="+data['rrdpath']+r':'+data['pitem'][0]+r":AVERAGE")
    DEFb = str(r"DEF:b="+data['rrdpath']+r':'+data['pitem'][1]+r":AVERAGE")
    unit = str(data['pitem'][0][2])
    if not unit:
        unit = ' '
    if data['cols'] or data['itypes']:
        if not data['cols']:
            dtypea = str(data['itypes'][0][0]+r":a#00CF00FF:"+data['pitem'][0][1])
            dtypeb = str(data['itypes'][0][1]+r":b#002A97FF:"+data['pitem'][1][1])
        elif not data['itypes']:
            dtypea = str(r"AREA:a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
            dtypeb = str(r"LINE1:b"+data['cols'][0][1]+r":"+data['pitem'][1][1])
        else:
            dtypea = str(data['itypes'][0][0]+r":a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
            dtypeb = str(data['itypes'][0][1]+r":b"+data['cols'][0][1]+r":"+data['pitem'][1][1])
    else:
        dtypea = str(r"AREA:a#00CF00FF:"+data['pitem'][0])
        dtypeb = str(r"LINE1:b#002A97FF:"+data['pitem'][1])
    maxa = 'GPRINT:a:MAX:Max\:%.2lf %s'
    mina = 'GPRINT:a:MIN:Min\:%.2lf %s'
    avga = 'GPRINT:a:AVERAGE:Avg\:%.2lf %s'
    nowa = 'GPRINT:a:LAST:Now\:%.2lf %s'
    maxb = 'GPRINT:b:MAX:Max\:%.2lf %s'
    minb = 'GPRINT:b:MIN:Min\:%.2lf %s'
    avgb = 'GPRINT:b:AVERAGE:Avg\:%.2lf %s'
    nowb = 'GPRINT:b:LAST:Now\:%.2lf %s'
    rrdtool.graph(pngname, '-w', '600', '-h', '144', '-l', '0', '-s', start,
                '-t', graphname, '-v', unit, DEFa, DEFb, 'COMMENT: \\n', dtypea, nowa, avga, mina, maxa, 'COMMENT: \\n',
                dtypeb, nowb, avgb, minb, maxb, 'COMMENT: \\n')
###################################################################################################################
def dItem03(data):
    pngname = str(data['pname'])
    start = data['stime']
    graphname = str(data['gname']  + "(" + data['host'] + ")" + "(" + data['flag'] + ")")
    DEFa = str(r"DEF:a="+data['rrdpath']+r':'+data['pitem'][0]+r":AVERAGE")
    DEFb = str(r"DEF:b="+data['rrdpath']+r':'+data['pitem'][1]+r":AVERAGE")
    DEFc = str(r"DEF:c="+data['rrdpath']+r':'+data['pitem'][2]+r":AVERAGE")
    unit = str(data['pitem'][0][2])
    if not unit:
        unit = ' '
    if data['cols'] or data['itypes']:
        if not data['cols']:
            dtypea = str(data['itypes'][0][0]+r":a#00CF00FF:"+data['pitem'][0][1])
            dtypeb = str(data['itypes'][0][1]+r":b#002A97FF:"+data['pitem'][1][1])
        elif not data['itypes']:
            dtypea = str(r"AREA:a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
            dtypeb = str(r"LINE1:b"+data['cols'][0][1]+r":"+data['pitem'][1][1])
        else:
            dtypea = str(data['itypes'][0][0]+r":a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
            dtypeb = str(data['itypes'][0][1]+r":b"+data['cols'][0][1]+r":"+data['pitem'][1][1])
    else:
        dtypea = str(r"AREA:a#00CF00FF:"+data['pitem'][0])
        dtypeb = str(r"LINE1:b#002A97FF:"+data['pitem'][1])
        dtypec = str(r"LINE1:c#CC00CC:"+data['pitem'][2])
    maxa = 'GPRINT:a:MAX:Max\:%.2lf %s'
    mina = 'GPRINT:a:MIN:Min\:%.2lf %s'
    avga = 'GPRINT:a:AVERAGE:Avg\:%.2lf %s'
    nowa = 'GPRINT:a:LAST:Now\:%.2lf %s'
    maxb = 'GPRINT:b:MAX:Max\:%.2lf %s'
    minb = 'GPRINT:b:MIN:Min\:%.2lf %s'
    avgb = 'GPRINT:b:AVERAGE:Avg\:%.2lf %s'
    nowb = 'GPRINT:b:LAST:Now\:%.2lf %s'
    maxc = 'GPRINT:c:MAX:Max\:%.2lf %s'
    minc = 'GPRINT:c:MIN:Min\:%.2lf %s'
    avgc = 'GPRINT:c:AVERAGE:Avg\:%.2lf %s'
    nowc = 'GPRINT:c:LAST:Now\:%.2lf %s'
    rrdtool.graph(pngname, '-w', '600', '-h', '144', '-l', '0', '-s', start,
                '-t', graphname, '-v', unit, DEFa, DEFb, DEFc, 'COMMENT: \\n', dtypea, nowa, avga, mina, maxa, 'COMMENT: \\n',
                dtypeb, nowb, avgb, minb, maxb, 'COMMENT: \\n',
                dtypec, nowc, avgc, minc, maxc, 'COMMENT: \\n')
###################################################################################################################
def dItem04(data):
    pngname = str(data['pname'])
    start = data['stime']
    graphname = str(data['gname']  + "(" + data['host'] + ")" + "(" + data['flag'] + ")")
    DEFa = str(r"DEF:a="+data['rrdpath']+r':'+data['pitem'][0]+r":AVERAGE")
    DEFb = str(r"DEF:b="+data['rrdpath']+r':'+data['pitem'][1]+r":AVERAGE")
    DEFc = str(r"DEF:c="+data['rrdpath']+r':'+data['pitem'][2]+r":AVERAGE")
    DEFd = str(r"DEF:d="+data['rrdpath']+r':'+data['pitem'][3]+r":AVERAGE")
    unit = str(data['pitem'][0][2])
    if not unit:
        unit = ' '
    if data['cols'] or data['itypes']:
        if not data['cols']:
            dtypea = str(data['itypes'][0][0]+r":a#00CF00FF:"+data['pitem'][0][1])
            dtypeb = str(data['itypes'][0][1]+r":b#002A97FF:"+data['pitem'][1][1])
        elif not data['itypes']:
            dtypea = str(r"AREA:a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
            dtypeb = str(r"LINE1:b"+data['cols'][0][1]+r":"+data['pitem'][1][1])
        else:
            dtypea = str(data['itypes'][0][0]+r":a"+data['cols'][0][0]+r":"+data['pitem'][0][1])
            dtypeb = str(data['itypes'][0][1]+r":b"+data['cols'][0][1]+r":"+data['pitem'][1][1])
    else:
        dtypea = str(r"AREA:a#00CF00FF:"+data['pitem'][0])
        dtypeb = str(r"LINE1:b#002A97FF:"+data['pitem'][1])
        dtypec = str(r"LINE1:c#CC00CC:"+data['pitem'][2])
        dtyped = str(r"LINE1:d#FFFF00:"+data['pitem'][3])
    maxa = 'GPRINT:a:MAX:Max\:%.2lf %s'
    mina = 'GPRINT:a:MIN:Min\:%.2lf %s'
    avga = 'GPRINT:a:AVERAGE:Avg\:%.2lf %s'
    nowa = 'GPRINT:a:LAST:Now\:%.2lf %s'
    maxb = 'GPRINT:b:MAX:Max\:%.2lf %s'
    minb = 'GPRINT:b:MIN:Min\:%.2lf %s'
    avgb = 'GPRINT:b:AVERAGE:Avg\:%.2lf %s'
    nowb = 'GPRINT:b:LAST:Now\:%.2lf %s'
    maxc = 'GPRINT:c:MAX:Max\:%.2lf %s'
    minc = 'GPRINT:c:MIN:Min\:%.2lf %s'
    avgc = 'GPRINT:c:AVERAGE:Avg\:%.2lf %s'
    nowc = 'GPRINT:c:LAST:Now\:%.2lf %s'
    maxd = 'GPRINT:d:MAX:Max\:%.2lf %s'
    mind = 'GPRINT:d:MIN:Min\:%.2lf %s'
    avgd = 'GPRINT:d:AVERAGE:Avg\:%.2lf %s'
    nowd = 'GPRINT:d:LAST:Now\:%.2lf %s'
    rrdtool.graph(pngname, '-w', '600', '-h', '144', '-l', '0', '-s', start,
                '-t', graphname, '-v', unit, DEFa, DEFb, DEFc, DEFd, 'COMMENT: \\n', dtypea, nowa, avga, mina, maxa, 'COMMENT: \\n',
                dtypeb, nowb, avgb, minb, maxb, 'COMMENT: \\n',
                dtypec, nowc, avgc, minc, maxc, 'COMMENT: \\n',
                dtyped, nowd, avgd, mind, maxd, 'COMMENT: \\n')
