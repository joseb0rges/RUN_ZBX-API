

class Host:


    def __init__(self, zapi,hostname,host_group_id,template_id):

        self.__zapi = zapi
        self.__hostname = hostname
        self.__host_group_id = host_group_id
        self.__template_id = template_id

    def setHost(self,hostip):

            self.__zapi.host.create(

                host=self.__hostname,
                interfaces=[{
                    "type":1,
                    "main": 1,
                    "useip":1,
                    "ip":hostip,
                    "dns":"",
                    "port":"10050"
                }],
                groups=[{
                    "groupid":self.__host_group_id
                }],
                templates=self.__template_id)

            print('\t\n Host: {} Criado com Sucesso .... [OK] '.format(self.__hostname))


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














