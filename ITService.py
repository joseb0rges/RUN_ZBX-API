import sys


class ITservice:

    def __init__(self,zapi,hostname):
        self.__zapi = zapi
        self.__hostname = hostname
        #self.__group = group

    """
    def setFather_itservice(self):

        self.__zapi.service.create(name=self.__group,
                                   algorithm=1,
                                   showsla=1,
                                   goodsla=99.70,
                                   sortorder=1)

        print("Item de Serviço Pai : {}, Criado com sucesso .... [OK]".format(self.__group))


    """

    def get_FatherItservice_pid(self,group):

        parentID = self.__zapi.service.get(selectParent="extend",
                                selectTrigger="extend",
                                expandExpression="true",
                                filter={"name":group})[0]['serviceid']

        return parentID

    def getChild_itservice_pid(self):

        parentNameChild = self.__zapi.service.get(selectParent="extend",
                                                  selectTrigger="extend",
                                                  expandExpression="true",
                                                  filter={"name": self.__hostname},output='extend')



        return parentNameChild




    def setChild_itservices(self,group,triggerid):

        idservice = self.getChild_itservice_pid()

        if len(idservice) == 0:


                self.__zapi.service.create(name=self.__hostname,
                                        algorithm=1,
                                        showsla=1,
                                        goodsla=99.70,
                                        sortorder=0,
                                        parentid=self.get_FatherItservice_pid(group),
                                        triggerid=triggerid)

                print("Serviços de TI do Host: {} | Criado com sucesso .... [OK]".format(self.__hostname))

        else:

                 print("Erro O Serviço de TI do Host: {} | já existe !!!".format(self.__hostname))

    """
    def setChild_itservice_trigger(self,triggerid):

        self.__zapi.service.create(name=self.__hostname,
                        algorithm=1,
                        showsla=1,
                        goodsla=99.70,
                        sortorder=1,
                        parentid=self.getChild_itservice_pid(),
                        triggerid=triggerid)

        print(" Trigger de item de Serviço  : {}, Criado com sucesso .... [OK]".format(self.__hostname))

    """