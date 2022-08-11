from random import choice

from tobrot import BOT_THEME, USER_THEMES
from tobrot.bot_theme.themes import fx_optimised, fx_minimal 

AVAILABLE_THEMES = {'fx-optimised-theme': 'fx_optimised', 'fx-minimal-theme': 'fx_minimal'}

def BotTheme(user_id_):

    if (not BOT_THEME):
        BOT_THEME = USER_THEMES.get(user_id_)

    if BOT_THEME in AVAILABLE_THEMES.keys():
        return (AVAILABLE_THEMES.get(BOT_THEME)).TXStyle()
    elif BOT_THEME == "fx-random-theme":
        rantheme = choice(list(AVAILABLE_THEMES.values()))
        LOGGER.info(f"Random Theme Choosen : {rantheme}")
        return rantheme.TXStyle()
    else:
        return fx_optimised.TXStyle()

