#!/bin/bash
set -eu

for i in queries;
do python3 overpass.py $i;
   osmtogeojson 
   
   
