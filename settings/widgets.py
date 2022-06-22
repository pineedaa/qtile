# Carlos Pineda

import numpy
import os
import random
import psutil
from libqtile import widget, qtile, lazy

from .colors import colors

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=18,
    padding=0,
    background='#282a36'
)
extension_defaults = widget_defaults.copy()


def battery_level_hearts():
    heart = ' '
    half_heart = 'ﯜ '
    empty_heart = ' '
    indicator = ''

    battery = psutil.sensors_battery()
    hearts = int(20 / (100 / battery.percent))

    for _ in range(1, hearts, 2):
        indicator = indicator + heart

    if hearts % 2 != 0:
        indicator = indicator + half_heart

    for _ in range(1, 20 - hearts, 2):
        indicator = indicator + empty_heart

    return indicator


def transparency(color='#000000', opacity=0):
    return color + '.' + str(opacity)


def chname(text):
    for string in ['Firefox', 'Alacritty', 'Speek', 'Thunar', 'Spotify', 'VSCodium', 'MARS', 'DrRacket', 'carlos@', 'NVIM']:
        if string in text:
            text = string
            if text == 'carlos@':
                text = 'Alacritty'
            if text == 'NVIM':
                text = 'Neovim'
        else:
            text = text
    return text


def openCalendar():
    state = os.system('eww windows | grep "*clock"')
    if state == 0:
        os.system('eww close clock')
    else:
        os.system('eww open clock')


widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=18,
    padding=0,
    background=colors[1]
)


left = ''
right = ' '

widget_list = [
    widget.Spacer(
        length=12,
        background=transparency()
    ),
    widget.TextBox(
        text='  ',
        background=transparency(),
        foreground=colors[4]
    ),
    widget.Clock(
        format='%A, %d de %B  %H:%M',
        background=transparency(),
        foreground=colors[10],
        mouse_callbacks={'Button1': openCalendar}
    ),
    widget.Spacer(
        background=transparency()
    ),
    widget.GroupBox(
        margin_x=8,
        margin_y=4,
        highlight_method='text',
        background=transparency(),
        active=colors[3],
        inactive=transparency(colors[9], 2),
        this_current_screen_border=colors[10],
    ),
    widget.Spacer(
        background=transparency()
    ),
    widget.GenPollText(
        func=battery_level_hearts,
        background=transparency(),
        foreground='#ff5555',
        update_interval=60
    ),
    widget.Spacer(
        background=transparency(),
        length=20
    ),
    widget.Wlan(
        foreground=colors[1],
        background=transparency(),
        format='  ',
        disconnected_message='睊 ',
    ),
    widget.Wlan(
        foreground=colors[10],
        background=transparency(),
        format='{essid}',
        disconnected_message='',
    ),
    widget.Spacer(
        length=20,
        background=transparency()
    ),
    widget.Battery(
        format='{char} ',
        charge_char='',
        discharge_char='',
        empty_char='',
        unknown_char='',
        foreground=colors[2],
        background=transparency(),
        low_foreground='#FF0000',
        low_percentage=0.2
    ),
    widget.Battery(
        format='{percent:2.0%}',
        charge_char='',
        discharge_char='',
        empty_char='',
        unknown_char='',
        foreground=colors[10],
        background=transparency(),
        low_foreground='#FF0000',
        low_percentage=0.2
    ),
    widget.Spacer(
        length=20,
        background=transparency()
    ),
    widget.TextBox(
        text='墳 ',
        foreground=colors[6],
        background=transparency(),
    ),
    widget.PulseVolume(
        foreground=colors[10],
        background=transparency(),
        limit_max_volume=True
    ),
    widget.Spacer(
        length=12,
        background=transparency()
    )
]

taskbar = [
    widget.Spacer(
        background=transparency()
    ),
    widget.TextBox(
        font='MesloLGS NF',
        fontsize=26,
        text=left,
        foreground=transparency(colors[9], 4),
        background=transparency()
    ),
    widget.TaskList(
        background=transparency(colors[9], 4),
        unfocused_border=transparency(colors[9], 2),
        border=transparency(colors[3], 5),
        parse_text=chname,
        highlight_method='block',
        txt_floating='  ',
        txt_maximized='  ',
        txt_minimized='  ',
        title_width_method='uniform',
        icon_size=0,
        mouse_callbacks={'Button2': lambda: qtile.current_window.kill()}
    ),
    widget.TextBox(
        font='MesloLGS NF',
        fontsize=26,
        text=right,
        foreground=transparency(colors[9], 4),
        background=transparency()
    ),
    widget.Spacer(
        background=transparency()
    ),
    widget.Systray(
        background=transparency()
    ),
    widget.Spacer(
        length=12,
        background=transparency()
    )
]
