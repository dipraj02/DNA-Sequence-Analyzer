# 🧬 DNA Sequence Analyzer

A lightweight Python tool to analyze DNA sequences — directly from a file or user input — and get insights like base composition, GC content, transcription, translation, and reverse complement.

---

## 🚀 Features

- ✅ **DNA Validation** – Ensures the input contains only valid bases: A, T, G, C
- 🔢 **Base Counting** – Counts total occurrences and percentage of each nucleotide
- 🧪 **GC Content Calculation** – Measures GC richness of the sequence
- 🔁 **Reverse Complement** – Generates the reverse complement strand
- 🔬 **Transcription** – Converts DNA to RNA by replacing T with U
- 🧬 **Translation** – Translates DNA into a protein sequence using a codon table

---

## 📦 Requirements

- Python 3.x  
*(No external libraries required)*

---

## 📁 Input Options

You can analyze DNA from:

1. **A text file** (`.txt`)  
   Format: Plain sequence (A/T/G/C only), optionally multiline

2. **Manual input**  
   Just paste your DNA sequence when prompted

---

## 🛠️ How It Works

Run the script: python dna_analyzer.py

Then follow the interactive prompt:
📂 Do you have a file? (yes/no): yes
📝 Enter your DNA file path or name (.txt): my_sequence.txt

Sample output:
✅ DNA is valid!

🧾 Base Count: {'A': 22, 'T': 20, 'G': 18, 'C': 15}
📊 Base Percentage: {'A': '29.33%', 'T': '26.67%', 'G': '24.00%', 'C': '20.00%'}

🧪 GC Content: 44.0%

🔁 RNA Sequence:
AUGCGUUAAG...

🧬 Protein Sequence:
Met-Arg-Stop...

🧬 Reverse Complement:
TTACGCTA...

---
