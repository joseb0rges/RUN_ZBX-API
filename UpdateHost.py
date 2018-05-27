
class UpdateHost(object):


    def __init__(self,zapi,hostid):

            self.__zapi = zapi
            self.__hostid = hostid


    def updateDescription(self,descricao,host):

        try:

            self.__zapi.host.update(

                hostid=self.__hostid,
                description=descricao

            )
            print('O host : {} foi atualizado com a descrição: {} '.format(host, descricao))


        except Exception as e:
            print("Error: {}".format(e))

    # def updateHostName(self,hostnew):
    #
    #     try:
    #         self.__zapi.host.update(
    #
    #         hostid=self.getHostID(),
    #         host=hostnew
    #         )
    #     except Exception as e:
    #         print("Error: {}".format(e))





