# Prohlížeč obcí a měst

Zde je popsáno, jak program "Prohlížeč obcí a měst" funguje a jak je strukturován. 

### Sturktura
V souboru "ultrafiltr.py" jsou definovány potřebné třídy a funkce, které jsou následně použity v grafickém rozhraní "superview.qml". 

K jednotlivým vlastnostem prvku v seznamu přistupujeme pomocí rolí. Ty dědí od třídy "enum" a pracuje s nimi funkce "data" a "roleNames". 

Následně jsou definovány proměnné používané v programu. Funkce get_min/max_po a set_min/max_po nastavují hodnotu počtu obyvatel, která je uživatelem upravována buď pomocí posuvníku, tak pomocí textových polí. V případě změny jednoho, dojde k autualizování dané hodnoty u druhého ukazatele. Totéž platí pro filtrování sídel na základě rozlohy a toho, zda se jedná o obec či město. 

Funkce pro načítání souboru "load_from_json" pomocí for cyklu projde data a dojde zde k nastavení souřadnic (určení zeměpisné délky a šířky), typu sídla a vyfiltrování znaků sídel v případě, že ho mají. 

Samotné filtrování krajů a okresů je založeno na ukládání vybraných položek do nového seznamu, který je poté zobrazen v grafickém rozhranní místo původního, který obsahuje všechny. Funkce "filtrovat" poté opět for cyklem iteruje data v návaznosti na uživatelem zvolené atributy. 

### QML 
Struktura qml souboru je uspořádána v "RowLayout", který je rozdělen na 3 sloupce. V prvním se nachází filtrovací parametry. Zde je možné zvolit typ sídla (město/obec), a to pomocí "CheckBox". V návaznosti na zvolený parametr jsou přes proměnnou "self.obce" či "self.mesta" vyselektována příslušná data, která jsou poté uložena do nového seznamu. 

Dalším volitelným parametrem je počet obyvatel, který lze nastavit buď jako "TextInput" nebo pomocí "RangeSlider". Návaznost těchto dvou možností je zajištěna díky proměnným "min_po" a "max_po". Na stejném principu lze zvolit i rozlohu daného sídla. V tomto případě provázanost určují "min_area" a "max_area". K následnému filtrování dat dojde stejně jako v předchozím případě, tedy uložením na základě podmínky do nového seznamu. 

Sídla je v neposlední řadě možné selektovat na základě příslušnosti k vyšším administrativním jednotkám a sice ke krajům a následně k okresům. Defaultně jsou nastaveny všechny kraje i okresy, ale je možné je v "ComboBox" nastavit na jeden libovolný kraj či okres. V případě změny dojde k nastavení nové hodnoty pro proměnné "self.kraj_filtr" a "self.okres_filtr". Na základě této hodnoty jsou pak opět ve for cyklu z dat vyfiltrovány jen konkrétní kraje či okresy a uloženy do nového seznamu. 
Pro aktivování filtru je nutné stishnout tlačítko "Filtrovat".

Druhý sloupec tvoří mapové pole, uspořádané v "Rectangle". Pomocí pluginu je zobrazena mapa z OpenStreetMaps a defaultně je nastavena, aby zobraovala střed Česka. Při kliknutí na filtrovaví tlačítko, dojde k přiblížení na aktuálně zvolé sídlo, kraj či okres. 

Poslední sloupec tvoří "ListView", kde jsou zobrazeny informace o jednotlivých sídlech včetně znaku dané obce v případě, že ho má. 