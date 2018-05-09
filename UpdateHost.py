
class UpdateHost(object):


    def __init__(self,zapi,hostname):

            self.__zapi = zapi
            self.__hostname = hostname


    def updateDescription(self,descricao):

        try:

            self.__zapi.host.update(

                hostid=self.getHostID(),
                description=descricao

            )

        except Exception as e:
            print("Error: {}".format(e))

    def updateHostName(self,hostnew):

        try:
            self.__zapi.host.update(

            hostid=self.getHostID(),
            host=hostnew
            )
        except Exception as e:
            print("Error: {}".format(e))





