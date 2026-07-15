import bootstrap
bootstrap.load_secrets()

from ui.theme import configure_page, load_theme
from ui.logo import render_logo
from ui.hero import render_hero
from ui.composer import render_composer

configure_page()
load_theme()

render_logo()
render_hero()
render_composer()