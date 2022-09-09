from sys import argv

#Dict for codon to protien
key = {}
Linelist = []
for line in open(argv[2], "r"):
    Linelist.append(line.strip().split(" "))
for i in range(0,len(Linelist)):
    if Linelist[i][0].isalpha():
        key[Linelist[i][0]] = Linelist[i][1]

#reads a sequence and turns the sequence into a list of protiens
def DNAtoProtien(myDNA):
    codon = ""
    count = 0
    protien = ""
    for Mynucleotide in myDNA:
        codon += Mynucleotide
        count +=1
        if count == 3:
            protien += key[codon]
            if key[codon] == "-":
                return protien
            else:
                count = 0
                codon = ""
    return protien

#Reads an .fa file into a sequence
Linelist2 = []

for line2 in open(argv[1],"r"):
    if ">" not in line2:
        Linelist2.append(line2.strip())
DNA = "".join(Linelist2)

#breaks the sequence into list of translations
def SeqtoTransl (Myseq, MyDict):
    TList = []
    seq = ""
    index = -1
    
    for base in Myseq.upper():
        seq += base
        index += 1
        if "ATG" in seq:
            seq = ""
            TList.append(Myseq[(index - 2):].upper())
    return TList

#translate a list of DNA to a list of protiens
def ConvertList (MyList):
    ProtienList = []
    for translate in MyList:
        Protiens = DNAtoProtien(translate)
        if Protiens[-1] != '-':
            continue
        else:
            ProtienList.append(Protiens)

    return ProtienList

#reverse sequence
def ReverseSequence (Myseq):
    ReverseSeq = Myseq[::-1].upper()
    Reverse = ""

    for i in range(0,len(Myseq)-1):
        if ReverseSeq[i] == 'A':
            Reverse += 'T'
        elif ReverseSeq[i] == 'T':
            Reverse += 'A'
        elif ReverseSeq[i] == 'G':
            Reverse += 'C'
        elif ReverseSeq[i] =='C':
            Reverse += 'G'
    return Reverse

#main
TranslList = SeqtoTransl(DNA, key)
PossibleP = ConvertList(TranslList)
ReverseDNA = ReverseSequence(DNA)
TranslList2 = SeqtoTransl(ReverseDNA,key)
PossibleP2 = ConvertList(TranslList2)

print("possible protiens are:")
for protien in PossibleP:
    print(protien)
for protien in PossibleP2:
    print(protien)
