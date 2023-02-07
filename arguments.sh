#!/bin/bash
# For loop with individual numbers
for i in 2 5 10 15 20
do
   python TextAnalyzer.py DCF  /work/courses/EECE5645/HW1/Data/Books/MobyDick.txt --N=$i >>output.log_"$i"
done
