# Analiza podatkov o gorskih kolesih

Ta projekt izvaja zajem in obdelavo podatkov o gorskih kolesih s spletne strani Bajk.si.
Cilj je analizirati kolesa po kategorijah, proizvajalcih, letnikih, materialih, cenah in drugih parametrih.


## Zajem podatkov

Projekt uporablja podatke iz spletne strani https://bajk.si, ki je ena vodilnih slovenskih spletnih strani za prodajo rabljenih koles.

## Struktura projekta
 
V glavni mapi sta mapi, `podatki` in `tabele`.
V mapi `podatki` so shranjeni surovi HTML podatki po mapah.
V mapi `tabele` je CSV datoteka.
V glavni mapi je tudi `analiza.ipynb`, kjer poteka analiza podatkov z uporabo Jupyter Notebooka.



## Zajeti podatki

Za vsako kolo so zajeti naslednji podatki:
- `naslov`: Naslov oglasa
- `cena`: Cena kolesa
- `starost`: Starost izdelka
- `proizvajalec`: Proizvajalec kolesa
- `letnik`: Letnik izdelave
- `velikost okvirja`: Velikost okvirja
- `material`: Material okvirja
- `velikost obročev`: Velikost obročev
- `dolžina opisa`: Dolžina opisa v znakih
- `kategorija`: Kategorija kolesa
- `posodobljeno`: Datum posodobitve oglasa
- `ogledi`: Število ogledov oglasa

## Uporabljene knjižnice

Za zagon programa je potrebno namestiti naslednje knjižnice:

- `requests` (za zajem podatkov s spleta)
- `re` (za delo z regularnimi izrazi)
- `csv` (za delo s CSV datotekami)
- `pandas` (za analizo podatkov v Jupyter Notebooku)

## Zagon projekta

Zaženite main.py nato odprite analiza.ipynb in ustvarite analizo.