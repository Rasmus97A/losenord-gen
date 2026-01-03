import sys
from pathlib import Path

### Hitta projektets rotmapp (där run.py ligger)
ROOT_DIR = Path(__file__).resolve().parent

### Lägg till rotmappen i Python's sökväg så att imports funkar
sys.path.insert(0, str(ROOT_DIR))

### Importera main-funktionen från app-paketet
from app.main import main

### Kör programmet
if __name__ == "__main__":
    main()