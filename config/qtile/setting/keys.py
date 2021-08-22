import datetime

from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
date = datetime.datetime.now();

keys_main = [
   # Switch between windows in current stack pane
   Key([mod], "k", lazy.layout.down()),
   Key([mod], "j", lazy.layout.up()),

   # Move windows up or down in current stack
   Key([mod, "control"], "k", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
   Key([mod, "control"], "j", lazy.layout.shuffle_up(), desc="Move window up in current stack "),
   
   # Toggle between split and unsplit sides of stack.
   # Split = all windows displayed
   # Unsplit = 1 window displayed, like Max layout, but still with
   Key([mod, "shift"], "Return", lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
   
   # Launch terminal
   Key([mod], "Return", lazy.spawn('alacritty')),
   
   # Toggle between different layouts as defined below
   Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
   
   # Close windows
   Key([mod, "shift"], "w", lazy.window.kill()),
   
   #Focus of monitors
   Key([mod], "comma", lazy.prev_screen()),
   
   # Window size
   Key([mod, "shift"], "k", lazy.layout.grow()),
   Key([mod, "shift"], "j", lazy.layout.shrink()),
   
   #Apps
   Key([mod, "shift"], "m", lazy.spawn('rofi -modi drun,run -show drun -show-icons')),
   #Browser
   Key([mod, "shift"], "f", lazy.spawn("firefox-developer-edition")),
   #Files
   Key([mod, "shift"], "e", lazy.spawn("thunar")),
   #screenshot
   Key([mod, "shift"], "p", lazy.spawn("imlib2_grab screenshot.png")),
   
   # Sound
   Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
   Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
   Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),
   # Brillo
   Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
   Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

   # Restart qtile
   Key([mod, "control"], "r", lazy.restart()),
   # Shutdown qtile 
   Key([mod, "control"], "q", lazy.shutdown()),
]