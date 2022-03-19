# Prohlížeč obcí a měst

Program `Prohlížeč obcí a měst` umožňuje filtrovat sídla v Česku podle několika parametrů a výsledek zobrazit v mapě a seznamu.

### Filtrovací kategorie
* **Města a obce**
  * Při zakliknutí políčka dojde k filitrování příslušného typu sídla. Vždy musí být vybrán alespoň jeden z nich, případně oba najednou.
* **Počet obyvatel**
  * Pomocí posuvníku nebo zápisu do textových polí lze nastavit minimální a maximální požadovaný počet obyvatel a program filitruje sídla ve zvoleném rozmezí.
    Minimum je defaultně nastaveno na 0 a maximum na 1,5 milionu obyvatel. 
* **Rozloha**
  * Obdobně jako u rozlohy lze pomocí posuvníku nebo textových polí nastavit požadované rozmezí pro rozlohu sídla v km<sup>2</sup>.
    Minumum je defaultně nastaveno na 0 km<sup>2</sup> a maximum na 500 km<sup>2</sup>.
* **Kraj**
  * Výběrem z rolovacího menu mohou být vybrány všechny kraje nebo jeden konkrétní. V základu je zvolena možnost všech krajů.
* **Okres**
  * Výběrem konkrétního kraje se položky v rolovacím menu upraví tak, aby okresy v nabídce odpovídaly zvolenému okresu. Opět lze vybrat
    všechny okresy v kraji nebo jeden konkrétní. Při výběru všech krajů se automaticky vyberou i všechny okresy.

### Výsledek filtrování
Po nastavení požadovaných filtrovacích parametrů a kliknutí na tlačítko `Filtrovat` se vybraná sídla zobrazí v seznamu v pravé části a zároveň v mapě.
Pro přiblížení mapy a detailnější zobrazení vyfiltrovaných měst je potřeba zmáčknout `Filtrovat` dvakrát nebo třikrát. V seznamu je zobrazen název sídla
a pod ním jeho rozhloha, počet obyvatel a okres, do kterého spadá. Názvy sídel, které jsou města, jsou v seznamu i v mapě zobrazeny červeně. Při kliknutí
na konkrétní sídlo v seznamu dojde k jeho vybrání a mapa se na toto sídlo přiblíží a vycentruje.
