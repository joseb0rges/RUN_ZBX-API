import csv
from Biblioteca import *
from ITService import  ITservice
from Item import  Item
from Interface import Interface
import pyprog
from time import sleep


class Import:

    def __init__(self,zapi,file):

        self.__zapi = zapi
        self.__file = file


    def ImportHost(self):

        dataset = csv.reader(open(self.__file,'r'))

        for data in dataset:

            host = data[0]
            ip = data[1]
            group = data[2]
            #template = data[3]

            group_id = Group(self.__zapi,group)
            #template_id = Template(self.__zapi,template)

            #H = Host(self.__zapi,host,group_id.getGroupID(),template_id.getTemplate())
            H = Host(self.__zapi,host,group_id.getGroupID())
            H.setHost(ip)



    def ImportSLA(self):

        dataset = csv.reader(open(self.__file,'r'))

        for data in dataset:

            host = data[0]
            group = data[1]
            item = data[2]

            its = ITservice(self.__zapi,host,group)
            i = Item(self.__zapi,host)
            its.setChild_itservices(i.getItem_triggerid(item))





    def ImportDescriptionHost(self):

        dataset = csv.reader(open(self.__file,'r'))

        for data in dataset:

            host = data[0]
            description = data[1]

            h = Host(self.__zapi,host,host_group_id=None,template_id=None)
            upd = UpdateHost(self.__zapi,h.getHostID())
            upd.updateDescription(description,host)




    def ImportVisibleHostName(self):

        dataset = csv.reader(open(self.__file,'r'))

        for data in dataset:

            vhost = data[0]
            host = data[1]

            h = Host(self.__zapi,host,host_group_id=None)
            upd = UpdateHost(self.__zapi,h.getHostID())
            upd.updateHostName(vhost,host)




    def ImportNewInterface(self):

        dataset = csv.reader(open(self.__file,'r'))

        for data in dataset:

            nip = data[1]
            host = data[0]

            h = Host(self.__zapi,host,host_group_id=None)
            upd = Interface(self.__zapi,h.getHostID())
            upd.setInterface(nip)




    def contar_linhas_arquivo(self,file):

        with open(self.__file, 'r') as f:
            t = len(f.readlines())
            f.close()
            return (t)

    def progresso(self,x):

        prog = pyprog.ProgressBar("\tImportando Hosts  ", "[OK]", x)
        prog.update()

        for i in range(x):
            sleep(0.1)
            prog.set_stat(i + 1)
            prog.update()

        prog.end()
