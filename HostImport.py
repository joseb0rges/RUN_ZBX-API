#-*- coding:utf-8 -*-
import csv

from biblioteca import *


def HostImport(arquivo):

    zapi = ZabbixAPI(server)
    zapi.session.verify = False
    zapi.login(username, password)

    data = csv.reader(open(arquivo, 'r'))
    cont = 0

    for dt in data: #tratando variaveis
        bar = ProgressBar(maxval=len(dt[0]),
                          widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
        host = dt[0]
        ip1 = dt[1]
        ip2 = dt[2]
        gp = dt[3]
        v_macro = dt[4]
        tempt = dt[5]
        g = Group(zapi, gp)
        t = Template(zapi, tempt)
        h = Host(zapi,host,ip1,ip2,g.getGroup(),v_macro,t.getTemplate())
        bar.update(cont)
        h.setHost()

        bar.finish()


