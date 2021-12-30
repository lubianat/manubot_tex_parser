#!/bin/sh

cd images &&
for f in *?raw=true; do 
    mv -- "$f" "${f%.*?raw=true}.png"
done

for file in *.svg; do
     /usr/bin/inkscape -z -f "${file}" -w 1280 -e "${file}.png"
done