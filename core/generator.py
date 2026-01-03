import random
import string

class PasswordGenerator:
    ### Konstruktor: körs när objektet skapas
    def __init__(self, length: int):
        self.length = length

        ### Tillåtna tecken: bokstäver + siffror
        self.characters = string.ascii_letters + string.digits

    ### Metod som skapar lösenordet
    def generate(self) -> str:
        ### Väljer slumpmässiga tecken och sätter ihop till sträng
        return "".join(
            random.choice(self.characters)
            for _ in range(self.length)
        )