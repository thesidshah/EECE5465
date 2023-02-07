#!/bin/bash
# For loop with individual numbers
mkdir Movies
for i in PiratesOfTheCaribbean.txt
do
   python TextAnalyzer.py DCF  /work/courses/EECE5645/HW1/Data/Movies/$i >>output.log_"$i"
done
