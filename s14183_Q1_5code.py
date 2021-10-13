BRCA1seq= ""
with open ("seq2.fasta",'r') as seqfile:
    for eachline in seqfile:
        if eachline!= '\n' :
            eachline=eachline.strip()

            if(eachline[0]!='>'):
                BRCA1seq += eachline

print("Total bases Length of the BRCA1 sequence: ", len(BRCA1seq))
