#generate random DNA sequence with length 200
import random
dna = ['a','t','g','c']
query_list = []
for i in range(201):
	query_list.append(random.choice(dna))
query_dna = ''.join(query_list)
print(query_dna)
#find matching bases (ie 'ATG')

#remove the noncoding bases before start codon

#look for the stop codons

#output the coding sequence

#calculate GC content of the ORF

#BLAST this sequence...
