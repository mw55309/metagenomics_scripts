# metagenomics_scripts

Miscellaneous scripts for metagenomics

## checkM
### add taxonomic lineage to checkM results

```bash
python add_tax.py checkm.txt > checkm_clean.tsv
```

## Centrifuge
### add taxonomic lineage to  Centrifuge results

```bash
python add_tax.py centrifuge.tsv > centrifuge.plus.tsv
```

We can then generate some reports:

```bash
#
# $6 below is uniqueReads
# $5 would be totalReads
#

# superkingdom
awk -F"\t" '{a[$8] += $6} END{for (i in a) print i, a[i]}' centrifuge.plus.tsv | sort -n -k 2 -r

# phylum
awk -F"\t" '{a[$10] += $6} END{for (i in a) print i, a[i]}' centrifuge.plus.tsv | sort -n -k 2 -r

# class
awk -F"\t" '{a[$11] += $6} END{for (i in a) print i, a[i]}' centrifuge.plus.tsv | sort -n -k 2 -r

```
