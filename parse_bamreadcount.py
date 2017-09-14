#Summarize the output of bam_readcount
#OG script nickmiller-iit
#edited Sridhar September 14 2017
#https://github.com/genome/bam-readcount
#
#The format of the bam_readcount output is a set of tab delimited columns
#
#	1) Chromosome
#	2) Position
#	3) Reference base
#	4) Depth
#	5) Base info field 1
#	...
#	5+n) Base info field n
#
#Each base info field contains sub fields separated by colons We are o ly interested in
#the first two:
#
#	1) Base
#	2) Count
#
#The base subfield can take various values:
#	=	Same as the reference,never used (see: https://www.biostars.org/p/82993/) so we
#	 	can ignore it
#	A
#	C
#	G
#	T
#	N
#	Strings that appear to represent indels, we will ignore these too.
#
#
#Output will be a tab delimited table:
#
#Chromosome	Position	Reference	A	C	G	T	N
#
#Where A, C, G, T & N are the counts for each base

from __future__ import print_function
import sys

inFileName = sys.argv[1]
print("\t".join(["chromosome", "position", "reference", "A", "C", "G", "T", "N", "+A", "+G", "+GG", "+GGG"]))
inFile = open(inFileName, 'rU')

for line in inFile:
	line = line.split('\t')
	outLine = line[:3]
	outBases = ["A", "C", "G", "T", "N", "+A", "+G", "+GG", "+GGG"]
	outCounts = [0 for x in range(0,9)]	
	for element in line[4:]:
		base = element.split(':')[0]
		count = element.split(':')[1]
		for i in range(0,9):
			if base == outBases[i]:
				outCounts[i] += int(count)
	print('\t'.join((outLine + [str(x) for x in outCounts])))

inFile.close()