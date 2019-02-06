#!/usr/bin/env python

def block_information(first_variant):
	""" Takes HapCUT2 output fields for first block variant and returns the block ID and strand info 
	first_variant: haplotype data from HapCUT2 for first variant in block (list)

	Return values:
	block_id: position of variant (string)
	matching_field: field of haplotype output to check for strand match in other variants (int)
	"""
	block_id = first_variant[4]
	if first_variant[1] == '1':
		matching_field = 1
	elif first_variant[2] == '1':
		matching_field = 2
	return block_id, matching_field

def hapcut_to_vcf(hapcut, vcf, out_vcf):
	""" Converts HapCUT2 haplotype output and the VCF it came from into a GATK ReadBackedPhasing VCF
        hapcut: path to haplotype block output from HapCUT2
        vcf: path to unphased VCF used to run HapCUT2 and generate hapcut output
        out_vcf: path to write new phased VCF
        Return value: None
    """
	# Store haplotype blocks in a dictionary that links VCF line to block/strand info
	hapcut_dict = {}
	# Open HapCUT2 output for reading/processing
	with open(hapcut) as input_stream:
		# Initialize empty block list
		block = []
		for line in input_stream:
			if line.startswith("BLOCK"):
				# Skip block header lines
				continue
			elif line[0] == "*":
				# Reached end of block - process data and add to dictionary
				# Find block ID and strand matching field
				block_id, matching_field = block_information(block[0])
				# Process through block and link VCF line to block ID/strand info
				for entry in block:
					if entry[matching_field] == '1':
						hapcut_dict[int(entry[0])] = (block_id, 1)
					else:
						hapcut_dict[int(entry[0])] = (block_id, 0)
				# Reset block list for next block
				block = []
			else:
				# Store line data in block list
				block.append(line.strip().split("\t"))
	# Process last block - HapCUT2 files don't end with asterisk line to finish
	for entry in block:
		# Find block ID and strand matching field
		block_id, matching_field = block_information(block[0])
		# Process through block and link VCF line to block ID/strand info
		for entry in block:
			if entry[matching_field] == '1':
				hapcut_dict[int(entry[0])] = (block_id, 1)
			else:
				hapcut_dict[int(entry[0])] = (block_id, 0)
	# Process VCF and write output
	with open(vcf) as vcf_stream:
		with open(out_vcf, "w") as output_stream:
			line = vcf_stream.readline()
			if line.startswith('##'):
				output_stream.write(line)
				output_stream.write('##FORMAT=<ID=HP,Number=.,Type=String,Description="Read-backed phasing haplotype identifiers">\n')
			else:
				raise BadFormatError('VCF missing header lines')
			first_char = "#"
			while first_char == "#":
				line = vcf_stream.readline()
				try:
					first_char = line[0]
				except IndexError:
					first_char = "#"
				output_stream.write(line)
			counter = 1
			while line:
				if counter in hapcut_dict:
					tokens = line.strip().split("\t")
					hap_id = hapcut_dict[counter][0]
					if hapcut_dict[counter][1] == 1:
						hp_info = ''.join([hap_id, '-1,', hap_id, '-2'])
					else:
						hp_info = ''.join([hap_id, '-2,', hap_id, '-1'])
					format_field = ':'.join([tokens[8], "HP"])
					genotype_field = ':'.join([tokens[9], hp_info])
					output_line = tokens[0:8] + [format_field, genotype_field]
					output_stream.write('\t'.join(output_line) + '\n')
				else:
					output_stream.write(line)
				line = vcf_stream.readline()
				counter += 1

