#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins


YEAR=$11857
cat data/txt/*_${YEAR}_*.txt > module3/${YEAR}.txt
python module3/filtering.py 'data' $YEAR
wordcloud_cli --text module3/${YEAR}_keywords.txt --imagefile module3/${YEAR}.png --width 2000 --height 1000
display module3/${YEAR}.png

