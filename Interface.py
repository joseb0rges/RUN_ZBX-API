
from termcolor import colored

class Interface:

    def __init__(self,zapi,hostid):

        self.__zapi = zapi
        self.__hostid = hostid


    def setInterface(self,ip):

        try:
            self.__zapi.hostinterface.create(

                hostid=self.__hostid,
                dns="",
                ip=ip,
                main=0,
                port="161",
                type=2,
                useip=1
            )


        except Exception as e:
                print(colored("\t\nError: {}".format(e),'red'))



