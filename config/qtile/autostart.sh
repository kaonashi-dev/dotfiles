#!/bin/sh

screens=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

if [ "$screens" = "HDMI-1" ]; 
then
   xrandr --output VGA-1 --mode 1366x768 --pos 1920x0 --rotate normal --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off
fi

volumeicon &

picom &

nm-applet &

setxkbmap us -variant intl

nitrogen --restore