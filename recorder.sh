#!/bin/zsh

echo "Number of other players: "
read NUM_OTHER_PLAYERS
echo "Result filename: "
read RES_FILENAME

#exit with crl-c
while [ 1 ]
do
	echo "Card 1:"
	read C1
	echo "Card 2:"
	read C2
	
	echo > ./stats/hands
	echo '1' >> ./stats/hands
	echo "$C1" >> ./stats/hands
	echo "$C2" >> ./stats/hands
	echo "$NUM_OTHER_PLAYERS" >> ./stats/hands
	echo 'q' >> ./stats/hands

	if [ "$C1" = "EOF" ]
	then 
		rm ./stats/hands
		exit
	fi
		
	#prints the cards, the percentage, and a newline in the out file.
	head -n 4 ./stats/hands | tail -n 2 >> "./stats/${RES_FILENAME}"; \
    python3 sim.py < ./stats/hands | grep -o '[0-9][0-9]*%'        \
	 >> "./stats/${RES_FILENAME}";                                 \
     echo >> ./stats/handres.txt
done
