#!/bin/bash
#This is a getopts block to define every flag that the user might input. 
while getopts "a:b:r:eo:f:zvih" option
	do 
	case $option in
	a)reads1=$OPTARG ;;
	b)reads2=$OPTARG ;;
	r)ref=$OPTARG ;;
	e)if [[ $* == *-e* ]]; then 
        realign=1 
        else
        realign=0
	fi ;; 
	o)output=$OPTARG ;;
	f)millsFile=$OPTARG ;;
	z)if [[ $* == *-z* ]]; then 
	gunzip=1
	else
	gunzip=0
	fi ;;
	v)echo "YOU HAVE SELECTED VERBOSE MODE"
	if [[ $* == *-v* ]]; then 
        v=1 
        else
        v=0
	fi ;;
	i)if [[ $* == *-i* ]]; then
        index=1
        else
        index=0
	fi ;;
	h)echo "The following flags can be used while running the script- 1. -a to inout the first read file in unzipped form, -b to input the second read file in unzipped form, -r to input the reference genome in unzipped form, -e to perform read re alignment, -o to set name for the output vcf file without extension, -f to specify the mills file location, -z to specify if the output vcf file has to be gunzipped, -v for verbose mode, -i to index output BAM file and -h to get help" ;;
	esac	
done

#file checking
if test -f "$reads1"; then
echo "Read 1 is input"
else
echo "Read 1 is not input"
exit
fi 

if test -f "$reads2"; then
echo "Read 2 is input"
else
echo "Read 2 is not input"
exit
fi 

if test -f "$ref"; then
echo "Reference genome is input"
else
echo "Reference genome is not input"
exit
fi 

FILENAME="$output.vcf.gz"
 
if [ -f "$FILENAME" ]
then
echo "$FILENAME exists. Do you want to replace it? Type yes if you want to, else type no"
read answer
if [ $answer == "no" ]
then
exit  
fi
fi

FILENAME1="$output.vcf"
 
if [ -f "$FILENAME1" ]
then
echo "$FILENAME1 exists. Do you want to replace it? Type yes if you want to, else type no"
read answer
if [ $answer == "no" ]
then
exit  
fi
fi


#ALignment step using BWA
if [[ $v == 1 ]]; then
echo "We are now at the aligning and mapping step"
fi 
bwa index $ref
bwa mem -R '@RG\tID:foo\tSM:bar\tLB:library1' $ref $reads1 $reads2 > lane.sam 
samtools sort -O bam lane.sam -o lane_sorted.bam 
samtools index lane_sorted.bam


#improvement step
if [[ $v == 1 ]]; then
echo "We are now at the optional re alignment step"
fi

if [[ $realign == 1 ]]; then
samtools faidx $ref
name="${ref%.*}" 
samtools dict $ref -o $name.dict
java -Xmx2g -jar GenomeAnalysisTK.jar -T RealignerTargetCreator -R $ref -I lane_sorted.bam -o lane.intervals --known $millsFile 2>GATKLog1.log
java -Xmx4g -jar GenomeAnalysisTK.jar -T IndelRealigner -R $ref -I lane_sorted.bam -targetIntervals lane.intervals -known $millsFile -o lane_realigned.bam 2>GATKLog2.log
if [[ $* == *-i* ]]; then
samtools index lane_realigned.bam
fi
fi

#variant calling step
if [[ $v == 1 ]]; then
echo "We are now at the variant calling step"
fi
 
if [[ $realign == 1 ]]; then
if [[ $gunzip == 1 ]]; then
bcftools mpileup -Ou -f $ref lane_realigned.bam | bcftools call -vmO z -o $output.vcf.gz
else
bcftools mpileup -Ou -f $ref lane_realigned.bam | bcftools call -vmO z -o $output.vcf
fi
fi

if [[ $realign == 0 ]]; then
if [[ $gunzip == 1 ]]; then
bcftools mpileup -Ou -f $ref lane_sorted.bam | bcftools call -vmO z -o $output.vcf.gz
else
bcftools mpileup -Ou -f $ref lane_sorted.bam | bcftools call -vmO z -o $output.vcf
fi
fi

#conversion of vcf files to bed file 
if [[ $v == 1 ]]; then
echo "We are now at the conversion step"
fi

if [[ $gunzip == 1 ]]; then
gzip -dk $output.vcf.gz
fi
sed '/^#/d' $output.vcf > study1.vcf
cut -f1,2,4,5 study1.vcf > int_file.txt
awk '{print length($4)-length($3)}' int_file.txt >int_file1.txt
paste int_file.txt int_file1.txt > int_file2.txt
awk '{print $2+$5}' int_file2.txt >int_file3.txt
paste int_file2.txt int_file3.txt > int_file4.txt
cut -f1,2,6 int_file4.txt > final.txt  
paste final.txt int_file1.txt > int_file5.txt
sed 's/chr//g' int_file5.txt > int_file6.txt 
awk '{if ($4 == 0) print $0}' int_file6.txt > snps.txt                                 
awk '{if ($4 != 0) print $0}' int_file6.txt > indels.txt                                 





