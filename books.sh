#!/bin/bash
# For loop with individual numbers
mkdir books
for i in "Frankenstein.txt"  "JaneEyre.txt"  "MobyDick.txt"  "PrideAndPrejudice.txt"  "TheOdyssey.txt"  "TheStoryOfTheStone.txt"  "WarAndPeace.txt"
do
   python TextAnalyzer.py DCF  /work/courses/EECE5645/HW1/Data/Books/$i >>"./books/output.log_$i"
done
