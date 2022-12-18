#!/bin/bash

screens=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

if [ "$screens" = "HDMI1" ]; 
then
   xrandr --output VGA1 --mode 1366x768 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off
fi

setxkbmap us -variant intl

# volumeicon &

# cbatticon &

picom &

nm-tray &

nitrogen --restore