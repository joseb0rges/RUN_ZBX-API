
     ██████╗ ██╗   ██╗███╗   ██╗    ███████╗██████╗ ██╗  ██╗      █████╗ ██████╗ ██╗
	 ██╔══██╗██║   ██║████╗  ██║    ╚══███╔╝██╔══██╗╚██╗██╔╝     ██╔══██╗██╔══██╗██║
	 ██████╔╝██║   ██║██╔██╗ ██║      ███╔╝ ██████╔╝ ╚███╔╝█████╗███████║██████╔╝██║
	 ██╔══██╗██║   ██║██║╚██╗██║     ███╔╝  ██╔══██╗ ██╔██╗╚════╝██╔══██║██╔═══╝ ██║
	 ██║  ██║╚██████╔╝██║ ╚████║    ███████╗██████╔╝██╔╝ ██╗     ██║  ██║██║     ██║
	 ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝


**RUN ZBX-API** *é um projeto que tem por finalidade a interação com API do Zabbix, afim de automatiza algumas tarefas que se fossem realizadas
pela interface web do sistema iria demandar um certo tempo*

**Funcionalidades:**

- Importação de Ativos em massa.
- Importação de Descrição em massa.
- Importação de SLA.
- Liste e Desabilite items não suportados .


**Personalização de Metodos.**

É possivel customizar os metodos de acordo com sua necessidade .

**Adicionar segunda interface ao Ativo.**

				{
                    "type": 2,
                    "main": 1,
                    "useip": 1,
                    "ip":hostip2,
                    "dns": "",
                    "port": "161"

                }

**Adicionar uma macro.**

		  macros=[{
                    "macro":"{$SNMP_COMMUNITY}",
                    "value":vmacro
                }],


*obs => É possivel realizar tais alterações, modificando o JSON dos metodos.*

#### Pre-requisitos 

##### Instalar bibliotecas necessarias.

- pip install pyzabbix

- pip install termcolor


#### Execultando projeto

python3 ZabbixAPIUltius.py



#### Referencias

https://www.zabbix.com/documentation/3.0/pt/manual/api





