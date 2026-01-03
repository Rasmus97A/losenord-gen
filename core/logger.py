import logging

def get_logger():
    ### Skapar en logger med namn
    logger = logging.getLogger("password_generator")

    ### Sätter loggnivå
    logger.setLevel(logging.INFO)

    ### Undviker att lägga till flera handlers
    if not logger.handlers:
        handler = logging.StreamHandler()

        ### Bestämmer hur loggarna ska se ut
        formatter = logging.Formatter(
            "%(levelname)s: %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger