import time
import os
import subprocess

try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip, shell=True')
    if str ('install ok installesd') in (check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip not installed')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')

try:
    import requests
except Exception:
    print('[+] python3 requestes is not instaled')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 request is installed')

try:
    check_tor = subprocess.check_output(' which tor', shell = True)
except subprocess.CalledProcessError:
    print('[+] Tor is not Installed')
    subprocess.check_output('sudo apt update', shell = True)
    print("[!] Updating the system ...")
    subprocess.check_output('sudo apt tor -y', shell = True)
    print('[!] installing Tor')
    print('[!] Tor is installed succesfully')
os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text
# Função para mudar o endereço IP
def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

# Mensagem de apresentação
print('''\033[1;32;40m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.1
from mrFD
''')
print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

# Inicia o serviço Tor
os.system("service tor start")

# Pausa por 3 segundos
time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")

# Solicita ao usuário os parâmetros de tempo e número de alterações de IP desejados
x = input("[+] time to change Ip in Sec [type=60] >> ")
lin = input("[+] how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>")

# Se o número de alterações for 0, entra em um loop infinito, senão executa o número especificado de mudanças.
if int(lin) == int(0):
    while True:
        try:
            time.sleep(int(x))
            change()
        except KeyboardInterrupt:
            print('\nauto tor is closed ')
            quit()
else:
    for i in range(int(lin)):
        time.sleep(int(x))
        change()