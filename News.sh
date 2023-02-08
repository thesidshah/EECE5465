#!/bin/bash
# For loop with individual numbers
mkdir News
for i in "NYT1.txt"  "NYT2.txt"  "NYT3.txt"  "WSJ1.txt"  "WSJ2.txt"

do
   python TextAnalyzer.py DCF  /work/courses/EECE5645/HW1/Data/News/$i >>output.log_"$i"
done
