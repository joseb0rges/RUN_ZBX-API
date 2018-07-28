#-*- coding:utf-8 -*-
import sys

from termcolor import colored


class Item(object):

    def __init__(self, zapi, hostname):

        self.__zapi=zapi
        self.__hostname=hostname

    def getItems(self,hostname):
        host = self.__zapi.host.get(filter={"host": self.__hostname})
        if len(host) == 0:
            print(colored('\n\tERROR:O nome de host não existe !!!.','red'))
        else:
            items = self.__zapi.item.get(monitored=1,
                                  webitems=1,
                                  hostids=host[0]['hostid'],
                                  filter={"state": 1},
                                  output='extend')
            if len(items) == 0:
                print('\n\t Nenhum item encontrado !!!.')
                sys.exit(1)
            else:

                return items


    def getItem_triggerid(self,item):

        hostid = self.__zapi.host.get(filter={"host": self.__hostname})[0]['hostid']
        triggerId = self.__zapi.item.get(output="triggers",
                                  hostids=hostid,
                                  with_triggers=True,
                                  selectTriggers="triggers",
                                  filter={"name": item})[0]['triggers'][0]['triggerid']

        return triggerId

    def DisableItems(self):
        try:
             for item in self.getItems(self.__hostname):
                item.setdefault('name', 'unkonown')
                item.setdefault('error', 'unkonown')
                self.__zapi.item.update(
                    itemid=item['itemid'],
                    status=1
                 )

             print("\n\t Item: {} Desabilitado com sucesso ..... [OK] ".format(item['name']))

        except Exception as e:
                print(colored("\n\tError: {}".format(e),'red'))

    def LNSupported(self):

        for item in self.getItems(self.__hostname):
            item.setdefault('name', 'unkonown')
            item.setdefault('error', 'unkonown')
            print("\n\tNome: {} Error: {}".format(item['name'], item['error']))

    def LQNSupported(self):
        print('\n\tO host possui: ' + str(len(self.getItems(self.__hostname))) + ' items não suportados \n')
