
class ITservice:

    def __init__(self,zapi,hostname,group):
        self.__zapi = zapi
        self.__hostname = hostname
        self.__group = group


    def setFather_itservice(self):

        self.__zapi.service.create(name=self.__group,
                                   algorithm=1,
                                   showsla=1,
                                   goodsla=99.99,
                                   sortorder=1)

        print("Item de Serviço Pai : {}, Criado com sucesso .... [OK]".format(self.__group))

    def get_FatherItservice_pid(self,group):

        parentID = self.__zapi.service.get(selectParent="extend",
                                selectTrigger="extend",
                                expandExpression="true",
                                filter={"name":self.__group})[0]['serviceid']

        return parentID


    def setChild_itservices(self):

        self.__zapi.service.create(name=self.__hostname,
                                   algorithm=1,
                                   showsla=1,
                                   goodsla=99.99,
                                   sortorder=1,
                                   parentid=self.get_FatherItservice_pid(self.__group))

        print("Item de Serviço Filho : {}, Criado com sucesso .... [OK]".format(self.__hostname))

    def getChild_itservice_pid(self):

        parentIDChild = self.__zapi.service.get(selectParent="extend",
                                                selectTrigger="extend",
                                                expandExpression="true",
                                                filter={"name":self.__hostname})[0]['serviceid']


        return parentIDChild

    def setChild_itservice_trigger(self,triggerid):

        self.__zapi.service.create(name=self.__hostname,
                        algorithm=1,
                        showsla=1,
                        goodsla=99.99,
                        sortorder=1,
                        parentid=self.getChild_itservice_pid(),
                        triggerid=triggerid)

        print(" Trigger de item de Serviço  : {}, Criado com sucesso .... [OK]".format(self.__hostname))