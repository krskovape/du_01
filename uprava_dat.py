import json
from json.decoder import JSONDecodeError

#otevírání souboru 
try:
    #!!! data bez Prahy a se statutárními městy !!!
    with open("data_ukol1.json", encoding="utf-8") as soubor:
         data = json.load(soubor)
except FileNotFoundError:
    print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
    quit()
except PermissionError:
    print("Program nemá přístup k zápisu výstupních souborů.")
    quit()
except JSONDecodeError:
    print("Načtený vstupní soubor není platný JSON.")
    quit()

#změna názvu krajů a okresů
for feature in data:

    #kraje
    if feature ["krajLabel"] == "Jihočeský kraj":
        feature ["krajLabel"] = "Jihočeský"
    if feature ["krajLabel"] == "Jihomoravský kraj":
        feature ["krajLabel"] = "Jihomoravský"
    if feature ["krajLabel"] == "Karlovarský kraj":
        feature ["krajLabel"] = "Karlovarský"
    if feature ["krajLabel"] == "Královéhradecký kraj":
        feature ["krajLabel"] = "Královéhradecký"
    if feature ["krajLabel"] == "Liberecký kraj":
        feature ["krajLabel"] = "Liberecký"
    if feature ["krajLabel"] == "Moravskoslezský kraj":
        feature ["krajLabel"] = "Moravskoslezský"
    if feature ["krajLabel"] == "Olomoucký kraj":
        feature ["krajLabel"] = "Olomoucký"
    if feature ["krajLabel"] == "Pardubický kraj":
        feature ["krajLabel"] = "Pardubický"
    if feature ["krajLabel"] == "Plzeňský kraj":
        feature ["krajLabel"] = "Plzeňský"
    if feature ["krajLabel"] == "Středočeský kraj":
        feature ["krajLabel"] = "Středočeský"
    if feature ["krajLabel"] == "Ústecký kraj":
        feature ["krajLabel"] = "Ústecký"
    if feature ["krajLabel"] == "Kraj Vysočina":
        feature ["krajLabel"] = "Vysočina"
    if feature ["krajLabel"] == "Zlínský kraj":
        feature ["krajLabel"] = "Zlínský"
    if feature ["krajLabel"] == "Kraj Praha":
        feature ["krajLabel"] = "Praha"

    #okresy
    if feature ["okresLabel"] == "okres Benešov":
        feature ["okresLabel"] = "Benešov"
    if feature ["okresLabel"] == "okres Beroun":
        feature ["okresLabel"] = "Beroun"
    if feature ["okresLabel"] == "okres Blansko":
        feature ["okresLabel"] = "Blansko"
    if feature ["okresLabel"] == "okres Brno-město":
        feature ["okresLabel"] = "Brno-město"
    if feature ["okresLabel"] == "okres Brno-venkov":
        feature ["okresLabel"] = "Brno-venkov"
    if feature ["okresLabel"] == "okres Bruntál":	
        feature ["okresLabel"] = "Bruntál"
    if feature ["okresLabel"] == "okres Břeclav":	
        feature ["okresLabel"] = "Břeclav"
    if feature ["okresLabel"] == "okres Česká Lípa":	
        feature ["okresLabel"] = "Česká Lípa"
    if feature ["okresLabel"] == "okres Český Krumlov":	
        feature ["okresLabel"] = "Český Krumlov"
    if feature ["okresLabel"] == "okres Děčín":	
        feature ["okresLabel"] = "Děčín"
    if feature ["okresLabel"] == "okres Domažlice":	
        feature ["okresLabel"] = "Domažlice"
    if feature ["okresLabel"] == "okres Frýdek-Místek":	
        feature ["okresLabel"] = "Frýdek-Místek"
    if feature ["okresLabel"] == "okres Havlíčkův Brod":	
        feature ["okresLabel"] = "Havlíčkův Brod"
    if feature ["okresLabel"] == "okres Hodonín":	
        feature ["okresLabel"] = "Hodonín"
    if feature ["okresLabel"] == "okres Hradec Králové":
        feature ["okresLabel"] = "Hradec Králové"
    if feature ["okresLabel"] == "okres Cheb":
        feature ["okresLabel"] = "Cheb"	
    if feature ["okresLabel"] == "okres Chomutov":
        feature ["okresLabel"] = "Chomutov"	
    if feature ["okresLabel"] == "okres Chrudim":
        feature ["okresLabel"] = "Chrudim"
    if feature ["okresLabel"] == "okres Jablonec nad Nisou":
        feature ["okresLabel"] = "Jablonec nad Nisou"
    if feature ["okresLabel"] == "okres Jeseník":
        feature ["okresLabel"] = "Jeseník"	
    if feature ["okresLabel"] == "okres Jičín":
        feature ["okresLabel"] = "Jičín"	
    if feature ["okresLabel"] == "okres Jihlava":
        feature ["okresLabel"] = "Jihlava"	
    if feature ["okresLabel"] == "okres Jindřichův Hradec":
        feature ["okresLabel"] = "Jindřichův Hradec"	
    if feature ["okresLabel"] == "okres Karlovy Vary":
        feature ["okresLabel"] = "Karlovy Vary"	
    if feature ["okresLabel"] == "okres Karviná":
        feature ["okresLabel"] = "Karviná"	
    if feature ["okresLabel"] == "okres Kladno":
        feature ["okresLabel"] = "Kladno"	
    if feature ["okresLabel"] == "okres Klatovy":
        feature ["okresLabel"] = "Klatovy"	
    if feature ["okresLabel"] == "okres Kolín":
        feature ["okresLabel"] = "Kolín"	
    if feature ["okresLabel"] == "okres Kroměříž":
        feature ["okresLabel"] = "Kroměříž"	
    if feature ["okresLabel"] == "okres Kutná Hora":
        feature ["okresLabel"] = "Kutná Hora"	
    if feature ["okresLabel"] == "okres Liberec":
        feature ["okresLabel"] = "Liberec"	
    if feature ["okresLabel"] == "okres Litoměřice":
        feature ["okresLabel"] = "Litoměřice"	
    if feature ["okresLabel"] == "okres Louny":
        feature ["okresLabel"] = "Louny"	
    if feature ["okresLabel"] == "okres Mělník":
        feature ["okresLabel"] = "Mělník"	
    if feature ["okresLabel"] == "okres Mladá Boleslav":
        feature ["okresLabel"] = "Mladá Boleslav"	
    if feature ["okresLabel"] == "okres Most":
        feature ["okresLabel"] = "Most"	
    if feature ["okresLabel"] == "okres Náchod":
        feature ["okresLabel"] = "Náchod"	
    if feature ["okresLabel"] == "okres Nový Jičín":
        feature ["okresLabel"] = "Nový Jičín"	
    if feature ["okresLabel"] == "okres Nymburk":
        feature ["okresLabel"] = "Nymburk"	
    if feature ["okresLabel"] == "okres Olomouc":
        feature ["okresLabel"] = "Olomouc"	
    if feature ["okresLabel"] == "okres Opava":
        feature ["okresLabel"] = "Opava"	
    if feature ["okresLabel"] == "okres Ostrava-město":
        feature ["okresLabel"] = "Ostrava-město"	
    if feature ["okresLabel"] == "okres Pardubice":
        feature ["okresLabel"] = "Pardubice"	
    if feature ["okresLabel"] == "okres Pelhřimov":
        feature ["okresLabel"] = "Pelhřimov"	
    if feature ["okresLabel"] == "okres Písek":
        feature ["okresLabel"] = "Písek"	
    if feature ["okresLabel"] == "okres Plzeň-jih":
        feature ["okresLabel"] = "Plzeň-jih"	
    if feature ["okresLabel"] == "okres Plzeň-město":
        feature ["okresLabel"] = "Plzeň-město"	
    if feature ["okresLabel"] == "okres Plzeň-sever":
        feature ["okresLabel"] = "Plzeň-sever"	
    if feature ["okresLabel"] == "okres Praha":
        feature ["okresLabel"] = "Praha"	
    if feature ["okresLabel"] == "okres Praha-východ":
        feature ["okresLabel"] = "Praha-východ"	
    if feature ["okresLabel"] == "okres Praha-západ":
        feature ["okresLabel"] = "Praha-západ"	
    if feature ["okresLabel"] == "okres Prachatice":
        feature ["okresLabel"] = "Prachatice"	
    if feature ["okresLabel"] == "okres Prostějov":
        feature ["okresLabel"] = "Prostějov"	
    if feature ["okresLabel"] == "okres Přerov":
        feature ["okresLabel"] = "Přerov"
    if feature ["okresLabel"] == "okres Příbram":
        feature ["okresLabel"] = "Příbram"	
    if feature ["okresLabel"] == "okres Rakovník":
        feature ["okresLabel"] = "Rakovník"	
    if feature ["okresLabel"] == "okres Rokycany":
        feature ["okresLabel"] = "Rokycany"	
    if feature ["okresLabel"] == "okres Rychnov nad Kněžnou":
        feature ["okresLabel"] = "Rychnov nad Kněžnou"	
    if feature ["okresLabel"] == "okres Semily":
        feature ["okresLabel"] = "Semily"	
    if feature ["okresLabel"] == "okres Sokolov":
        feature ["okresLabel"] = "Sokolov"	
    if feature ["okresLabel"] == "okres Strakonice":
        feature ["okresLabel"] = "Strakonice"	
    if feature ["okresLabel"] == "okres Svitavy":
        feature ["okresLabel"] = "Svitavy"	
    if feature ["okresLabel"] == "okres Šumperk":
        feature ["okresLabel"] = "Šumperk"	
    if feature ["okresLabel"] == "okres Tábor":
        feature ["okresLabel"] = "Tábor"	
    if feature ["okresLabel"] == "okres Tachov":
        feature ["okresLabel"] = "Tachov"	
    if feature ["okresLabel"] == "okres Teplice":
        feature ["okresLabel"] = "Teplice"	
    if feature ["okresLabel"] == "okres Trutnov":
        feature ["okresLabel"] = "Trutnov"	
    if feature ["okresLabel"] == "okres Třebíč":
        feature ["okresLabel"] = "Třebíč"	
    if feature ["okresLabel"] == "okres Uherské Hradiště":
        feature ["okresLabel"] = "Uherské Hradiště"	
    if feature ["okresLabel"] == "okres Ústí nad Labem":
        feature ["okresLabel"] = "Ústí nad Labem"	
    if feature ["okresLabel"] == "okres Ústí nad Orlicí":
        feature ["okresLabel"] = "Ústí nad Orlicí"	
    if feature ["okresLabel"] == "okres Vsetín":
        feature ["okresLabel"] = "Vsetín"
    if feature ["okresLabel"] == "okres Vyškov":
        feature ["okresLabel"] = "Vyškov"	
    if feature ["okresLabel"] == "okres Zlín":
        feature ["okresLabel"] = "Zlín"  	
    if feature ["okresLabel"] == "okres Znojmo":
        feature ["okresLabel"] = "Znojmo"	
    if feature ["okresLabel"] == "okres Žďár nad Sázavou":
        feature ["okresLabel"] = "Žďár nad Sázavou"	
    if feature ["okresLabel"] == "okres České Budějovice":
        feature ["okresLabel"] = "České Budějovice"

#výstupní .json
with open('data_upravena.json', 'w', encoding ='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii = False)