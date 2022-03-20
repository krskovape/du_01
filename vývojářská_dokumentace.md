# Prohlížeč obcí a měst

Zde je popsáno, jak program "Prohlížeč obcí a měst" funguje a jak je strukturován. 

### Sturktura
V souboru "ultrafiltr.py" jsou definovány potřebné třídy a funkce, které jsou následně použity v grafickém rozhraní "superview.qml". 

K jednotlivým vlastnostem prvku v seznamu přistupujeme pomocí rolí. Ty dědí od třídy "enum" a pracuje s nimi funkce "data" a "roleNames". 

Následně jsou definovány proměnné používané v programu. Funkce get_min/max_po a set_min/max_po nastavují hodnotu počtu obyvatel, která je uživatelem upravována buď pomocí posuvníku, tak pomocí textových polí. V případě změny jednoho, dojde k autualizování dané hodnoty u druhého ukazatele. Totéž platí pro filtrování sídel na základě rozlohy a toho, zda se jedná o obec či město. 

Funkce pro načítání souboru "load_from_json" pomocí for cyklu projde data a dojde zde k nastavení souřadnic (určení zeměpisné délky a šířky), typu sídla a vyfiltrování znaků sídel v případě, že ho mají. 

Samotné filtrování krajů a okresů je založeno na ukládání vybraných položek do nového seznamu, který je poté zobrazen v grafickém rozhranní místo původního, který obsahuje všechny. Funkce "filtrovat" poté opět for cyklem iteruje data v návaznosti na uživatelem zvolené atributy. 

