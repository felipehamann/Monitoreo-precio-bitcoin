#importacion librerias necesarios
import time
import requests, bs4
from colorama import Fore, init

##inicio  
init()
print(Fore.RED + "Bienvenido al monitoreo del precio de Bitcoin en Tiempo Real.")
print(Fore.RED + "CARGANDO.....")

while True:
    
    pet = requests.get("https://coinmarketcap.com/currencies/bitcoin/") #pagina web utilizada
    
    scrap = bs4.BeautifulSoup(pet.content, "lxml") #conversion html de la pagina a formato lxml
 
    precio = scrap.select('div .priceValue___11gHJ') #busqueda del valor bitcoin
    

    print (Fore.YELLOW + "El precio del Bitcoin es: " + Fore.WHITE + str(precio)[33:43]) #ajustar etiqueta div, a solamente el valor actual del bitcoin. 

    time.sleep(5) # espera 5 segundos entre cada busqueda
 