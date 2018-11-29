from termcolor import colored


class Host:


    #def __init__(self, zapi,hostname,host_group_id,template_id):
    def __init__(self, zapi,hostname,host_group_id):

        self.__zapi = zapi
        self.__hostname = hostname
        self.__host_group_id = host_group_id
        #self.__template_id = template_id

    def setHost(self,hostip):
        try:
            self.__zapi.host.create(

                host=self.__hostname,
                interfaces=[{
                    "type":1, # - 1
                    "main": 1,
                    "useip":1,
                    "ip":hostip,
                    "dns":"",
                    "port":"161"
                }],
                groups=[{
                    "groupid":self.__host_group_id
                }],

                 macros=[{
                "macro":"{$SNMP_COMMUNITY}",
                "value":"comunity"
                }])

                #templates=self.__template_id)

            print(colored('\t\n Host: {} criado com sucesso .... [OK] '.format(self.__hostname),'green'))

        except Exception as e:
                print(colored("\t\nError: {}".format(e),'red'))


    def getHostID(self):

        try:
            hostid = self.__zapi.host.get(filter={"host": self.__hostname})
            return hostid[0]['hostid']

        except Exception as e:
            print("Error: {}".format(e))

    def getHostNome(self):

        try:

            hostname = self.__zapi.host.get(filter={"host": self.__hostname})
            return hostname[0]['host']

        except Exception as e:
            print("Error: {}".format(e))
