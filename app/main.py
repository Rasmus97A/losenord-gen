### Importerar lösenordsgenerator-klassen
from core.generator import PasswordGenerator

### Importerar funktion för säker input
from core.validator import get_password_length

### Importerar logger
from core.logger import get_logger

### Skapar logger-instans
logger = get_logger()

def main():
    ### Loggar att programmet startar
    logger.info("Programmet startar")

    ### Frågar användaren om längd (valideras)
    length = get_password_length()

    ### Skapar ett generator-objekt med vald längd
    generator = PasswordGenerator(length)

    ### Genererar lösenordet
    password = generator.generate()

    ### Skriver ut lösenordet
    print(f"Ditt lösenord: {password}")

    ### Loggar att lösenord skapats
    logger.info("Lösenord genererat")

### Kör main-funktionen om filen körs direkt
if __name__ == "__main__":
    main()