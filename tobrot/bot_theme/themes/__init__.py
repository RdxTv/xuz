from random import choice

from tobrot import BOT_THEME
from tobrot.bot_theme.themes import fx_optimised, fx_minimal 

AVAILABLE_THEMES = ['fx_optimised', 'fx_minimal']

def BotTheme():
    if BOT_THEME == "fx-optimised-theme":
        return fx_optimised.TXStyle()
    elif BOT_THEME == "fx-minimal-theme":
        return fx_minimal.TXStyle()
    elif BOT_THEME == "fx-random-theme":
        rantheme = choice(AVAILABLE_THEMES)
        LOGGER.info(f"Random Theme Choosen : {rantheme}")
        return rantheme.TXStyle()

