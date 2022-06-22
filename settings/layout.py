# Carlos Pineda

from libqtile import layout
from .colors import colors

layout_theme = {
    'margin': 6,
    'border_width': 1,
    'border_focus': colors[10],
    'border_normal': colors[9],
}

layouts = [
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]
