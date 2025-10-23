import re
import csv
import requests
def bajksi_podatki(kategorija,stran):
    if stran == 1:
        link = f"https://bajk.si/{kategorija}"
    else:
        link = f"https://bajk.si/{kategorija}/{stran}"
    r = requests.get(link)
    podatki = r.text
   # with open(f"tabele/{kategorija}/{stran}.html", "w", encoding="utf-8") as f:
    #    f.write(podatki)
   
    vzorec = r'href="(https://bajk\.si/kolesa/gorska-kolesa/[^"]+_i\d+)"'

    povezave = re.findall(vzorec, podatki)
    povezave = set(povezave)
    return povezave



strani_po_kategorijah = {
    "gorska-kolesa" : 74,
    "cestna-kolesa" : 19,
    "gravel-in-ciklokros-kolesa" : 5,
    "treking-kolesa" : 3,
    "bmx-dirt-kolesa" : 6,
    "mestna-kolesa" : 3,
    "otroska-kolesa" : 8

}
def posamezna_stran(link):
    r = requests.get(link)
    podatki = r.text
    id = link.split("/")[-1]
    with open(f"podatki/posamezni/{id}.html", "w", encoding="utf-8") as f:
        f.write(podatki)
    return id
    

def pridobi_podatke():
    vse_povezave = set()
    for kategorija in strani_po_kategorijah:
        strani = strani_po_kategorijah[kategorija]
        for stran in range(1,strani+1):
            povezave =bajksi_podatki(kategorija,stran)
            for i in povezave:
                vse_povezave.add(i)

    id_list = []
    for i in vse_povezave:
        id_list.append(posamezna_stran(i))
    return id_list
def podatki_v_csv(ids):
    kategorije = []
    for id in ids:
        with open(f"podatki/posamezni/{id}.html", "r", encoding="utf-8") as f:
            podatki = f.read()

        naslov = re.search(r'<h1>(.*?)</h1>', podatki).group(1).strip()
        cena = re.search(r'<div class="item-price">(.*?)</div>', podatki).group(1).strip()

        starost = re.search(r'Starost izdelka:.*?<strong>(.*?)</strong>', podatki, re.DOTALL).group(1).strip()
        proizvajalec = re.search(r'Proizvajalec kolesa:.*?<strong>(.*?)</strong>', podatki, re.DOTALL).group(1).strip()
        letnik = re.search(r'Letnik izdelave:.*?<strong>(.*?)</strong>', podatki, re.DOTALL).group(1).strip()
        velikost_okvirja = re.search(r'Velikost okvirja:.*?<strong>(.*?)</strong>', podatki, re.DOTALL).group(1).strip()
        material = re.search(r'Material okvirja:.*?<strong>(.*?)</strong>', podatki, re.DOTALL).group(1).strip()
        velikost_obrocev = re.search(r'Velikost obročev:.*?<strong>(.*?)</strong>', podatki, re.DOTALL).group(1).strip()

        opis_match = re.search(r'<div class="desc">(.*?)</div>', podatki, re.DOTALL)
        opis = re.sub(r'<br\s*/?>', '\n', opis_match.group(1)).strip() if opis_match else None
        opis = len(re.sub(r'<.*?>', '', opis)) if opis else None

    
        kategorija = re.search(r'<div class="row details">.*?<span>(.*?)\|', podatki, re.DOTALL).group(1).strip()
        posodobljeno = re.search(r'Posodobljeno (\d{2}\.\d{2}\.\d{4})', podatki).group(1)
        ogledi = re.search(r'(\d+) ogledov', podatki).group(1)

        kategorije.append((naslov,cena,starost,proizvajalec, letnik, velikost_okvirja, material, velikost_obrocev, opis, kategorija, posodobljeno, ogledi))

    with open("tabele/bike_podatki.csv", "w", newline='', encoding="utf-8") as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(["naslov", "cena", "starost", "proizvajalec", "letnik","velikost okvirja", "material", "velikost obročev", "dolžina opisa",
                           "kategorija", "posodobljeno", "ogledi"])
        
        for vrsta in kategorije:
            pisatelj.writerow(vrsta)

ids = pridobi_podatke()
podatki_v_csv(ids)