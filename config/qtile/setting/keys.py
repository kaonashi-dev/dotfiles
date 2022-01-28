import datetime

from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
terminal = 'alacritty'
date = datetime.datetime.now();

keys_main = [
   # Switch between windows
   Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
   Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
   Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
   Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
   Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

   # Move windows between left/right columns or move up/down in current stack.
   Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
   Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
   Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
   Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
   # Grow windows. If current window is on the edge of screen and direction
   Key([mod, "control"], "h", lazy.layout.shrink(), desc="Grow window to the left"),
   Key([mod, "control"], "l", lazy.layout.grow(), desc="Grow window to the right"),
   
   Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
   Key([mod], "comma", lazy.prev_screen(), desc="Focus of monitors"),

   # Toggle between split and unsplit sides of stack.
   # Split = all windows displayed
   # Unsplit = 1 window displayed, like Max layout, but still with
   # multiple stack panes
   Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
   Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

   # Toggle between different layouts as defined below
   Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
   Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),

   #Apps
   Key([mod, "shift"], "m", lazy.spawn('rofi -modi drun,run -show drun -show-icons')),
   #Firefox
   Key([mod, "shift"], "f", lazy.spawn("firefox-developer-edition")),
   #Visual studio code
   Key([mod, "shift"], "c", lazy.spawn("code")),
   #Brave
   Key([mod, "shift"], "b", lazy.spawn("brave")),
   #Files
   Key([mod, "shift"], "e", lazy.spawn("thunar")),
   #Slack
   Key([mod, "shift"], "k", lazy.spawn("slack")),
   #screenshot
   Key([mod, "shift"], "p", lazy.spawn("kazam -p")), # All screeen
   Key([mod, "control"], "p", lazy.spawn("kazam -p")), # crurent window
   
   # Sound
   Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
   Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
   Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

   # Brillo
   Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
   Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

   Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
   Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]