#!/bin/bash
>oldFiles.txt

files=$(grep " jane " ~/GoogleTraining/touchfile.txt | cut -d ' ' -f 3)
#files=$(echo "$files" | sed "s|^|~|")

#echo $files

for item in $files; do 
  if [ -f "$HOME$item" ]; then
    echo "$HOME$item" >> oldFiles.txt; 
  fi
done

