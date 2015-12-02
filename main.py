#! /usr/bin/env python3

import locale
from os.path import expanduser

from dialog import Dialog

from libqtile import confreader
# from libqtile import widget
# from libqtile import layout

locale.setlocale(locale.LC_ALL, '')

d = Dialog(autowidgetsize=True)

# should we start from empty or load some config
default_config = d.yesno("""This is Qtile setup program to prepair config to use Qtile.

Would you like to start from default config or load earlier config?""",
        yes_label='Default',
        no_label='Load file'
        )

if default_config == 'ok':
    d.infobox('Config is loading...')
    config = confreader.File()
else:
    home = expanduser("~")
    code, config_file = d.fselect(home)
    if code == 'ok':
        config = confreader.File(config_file)
        d.infobox('Config is loading...')
    else:
        d.infobox('File has not been loaded. Start gain :)')


print(config.__dict__)



