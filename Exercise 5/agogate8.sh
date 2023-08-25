#!/bin/bash
while getopts "n:m:v" option
	do 
	case $option in
	n)nfile=$OPTARG ;;
	m)nseq=$OPTARG ;;
	v)echo "YOU HAVE SELECTED VERBOSE MODE"
	esac
done

for ((i=1;i<=nfile;i++));
	do
	if [[ $* == *-v* ]]; then
		echo "THE SCRIPT IS CURRENTLY WORKING ON FILE $i"
	fi
	touch seq$i.fasta
	if [ $i  -le '10' ]; then
	rm -r seq$i.fasta
	fi

	for ((j=1;j<=nseq;j++));
		do
		if [[ $* == *-v* ]]; then
			echo "THE SCRIPT IS CURRENTLY WORKING ON FILE $i SEQUENCE $j"
		fi
		echo ">seq${i}_${j}" >> seq$i.fasta
		cat /dev/urandom | tr -dc 'ACGT' | fold -w 50 | head >> seq$i.fasta
	done
done
