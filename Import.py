import csv
from biblioteca import *
from ITService import  ITservice
from Item import  Item


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
            template = data[3]

            group_id = Group(self.__zapi,group)
            template_id = Template(self.__zapi,template)

            H = Host(self.__zapi,host,group_id.getGroupID(),template_id.getTemplate())
            H.setHost(ip)


    def ImportSLA(self):

        dataset = csv.reader(open(self.__file,'r'))

        for data in dataset:

            host = data[0]
            group = data[1]
            item = data[2]

            its = ITservice(self.__zapi,host,group)
            i = Item(self.__zapi,host)
            its.setFather_itservice()
            its.setChild_itservices()

            its.setChild_itservice_trigger(i.getItem_triggerid(item))



    def ImportDescriptionHost(self):

        dataset = csv.reader(open(self.__file,'r'))

        for data in dataset:

            host = data[0]
            description = data[1]

            h = Host(self.__zapi,host,host_group_id=None,template_id=None)
            upd = UpdateHost(self.__zapi,h.getHostID())
            upd.updateDescription(description,host)

