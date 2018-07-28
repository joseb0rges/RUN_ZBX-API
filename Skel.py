from termcolor import *

def banner():
    print(colored('''


\t ██████╗ ██╗   ██╗███╗   ██╗    ███████╗██████╗ ██╗  ██╗      █████╗ ██████╗ ██╗
\t ██╔══██╗██║   ██║████╗  ██║    ╚══███╔╝██╔══██╗╚██╗██╔╝     ██╔══██╗██╔══██╗██║
\t ██████╔╝██║   ██║██╔██╗ ██║      ███╔╝ ██████╔╝ ╚███╔╝█████╗███████║██████╔╝██║
\t ██╔══██╗██║   ██║██║╚██╗██║     ███╔╝  ██╔══██╗ ██╔██╗╚════╝██╔══██║██╔═══╝ ██║
\t ██║  ██║╚██████╔╝██║ ╚████║    ███████╗██████╔╝██╔╝ ██╗     ██║  ██║██║     ██║
\t ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                 
    ''', 'red', attrs=['bold']))
    print("")

def menup():
    print(colored('''
\t\t\t [1] - Imports 
\t\t\t [2] - Updates  
\t\t\t [3] - Reports         
\t\t\t [4] - Exit            

    ''','blue', attrs=['bold']))

def submenu1():
    print(colored('''
    
    \t\t\t [1] - Hosts
    \t\t\t [2] - ITService
    \t\t\t [3] - Description           
    \t\t\t [4] - Exit            

        ''', 'blue', attrs=['bold']))

def submenu2():

    print(colored('''
        \t\t\t [1] - Items           
        \t\t\t [2] - Exit            
            ''', 'blue', attrs=['bold']))


def submenu3():

    print(colored('''
 
        \t\t\t [1] - Items           
        \t\t\t [3] - Exit            
 
            ''', 'blue', attrs=['bold']))

def submenuitem():
    print(colored('''
\t\t\t   [1] - Disable unsupported items|
\t\t\t   [2] - Exit       |

    ''','blue', attrs=['bold']))


def submenuiteml():
    print(colored('''
\t\t\t   [1] - List unsupported items    |
\t\t\t   [2] - Quantity unsupported items|
\t\t\t   [3] - Exit       |

    ''','blue', attrs=['bold']))
