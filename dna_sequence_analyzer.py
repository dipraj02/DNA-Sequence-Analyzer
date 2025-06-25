# DNA SEQUENCE ANALYZER PROJECT

# Read DNA sequence from a file
def read_dna_sequence(file_path):
    try:
        with open(file_path,'r') as f:
            sequence = f.read()
            return sequence.upper().replace('\n','')
    except FileNotFoundError:
        print(f'❌ File {file_path} Not Found.')
        return ''
    
# Checks whether the file contains valid DNA base pair
def valid_dna(seq):
    return all(base in 'ATGC' for base in seq)

# Count the bases and it's percentage present in DNA
def count_bases(seq):
    total = len(seq)
    base_counts = {base: seq.count(base) for base in 'ATGC'}
    base_percentage = {base: f"{(count/total *100):.2f}%" for base, count in base_counts.items()}
    return base_counts, base_percentage

# Calculate GC content percentage
def gc_calculation(seq):
    gc_content = seq.count('G') +  seq.count('C')
    return round((gc_content/len(seq))*100,2)

# Get reverse complement of DNA
def reverse_complement(seq):
    complement = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    result = ''
    for base in reversed(seq):
        result += complement.get(base)
    return result


# Transcribe DNA to RNA
def transcription(seq):
    rna = seq.replace('T','U')
    return rna

# Translate DNA to Protein
def translate_dna(seq):
    codon_table = {
    'ATA': 'Ile', 'ATC': 'Ile', 'ATT': 'Ile', 'ATG': 'Met',
    'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACT': 'Thr',
    'AAC': 'Asn', 'AAT': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGC': 'Ser', 'AGT': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu',
    'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCT': 'Pro',
    'CAC': 'His', 'CAT': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGT': 'Arg',
    'GTA': 'Val', 'GTC': 'Val', 'GTG': 'Val', 'GTT': 'Val',
    'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCT': 'Ala',
    'GAC': 'Asp', 'GAT': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGT': 'Gly',
    'TCA': 'Ser', 'TCC': 'Ser', 'TCG': 'Ser', 'TCT': 'Ser',
    'TTC': 'Phe', 'TTT': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu',
    'TAC': 'Tyr', 'TAT': 'Tyr', 'TAA': 'STOP', 'TAG': 'STOP',
    'TGC': 'Cys', 'TGT': 'Cys', 'TGA': 'STOP', 'TGG': 'Trp',
}
    protein = []

    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        amino_acid = codon_table.get(codon, 'X')
        protein.append(amino_acid)
    return '-'.join(protein)

# Main Program
if __name__ == "__main__":
    print("🧬 Welcome to DNA Sequence Analyzer 🔍")
    print("=====================================")

    choice = input("📂 Do you have a file? (yes/no): ").strip().lower()

    if choice == 'yes':
        file_path = input("Enter your DNA file path or file name (.txt): ")
        dna_seq = read_dna_sequence(file_path)
    else:
        dna_seq = input("📝 Paste your DNA sequence directly: ").upper().replace('\n','').replace(' ','')

    if valid_dna(dna_seq):
        print('\n ✅ DNA is valid \n')
        print("🔎 DNA Sequence Analysis")
        print("========================")

        base_number , base_percent = count_bases(dna_seq)
        print('\n 🧾 Base Count:', base_number )
        print('\n 📊 Base Percentage:', base_percent )

        gc = gc_calculation(dna_seq)
        print(f'\n🧪 GC Content:{gc}%')

        protein_seq = translate_dna(dna_seq)
        print("\n🧬 Protein Sequence:")
        print(protein_seq)

        rna_seq = transcription(dna_seq)
        print('\n🧬 RNA Sequence:', rna_seq)

    else:
        print("Invalid DNA sequence. Only A, T, G, C allowed.")
    
    print("\n✅ Thanks for using DNA Sequence Analyzer🔬")