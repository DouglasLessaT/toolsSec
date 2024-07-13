import os

# Solicita ao usuário se deseja instalar (Y) ou desinstalar (N) o programa
choice = input('[+] to install press (Y) to uninstall press (N) >> ')

# Definindo uma função abreviada para executar comandos no sistema
run = os.system

# Se o usuário escolher 'Y' ou 'y', o programa será instalado
if str(choice) =='Y' or str(choice)=='y':
    # Concede permissões de execução ao arquivo autoTOR.py
    run('chmod 777 autoTOR.py')
    # Cria um diretório /usr/share/aut
    run('mkdir /usr/share/aut')
    # Copia o arquivo autoTOR.py para /usr/share/aut/
    run('cp autoTOR.py /usr/share/aut/autoTOR.py')

    # Cria um script shell (aut) em /usr/bin/ para facilitar a execução do programa
    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/autoTOR.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    
    # Concede permissões de execução aos arquivos aut e autoTOR.py
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/autoTOR.py')
    
    # Mensagem de conclusão da instalação
    print('''\n\ncongratulation auto Tor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')

# Se o usuário escolher 'N' ou 'n', o programa será desinstalado
if str(choice)=='N' or str(choice)=='n':
    # Remove o diretório /usr/share/aut
    run('rm -r /usr/share/aut ')
    # Remove o script aut de /usr/bin/
    run('rm /usr/bin/aut ')
    # Mensagem de conclusão da desinstalação
    print('[!] now Auto Tor Ip changer  has been removed successfully')