### Importerar inställningar från config
from config.settings import MIN_LENGTH, MAX_LENGTH

def get_password_length() -> int:
    ### Loop tills användaren anger giltig input
    while True:
        ### Visar tillåtna gränser från config
        user_input = input(
            f"Ange lösenordets längd ({MIN_LENGTH}–{MAX_LENGTH}): "
        ).strip()

        ### Kontrollerar att input är siffror
        if user_input.isdigit():
            length = int(user_input)

            ### Kontrollerar att längden är inom gränserna
            if MIN_LENGTH <= length <= MAX_LENGTH:
                return length

        ### Om något är fel
        print("Ogiltig längd. Försök igen.")