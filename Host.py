

class Host:


    def __init__(self, zapi, hostname,host_group_id,template_id):

        self.__zapi = zapi
        self.__hostname = hostname
        self.__host_group_id = host_group_id
        self.__template_id = template_id

    def setHost(self,hostip1,hostip2,vmacro):

            self.__zapi.host.create(

                host=self.__hostname,
                interfaces=[{
                    "type":1,
                    "main": 1,
                    "useip":1,
                    "ip":hostip1,
                    "dns":"",
                    "port":"10050"
                },{
                    "type": 2,
                    "main": 1,
                    "useip": 1,
                    "ip":hostip2,
                    "dns": "",
                    "port": "161"

                }],

                macros=[{
                    "macro":"{$SNMP_COMMUNITY}",
                    "value":vmacro
                }],
                groups=[{
                    "groupid":self.__host_group_id
                }],
                templates=self.__template_id)

            print('\t\nHost: {} criado com sucesso .... [OK] '.format(self.__hostname))



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














