![](images/header.png)

<div align = center>
<strong>
<hr>
BRKDWN
<br>
<hr>
<br>
Tartu Ülikooli LTAT.03.001 põhine projekt.
</strong>
</div>

### PAIGALDAMINE JA KÄIVITAMINE:

#### kloneerimine:
```bash
git clone https://github.com/DYESAWW/BRKDWN
cd BRKDWN
```
#### Sõltuvuste paigaldamine venvis ja põhiprogrammi käivitamine
```bash
python3 -m venv .venv
source .venv/bin/activate # Winowsil: ./.venv/Scripts/Activate.ps1
pip install -e ".[dev]"
./.venv/bin/BRKDWN  
```

### ARENDUSKESKKOND:
Projekt on peaaegu 100% kirjutatud Python programmerimiskeeles. Kasutajaliideseks on `textual` raamistik. Ning `textual` põhist kasutaja liidese välimust kirjeldatakse `.tcss` formaadis. Testid rakendame `pytest` tööriistaga. Andmebaasi jaoks on olemas `sqlite3`.
 
### FEATURES:
- Importeeri oma väljavõtted csv formaadis erinevatest pankadest.
- Pane neid kokku
- Vaata oma üldist sissetulukute ja kulude jaotust.
- Ekspordi kokkuväljavõtet edasiseks haldamiseks csv failina.

### TOETATAVAD PANGAD:
- Swedbank
- LHV
- Revolut

#### ARENDAJAD:
- Konstantin Razdolski 🪤🍻
- Ain August Talts 😔