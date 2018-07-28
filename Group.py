
class Group():

    def __init__(self,zapi,group):

        self.__zapi = zapi
        self.__group = group


    def getGroupID(self):

        group = self.__zapi.hostgroup.get(filter={"name": self.__group})
        if len(group) == 0:
            print('ERROR:O nome de grupo não existe !!!.')
        else:
            return group[0]['groupid']
