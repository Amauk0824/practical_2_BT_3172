BRCA1seq= ""
with open ("seq2.fasta",'r') as seqfile:
    for eachline in seqfile:
        if eachline!= '\n' :
            eachline=eachline.strip()

            if(eachline[0]!='>'):
                BRCA1seq += eachline
counter = 0
for base in BRACA1seq:
    counter+=1
print("Tota1 bases Length of the BRCA1 sequence: ", counter)
