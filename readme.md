# WOLServer

## Prerequisites

### Python Venv installieren
```bash
sudo apt install python3-venv
```

### Einen Ordner für die separierte Environment erstellen und hineinwechseln
```bash
mkdir wol
cd wol
```

### Python-Environment erstellen
```bash
python3 -m venv .
```

git clone http://192.168.160.39:3001/sem/wolServer.git

### In der Console auf die Python-Environment wechseln, damit nicht die Python-Instanz des Hosts verwendet wird
```bash
source bin/activate
```

### Alle Abhängigkeiten mit Hilfe der requirements.txt-Datei installieren.
```bash
pip install -r requirements.txt
```