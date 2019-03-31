#!/bin/bash

if [ ! -f output.txt ]; then
    touch output.txt
fi

if [ ! -f format.txt ]; then
    touch format.txt
	echo "%{time_total}" >> format.txt
	printf "\n" >> format.txt
fi

time=0

while [  $time -lt 10 ]; do
	curl -w "@format.txt" -o /dev/null -s "http://localhost:8000/v0/reports/" >> output.txt
	printf "\n" >> output.txt
	let time=time+1 
done

total="0"
file="output.txt"
while IFS= read line
do
	total=$(echo "scale=3; $total + $line" | bc)
done <"$file"

times="10"
ave=$(echo "$total / $times" | bc)
printf 'average time for requested 10 times from reports endpoint %.3f s\n' "$(echo "scale=8;$total/10" | bc)"

rm output.txt