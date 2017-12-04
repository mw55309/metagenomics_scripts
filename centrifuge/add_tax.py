#!/usr/bin/env python

import sys

from ete3 import NCBITaxa

# get NCBI taxonomu object
ncbi = NCBITaxa()

# open the file
checkm_file = open(sys.argv[1], mode="r")

# skip three lines
row1 = checkm_file.readline()

# print titles for the output
titles = ["name",
		"taxID",
		"taxRank",
		"genomeSize",
		"numReads",
		"numUniqueReads",
		"abundance",
		"superkingdom",
		"kingdom",
		"phylum",
		"class",
		"order",
		"family",
		"genus"]

print '\t'.join(map(str,titles))

# iterate over file
for row in checkm_file:

	# split on whitespace
	arr = row.rstrip().split('\t')

	# only consider data lines
	if (len(arr) > 1):
		
		# get taxonomy free of the k__ bit	
		tax = arr[1]

		sk = ''
		k  = ''
		p  = ''
		c  = ''
		o  = ''
		f  = ''
		g  = ''

		# get entire lineage from this tax id
		try:
			lineage = ncbi.get_lineage(tax)
			#break
		except ValueError:
			print '\t'.join(map(str,arr)),'\t',
			print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (sk,k,p,c,o,f,g)
			continue
		
		# get all names for that lineage
		names = ncbi.get_taxid_translator(lineage)

		# iterate up the lineage mapping names
		# to each of our variables
		for l in lineage:
			rank = ncbi.get_rank([l])
			if rank[l] == 'superkingdom':
				sk = names[l]
			if rank[l] == 'kingdom':
                                k = names[l]
				
			if rank[l] == 'phylum':
                                p = names[l]

			if rank[l] == 'class':
                                c = names[l]

			if rank[l] == 'order':
                                o = names[l]

			if rank[l] == 'family':
                                f = names[l]

			if rank[l] == 'genus':
                                g = names[l]	
			
		# print it all out
		print '\t'.join(map(str,arr)),'\t',
		print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (sk,k,p,c,o,f,g)

# close file
checkm_file.close()
