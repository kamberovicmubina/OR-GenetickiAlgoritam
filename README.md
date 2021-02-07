# OR-GenetickiAlgoritam

Implementiran je genetički algoritam sa binarnim kodiranjem i testiran je na problemu pronalaženja globalnog maksimuma Rastrigin funkcije. 

Jedinka (hromozom) je predstavljena klasom MojaIndividua izvedenom iz apstraktne klase ApstraktnaIndividua. Oblik hromozoma je sljedeći: <br/>
h: b<sub>d−1</sub>b<sub>d−2</sub>···b<sub>r</sub>b<sub>r−1</sub>b<sub>r−2</sub>···b<sub>0</sub>, <br/>
gdje je b<sub>i</sub>∈{0,1}, i∈{0,1,...,d−1}, pri čemu d predstavlja dužinu hromozoma koja treba biti oblika 2k+ 2, k∈N, a r=d/2. Bîti b<sub>r−1</sub>b<sub>r−2</sub>···b<sub>0</sub> određuju koordinatu x<sub>2</sub>, pri čemu najznačajniji bit b<sub>r−1</sub> određuje njen predznak (b<sub>r−1</sub>= 0 ako je x<sub>2</sub>≥0, a b<sub>r−1</sub>= 1 ako je x<sub>2</sub><0).  Bîti b<sub>r−2</sub>···b<sub>r−1−p</sub> određuju cijeli dio broja |x<sub>2</sub>|, a bîti b<sub>r−2−p</sub>···b<sub>0</sub> njegov decimalni dio, gdje p određuje broj bita cijelog dijela i ispunjava uslov 1≤p≤r−1. Ista logika važi i za bite b<sub>d−1</sub>b<sub>d−2</sub>···b<sub>r</sub>, koji određuju koordinatu x<sub>1</sub>. Vrijednost p u ovoj implementaciji je jednaka 2. <br/>

Implementirani su operator selekcije na bazi ruletskog točka, operator selekcije na bazi ranga, operatori ukrštanja u jednoj i u dvije tačke, te operator binarne mutacije. Atribut VelicinaElite definiše da li je prisutan elitizam i koliko najboljih jedinki se prenosi u sljedeću generaciju. 

Za rješavanje spomenutog problema je kreirana instanca klase Populacija koja sadrži 30 hromozoma, ima vjerovatnoću ukrštanja 0.99, vjerovatnoću mutacije 0.01. Maksimalan broj generacija algoritma je 50, a elitizam od jedne jedinke je prisutan. Dužina hromozoma je 16.
