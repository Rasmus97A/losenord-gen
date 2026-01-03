# Pythonprojekt
Pythonprojekt för inlämning i kursen Python Fortsättning

# Lösenordsgenerator

Ett enkelt Pythonprogram som genererar slumpmässiga lösenord baserat på användarens valda längd.

### Installation

Skapa virtuell miljö:

python -m venv venv  
source venv/bin/activate  
venv\Scripts\activate  

Installera beroenden: (behövs ej några i detta projekt, står även i requirements.txt)

pip install -r requirements.txt
(inga beroenden behövs)

### Kör programmet ###

py run.py
python run.py
python3 run.py

# Python version

python --version

koden skriven med Python version 3.13.7

### MAPPTRÄD över hur mappar och filer ligger i projektet.
```
📦 pyproj
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-313.pyc
│  │  └─ main.cpython-313.pyc
│  └─ main.py
├─ config
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-313.pyc
│  │  └─ settings.cpython-313.pyc
│  └─ settings.py
├─ core
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-313.pyc
│  │  ├─ generator.cpython-313.pyc
│  │  ├─ logger.cpython-313.pyc
│  │  └─ validator.cpython-313.pyc
│  ├─ generator.py
│  ├─ logger.py
│  └─ validator.py
├─ requirements.txt
└─ run.py
```
