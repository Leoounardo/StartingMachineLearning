from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

ct = "https://csgoempire.com/img/coin-ct.d399ffd4.png"
tr = "https://csgoempire.com/img/coin-t.37ae39bf.png"
bonus = "https://csgoempire.com/img/coin-bonus.806c9d88.png"
value = 0

deciprim = []
deci = []
nona = []
oit = []
setim = []
sexta = []
quinta = []
quarta = []
terca = []
segunda = []
prim = []
lista = []
seed = 2058
driver = webdriver.Chrome(r"C:\Users\ileoo\Desktop\ia\chromedriver")

while seed > 2030:
    url = "https://csgoempire.com/history?seed={}".format(seed)
    driver.get(url)
    sleep(10)
    lista = driver.find_elements_by_css_selector('div.bg-black-a.text-center.border.border-slate-dark.py-2.px-3.rounded-lg')
    print("Estamos na seed {}".format(seed))
    print("tamanha {}".format(len(lista)))
    a = (len(lista)//11)*11
    print("vai ate a posição {}".format(a))
    cont = 11
    cont2 = 0

    for li in lista:
        if cont2 == a:
            break
        
        imagem = li.find_element_by_css_selector('img').get_attribute('src')
        
        if imagem == ct:
            value = 1
        elif imagem == tr:
            value = 2
        else:
            value = 3

        if cont == 11:
            deciprim.append(value)
        elif cont == 10:
            deci.append(value)
        elif cont == 9:
            nona.append(value)
        elif cont == 8:
            oit.append(value)
        elif cont == 7:
            setim.append(value)
        elif cont == 6:
            sexta.append(value)
        elif cont == 5:
            quinta.append(value)
        elif cont == 4:
            quarta.append(value)
        elif cont == 3:
            terca.append(value)
        elif cont == 2:
            segunda.append(value)
        elif cont == 1:
            prim.append(value)
            cont = 12
        cont -= 1
        cont2 += 1
    print("-   Coletado!")
    df = pd.DataFrame(data={"primeira": prim, "segunda": segunda, "terceira": terca, "quarta": quarta, "quinta": quinta,"sexta": sexta, "setima": setim, "oitava": oit, "nona": nona, "decima": deci, "deciprimeira": deciprim})
    df.to_excel(r'C:\Users\ileoo\Desktop\ia\beleza{}.xlsx'.format(seed), index=False, header=True)
    lista = []
    deciprim = []
    deci = []
    nona = []
    oit = []
    setim = []
    sexta = []
    quinta = []
    quarta = []
    terca = []
    segunda = []
    prim = []
    lista = []
    seed -= 1


