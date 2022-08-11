from random import choice

from tobrot import BOT_THEME, USER_THEMES, LOGGER
from tobrot.bot_theme.themes import fx_optimised, fx_minimal

AVAILABLE_THEMES = {'fx-optimised-theme': fx_optimised, 'fx-minimal-theme': fx_minimal.__name__}

def BotTheme(user_id_):

    theme_ = USER_THEMES.get(str(user_id_), BOT_THEME)
    LOGGER.info(theme_)
    LOGGER.info(user_id_)
    if theme_ == "fx-optimised-theme":
        return fx_optimised.TXStyle()
    elif theme_ == "fx-minimal-theme":
        return fx_minimal.TXStyle()
    elif theme_ == "fx-random-theme":
        rantheme = choice(list(AVAILABLE_THEMES.values()))
        LOGGER.info(f"Random Theme Choosen : {rantheme}")
        return rantheme.TXStyle()
    else:
        return fx_optimised.TXStyle()

