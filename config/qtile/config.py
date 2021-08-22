# Configuration for Qtile
# samueldlh

from typing import List

import os
import subprocess
import socket

from setting.theme import colors
from setting.keys import keys_main

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

def base(fg, bg): 
    return {
        'foreground': colors[fg],
        'background': colors[bg],
    }

def icon(fg, bg, fz, txt): 
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        'fontsize': fz,
        'text': txt,
    }

def powerline(fg, bg):
     return {
        'foreground': colors[fg],
        'background': colors[bg],
        'fontsize': 39,
        'text': '',
        'padding': -7
    }

mod = "mod4"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

keys = keys_main

groups = [Group(i) for i in ["DEV", "WWW","TERM", "MIXED"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    layout.MonadTall(border_focus=colors['c5'], border_width=1, margin=3),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono NF", 
    fontsize=11,
    padding=5,
    background="#000000",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground='#000000',
                    active='#ffffff',
                    fontsize=11,
                    borderwidth=1,
                    highlight_method='block',
                    this_current_screen_border=[colors['c4'], colors['c4']],
                ),
                widget.WindowName(fontsize=11),
                widget.Chord(
                    chords_colors={'launch': ("#ff0000", "#ffffff"),},
                    name_transform=lambda name: name.upper(),
                ),

                widget.TextBox(**powerline( fg='c1', bg='c0' )),
                widget.TextBox(**icon( fg='c0', bg='c1', fz=19, txt='' )),
                widget.TextBox(
                    text=socket.gethostname(),
                    foreground='#000000',
                    background=colors['c1']
                ),

                widget.TextBox(**powerline( fg='c4', bg='c2' )),
                widget.TextBox(**icon( fg='c0', bg='c4', fz=19, txt='')),
                widget.Memory(**base(fg='c0', bg='c4')),

                widget.TextBox(**powerline( fg='c5', bg='c4' )),
                widget.TextBox(**icon( fg='c0', bg='c5', fz=19, txt='')),
                widget.Clock(
                    **base(fg='c0', bg='c5'),
                    format='%b %d [%I:%M %p]'
                ),

                widget.TextBox(**powerline( fg='c0', bg='c5' )),
                widget.Systray(),
            ],
            17,
            opacity=0.9
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
