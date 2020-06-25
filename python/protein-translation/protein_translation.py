codons ={   
            'AUG':'Methionine',
            'UUU': 'Phenylalanine', 'UUC':'Phenylalanine', 
            'UUA':'Leucine', 'UUG': 'Leucine', 
            'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine', 
            'UAU':'Tyrosine', 'UAC':'Tyrosine', 
            'UGU':'Cysteine', 'UGC':'Cysteine', 
            'UGG':'Tryptophan', 
            'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'
        }

def proteins(strand):
    protein_lst = []
    n=0
    while n != len(strand):
        codon = strand[n:(n+3)]
        protein = codons[codon]
        if protein == 'STOP':
            break
        else:
            protein_lst.append(protein)
        n+=3
    return protein_lst