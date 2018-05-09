from biblioteca import *
import os

op= 0

while op != 4:
    os.system('clear')
    banner()
    menu1()
    op = int(input("\n\tDigite uma Opção:"))

    if op == 1:
        arq = input("\n\tDigite o caminho do arquivo: ")
        HostImport(arq)
        sys.exit(1)

    elif op == 2:

        os.system('clear')
        banner()
        submenuitem()


        op1 = int(input("\n\tDigite uma Opção:"))

        if op1 == 1:
            hostname = input("\n\tDigite o hostname: ")
            I = Item(zapi, hostname)
            I.LNsuportados()
            sys.exit(1)

        elif op1 == 2:
            hostname = input("\n\tDigite o hostname: ")
            I = Item(zapi, hostname)
            I.LQNsuportados()
            sys.exit(1)
        elif op1 == 3:
            hostname = input("\n\tDigite o hostname: ")
            I = Item(zapi, hostname)
            I.setUpdate()
            sys.exit(1)

        else:
            sys.exit(1)
    else:

        print("exit !!!")
        sys.exit(1)

print("Fim do Programa|==>")





