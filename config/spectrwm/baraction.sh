#!/bin/bash

## RAM
mem() {
  mem=`free | awk '/Mem/ {printf "%dM/%dM\n", $3 / 1024.0, $2 / 1024.0 }'`
  echo -e "$mem"
}

## CPU
cpu() {
  read cpu a b c previdle rest < /proc/stat
  prevtotal=$((a+b+c+previdle))
  sleep 0.5
  read cpu a b c idle rest < /proc/stat
  total=$((a+b+c+idle))
  cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
  echo -e "CPU: $cpu%"
}

## VOLUME
vol() {
   vol=`pamixer --get-volume`
   echo -e "VOL: $vol"
}

SLEEP_SEC=3
while :; do
   # echo "+@fg=0; +@fn=1;💻+@fn=0; $(cpu) +@fg=0; | +@fg=0; +@fn=1;💾+@fn=0; $(mem) +@fg=0; | +@fg=0; +@fn=1;🔈+@fn=0; $(vol) +@fg=0; |"
   echo "$(cpu) | $(mem) | $(vol) |"
	sleep $SLEEP_SEC
done
