create table dbsnp (
	rsid int primary key asc,
	chrom text,
	pos int,
	ref_len int,
	alt text
);
