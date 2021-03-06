#generate random DNA sequence with length 200
import random
dna = ['a','t','g','c']
query_list = []
for i in range(201):
	query_list.append(random.choice(dna))
query_dna = ''.join(query_list)
orf=query_dna
#find matching bases (ie 'ATG')
if query_dna.find('atg') != -1:
#remove the noncoding bases before start codon
	orf=query_dna[query_dna.find('atg'):]
#look for the stop codons // Only TAA for now!
	if orf.find('taa') != -1:
		orf = orf[:orf.find('taa')+3]
#output the coding sequence
		print('Your randon ORF sequence is: ', orf.upper())
		#calculate GC content of the ORF,
		gc=(orf.count('c')+orf.count('g'))/len(orf)*100
		print('Your sequence is {} length. And your sequence include {}% GC bases.'.format((str(len(orf))), str(float(round(gc,2)))))
	else:
#output the random DNA sequence
		print('*'*40,'\n','No STOP Codon','\n','*'*40)
		print('Your random DNA sequence is: ', orf.upper())
else:
	print('*'*40,'\n','No START Codon','\n','*'*40)
	print('Your random DNA sequence is: ', orf.upper())

#BLAST this sequence...
