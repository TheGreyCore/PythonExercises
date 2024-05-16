# 3. OOPi põhitõed vol 1

**NB: Sellest ülesandest muutub ka ülesannete kirjelduse formaat!**

Selles harjutuses pead looma lihtsama programmi "loomaaed". Selle ülesande lahendamiseks **pead** kasutama OOPi paradigmad ja looma erinevaid klasse.

OOPist saad lugeda juurde siit: https://www.geeksforgeeks.org/python-oops-concepts/

Esiteks loo baasklass `loom`,  mis kirjeldab loomi üleüldiselt. Klass peab sisaldama looma nime, nälga ja meetodeid `liigu`, `söö` ja `loomast`. Iga meetod peab
klassi muutujaid muutma (v.a meetod `loomast`). Näiteks meetod `liigu` suurendab nälga ja meetod `söö` suurendab omakorda nälga. Meetod `loomast` peab tagastama kirje mis sisaldab informatsiooni loomast formaadis: `Loom nimega *nimi* on *nälg*% näljane`. 

Järgmiseks loo klassid `ahv`, `elevant`, `kits`, mis kõik laiendavad klassi `loom`. Lisa igale alamkallasile sellele vastavale isendile omapärased tegevused ja kirjuta üle sellised baasklassi meetodid nägu `liigu` ja `söö`.

Viimaseks loo põhimeetod `loomaaed` mis võimaldab kasutajal loomaaias seikleda, vaadata loomi ja neid ka sööta.

Näide programmi tööst (Peale '#' olev tekst on kasutaja sisendi näide.):
```text
Tere tulemast loomaaeda "Väike park"!
Meil saad näha järgmisi loomi: ahv, elevant ja kits.
Kelle juurde tahad minna: #Ahv
Jõudsid ahvi juurde. Saad teha järgmisi asju (v)aadata, (s)ööta, (m)inna edasi:
#v
Loom nimega ahv on 50% näljane.
Saad teha järgmisi asju (v)aadata, (s)ööta, (m)inna edasi:
#m
Meil saad näha järgmisi loomi: ahv, elevant ja kits.
Kelle juurde tahad minna: ...
```

NB: Ülesane võib tunduda ebaloogiline, kuid see peabki nii olema! 

