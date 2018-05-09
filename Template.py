
class Template():

    def __init__(self,zapi,template):

        self.__zapi = zapi
        self.__template = template


    def getTemplate(self):

        template = self.__zapi.template.get(filter={"name": self.__template})
        if len(template) == 0:
            print('ERROR:O nome de template não existe !!!.')

        else:
            return template[0]['templateid']
