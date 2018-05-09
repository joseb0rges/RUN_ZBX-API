from termcolor import *

def banner():
    print(colored('''


\t  _____     _     _     _           _    ____ ___ 
\t |__  /__ _| |__ | |__ (_)_  __    / \  |  _ \_ _|
\t   / // _` | '_ \| '_ \| \ \/ /   / _ \ | |_) | | 
\t  / /_ (_| | |_) | |_) | |>  <   / ___ \|  __/| | 
\t /____\__,_|_.__/|_.__/|_/_/\_\ /_/   \_\_|  |___|                                                 
    ''', 'red', attrs=['bold']))
    print("")


def menu1():
    print(colored('''
\t\t\t [1] - Import - Hosts  
\t\t\t [2] - Update - Items  
\t\t\t [3] - Reports         
\t\t\t [4] - Exit            

    ''','blue', attrs=['bold']))



def submenuitem():
    print(colored('''
\t\t\t   1 - List unsupported items    |
\t\t\t   2 - Quantity unsupported items|
\t\t\t   3 - Disable unsupported items |
\t\t\t   4 - Exit       |

    ''','blue', attrs=['bold']))
