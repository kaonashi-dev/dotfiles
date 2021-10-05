# Configuration for Qtile
# samueldlh

from typing import List

import os
import socket
import subprocess

from setting.theme import colors
from setting.keys import keys_main

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

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

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

keys = keys_main

groups = [Group(i) for i in ["DEV", "WWW","TERM", "MIXED"]]

for i, group in enumerate(groups):
    actual_key = str(i+ 1)
    keys.extend([

        # mod1 + letter of group = switch to group
        Key([mod], actual_key, lazy.group[group.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True)),
    ])

layouts = [
    layout.MonadTall(border_focus=[colors['color5'], colors['color5']], border_width=1, margin=3),
    layout.Max(),
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
                    this_current_screen_border=[colors['color4'], colors['color4']],
                ),
                widget.WindowName(fontsize=11),
                widget.Chord(
                    chords_colors={'launch': ("#ff0000", "#ffffff"),},
                    name_transform=lambda name: name.upper(),
                ),

                widget.TextBox(**powerline( fg='color3', bg='color1' )),
                widget.TextBox(**icon( fg='color1', bg='color3', fz=19, txt='' )),
                widget.TextBox(
                    text=socket.gethostname(),
                    foreground='#000000',
                    background=colors['color3']
                ),

                widget.TextBox(**powerline( fg='color4', bg='color3' )),
                widget.TextBox(**icon( fg='color1', bg='color4', fz=19, txt='')),
                widget.Memory(**base(fg='color1', bg='color4')),

                widget.TextBox(**powerline( fg='color5', bg='color4' )),
                widget.TextBox(**icon( fg='color1', bg='color5', fz=19, txt='')),
                widget.Clock(
                    **base(fg='color1', bg='color5'),
                    format='%b %d [%I:%M %p]'
                ),

                widget.TextBox(**powerline( fg='color1', bg='color5' )),
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
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus=[colors['color3'], colors['color5']],float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


auto_minimize = True

wmname = "LG3D"
