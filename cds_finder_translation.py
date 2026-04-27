dna = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC"
# 1 Найти старт-кодон — первую позицию (индекс), где встречается подстрока "ATG".
start_index = dna.find("ATG")
print(f"start codon index: {start_index}")

# 2 Найти стоп-кодон — одну из трёх подстрок: "TAA", "TAG" или "TGA". Найдите первый стоп-кодон
for i in range(start_index + 3, len(dna), 3):
     codon = dna[i:i+3]
     if codon in ["TAA", "TAG", "TGA"]:
          stop_index = i
          stop_codon = codon
          break
print(f"stop codon {stop_codon} index: {stop_index}")

# 3 Вырезать кодирующую последовательность (CDS — coding sequence) — то есть взять часть ДНК от старт-кодона включительно до стоп-кодона включительно.
cds = dna[start_index : stop_index + 3]
print(f"\nCDS: {cds}")
print(f"CDS length: {len(cds)}")

# 4 Перевести её в РНК — заменить все "T" на "U"
rna = cds.replace("T", "U")
print(f"\nRNA: {rna}")

# 5 Посчитать длину полученной РНК (количество символов).
print(f"RNA length: {len(rna)}")

# 6 словарь генетического кода
genetic_code = {
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGA": "R",
    "AGG": "R",
    "GAU": "D",
    "GAC": "D",
    "AAU": "N",
    "AAC": "N",
    "UGU": "C",
    "UGC": "C",
    "GAA": "E",
    "GAG": "E",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "CAU": "H",
    "CAC": "H",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "CAA": "Q",
    "CAG": "Q",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "UUA": "L",
    "UUG": "L",
    "AAA": "K",
    "AAG": "K",
    "UUU": "F",
    "UUC": "F",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "AGU": "S",
    "AGC": "S",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "UGG": "W",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "*",
    "UGA": "*",
    "UAG": "*",
    "AUG": "M"
    }

# 7 перебор последовательности и сравнение с генетическим кодом
protein = ""
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if codon in genetic_code:
        amino = genetic_code[codon]
        if amino == "*":
            break
        protein += amino
print(f"\namino acid sequence: {protein}")
print(len(protein))