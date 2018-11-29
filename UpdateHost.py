
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

    def updateHostName(self,vhost,host):

         try:
             self.__zapi.host.update(

             hostid=self.__hostid,
             name=vhost

             )
             print('O host : {} foi atualizado com a descrição: {} '.format(host, vhost))
         except Exception as e:
             print("Error: {}".format(e))


    def updateInterface(self,nip,host):

        try:

            self.__zapi.host.update(

                hostid=self.__hostid,
                    interfaces=[{
                        "type":1, # - 1
                        "main": 1,
                        "useip":1,
                        "ip":nip,
                        "dns":""
                    }]

            )
            print('O host : {} foi atualizado com a interface: {} '.format(host, nip))


        except Exception as e:
            print("Error: {}".format(e))
