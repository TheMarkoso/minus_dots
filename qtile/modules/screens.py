import os
from libqtile.config import Screen, Group, DropDown
from libqtile import bar, qtile, widget, layout, extension
from libqtile.lazy import lazy
from modules.colors import colors as cl
from typing import List
from libqtile.widget import spacer


layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": cl[14],
                "border_normal": cl[2]
                }

floating_layout = layout.Floating(
        border_with = 2,
        margin = 6,
        border_focus = cl[14],
        border_normal = cl[2],
        )

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
]

widget_defaults = dict(
    font = 'HackNerdFont',
    fontsize = 15,
    padding = 3,
    foreground = cl[15],
    background = cl[0]
)


screens = [
    Screen(
        top=bar.Bar(
        [
            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.TextBox(
                text = '󰟪',
                padding = 3,
                mouse_callbacks={"Button1": lazy.spawn('rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu')},
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),

            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.GroupBox(
                font = 'HackNerdFont',
                disable_drag = True,
                center_aligned = True,
                fontsize = 12,
                margin_y = 3,
                margin_x = 0,
                padding_y = 5,
                padding_x = 3,
                borderwidth = 3,
                highlight_method = "line",
                rounded = True,
                inactive = cl[2],
                active = cl[15],
                highlight_color = cl[9],
                this_current_screen_border = cl[15],
                this_screen_border = cl[15],
                other_current_screen_border = cl[7],
                other_screen_border = cl[7],
                foreground = cl[15],
                background = cl[0]
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            
            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=cl[5],
                scale=0.7,
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),

            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.Clock(
                format=" %a, %b %d",
                font = 'HackNerdFont',
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),

            widget.Spacer(),

            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.TextBox(
                text = ' ',
                ),
            widget.PulseVolume(
                limit_max_volume = "True",
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            
            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.Net(
                format="󰈀 {down} ↓↑ {up}",
                perfix = "k",
                padding = 5,
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            
            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.Memory(
                format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                padding=5
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),

            widget.TextBox(
                text = '[',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),
            widget.TextBox(
                text = " ",
                ), 
            widget.Clock(
                    format="%I:%M %p",
                ),
            widget.TextBox(
                text = ']',
                fontsize = 15,
                font = 'HackNerdFont',
                foreground = cl[10],
                ),

        ],
        25,
        margin = [5, 6, 0, 6]
    ),),
]
