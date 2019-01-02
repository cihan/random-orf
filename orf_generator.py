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
		print('Your randon ORF sequence is: ', orf)
		#calculate GC content of the ORF,
		gc=(orf.count('c')+orf.count('g'))/len(orf)*100
		print('Your sequence is ', str(len(orf)),'length. And your sequence include', str(float(round(gc,2))), '% GC bases.')
	else:
#output the random DNA sequence
		print('*'*40,'\n','No STOP Codon','\n','*'*40)
		print('Your random DNA sequence is: ', orf)
else:
	print('*'*40,'\n','No START Codon','\n','*'*40)
	print('Your random DNA sequence is: ', orf)

#BLAST this sequence...
#print('Your sequence is %s length. And your sequence include %s % GC bases.' % (str(len(orf)), str(len(orf))))