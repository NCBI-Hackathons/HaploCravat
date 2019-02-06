create table dbsnp (
	rsid int,
	chrom text,
	pos int,
	ref_len int,
	alt text
);
create index rsid_idx on dbsnp (rsid);
