#!/bin/zsh

echo "Number of other players: "
read NUM_OTHER_PLAYERS
echo "Result filename: "
read RES_FILENAME

echo > ./stats/temp
echo '0' >> ./stats/temp
echo "$NUM_OTHER_PLAYERS" >> ./stats/temp
echo 'q' >> ./stats/temp
	
#prints the cards and the percentage in the out file.
python3 another_sim.py < ./stats/temp | head -n 100003       \
	| tail -n 100000 >> "./stats/${RES_FILENAME}";

num_res=$(cat "./stats/${RES_FILENAME}" | wc -l)


num_high=$(grep '^high card$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "high cards," > ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_high / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_pairs=$(grep '^pair$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "pairs, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_pairs / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_2_pairs=$(grep '^two pair$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "two pairs, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_2_pairs / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_tofk=$(grep '^three of a kind$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "three of a kinds, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_tofk / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_straights=$(grep '^straight$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "straights, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_straights / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_flush=$(grep '^flush$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "flushes, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_flush / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_full_house=$(grep '^full house$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "full houses, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_full_house / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_foak=$(grep '^four of a kind$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "four of a kinds, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_foak / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_straight_flush=$(grep '^straight flush$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "straight flushes, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_straight_flush / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 

num_royal_flush=$(grep '^royal flush$' "./stats/${RES_FILENAME}" | wc -l)
echo -n "royal flushes, " >> ./stats/${RES_FILENAME}.csv 
echo "scale=7;( $num_royal_flush / $num_res ) * 100" | bc >> ./stats/${RES_FILENAME}.csv 
