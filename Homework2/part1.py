from sys import argv

key = {}
Linelist = []
for line in open(argv[1], "r"):
    Linelist.append(line.strip().split(" "))
    for i in range(0,len(Linelist)):
        if Linelist[i][0].isalpha():
         key[Linelist[i][0]] = Linelist[i][1]

def DNAtoProtien(myDNA):
    codon = ""
    count = 0
    protien = ""
    for Mynucleotide in myDNA:
        codon += Mynucleotide
        count +=1
        if count == 3:
            protien += key[codon]
            count = 0
            codon = ""
    return protien

print(DNAtoProtien("ATGGAAATAGATAGATAGATGAAAAGATAA"))
                                                                                
                                                                                
