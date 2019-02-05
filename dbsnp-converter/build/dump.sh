#!/bin/bash

for chrom in $(cat $1);
do
	echo $chrom
	sqlite3 -column -separator '\t' data/dbsnp.sqlite "select snp,'$chrom' as chrom, pos, ref_len, alt from $chrom;" >> $2
done
