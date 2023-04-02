#!/bin/bash

screens=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

if [ "$screens" = "HDMI-1" ]; 
then
   xrandr --output eDP-1 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal
fi

setxkbmap us -variant intl

volumeicon &

cbatticon &

applet &

picom &

dunst &

nitrogen --restore