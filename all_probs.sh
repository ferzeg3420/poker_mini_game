#!/bin/bash

for name in "$@"
do
	echo "Processing $name"
	for ((i=2; i <= 9; i++))
	do
		rm ./stats/temp 2>/dev/null
		outfile_name="${name%.*}${i}"
		echo "$i" >> ./stats/temp
		echo "${outfile_name}" >> ./stats/temp
		cat ./stats/temp $name >> ./stats/temp1
		echo "EOF" >> ./stats/temp1
		mv ./stats/temp1 ./stats/temp
		./recorder.sh < ./stats/temp 1 >/dev/null
		echo "${name} ${i} players DONE."
	done
done
