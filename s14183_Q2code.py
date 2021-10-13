BRCA1seq= ""
with open ("seq2.fasta",'r') as file:
    for eachline in file:
        if eachline!= '\n' :
            eachline=eachline.strip()

            if(eachline[0]!='>’):
                BRCA1seq += eachline

freq ={}
for character in BRCA1seq:
    if character in freq:
        freq[character] += 1
    else:
        freq[character]=1
print("FullSequence'{}' is : \n {}". format(BRCA1seq, str(freq)))
