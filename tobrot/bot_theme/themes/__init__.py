from random import choice

from tobrot import BOT_THEME, USER_THEMES
from tobrot.bot_theme.themes import fx_optimised as fxoptimised, fx_minimal as fxminimal

AVAILABLE_THEMES = {'fx-optimised-theme': fxoptimised.__name__, 'fx-minimal-theme': fxminimal.__name__}

def BotTheme(user_id_):

    theme_ = USER_THEMES.get(user_id_, BOT_THEME)
    if theme_ in AVAILABLE_THEMES.keys():
        fx = AVAILABLE_THEMES.get(theme_)
        return fx.TXStyle()
    elif theme_ == "fx-random-theme":
        rantheme = choice(list(AVAILABLE_THEMES.values()))
        LOGGER.info(f"Random Theme Choosen : {rantheme}")
        return rantheme.TXStyle()
    else:
        return fxoptimised.TXStyle()

