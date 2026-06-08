def read_fasta(filename):
    """
    функция которая читает FASTA-файл и возвращает заголовок и
    последовательность
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip()

    sequence = ''.join(line.strip() for line in lines[1:])

    return header, sequence

# Читаем файл
header, dna = read_fasta("mt_genome.fasta")

# print(f"Заголовок: {header[:100]}")
# print(f"Длина ДНК: {len(dna)}")
# print(f"Первые 100 символов: {dna[:100]}")
# print(f"Последние 100 символов: {dna[-100:]}")

def find_orfs_in_frame(dna, frame, min_len=300):
    """Функция для поиска ORF в заданной рамке чтения"""
    orfs = []
    i = frame
    while i < len(dna) - 2:
        if dna[i:i+3] == "ATG": #ищет первый попавшийся start codon
            j = i + 3 #делает шаг в 3 нуклеотида от start codon
            while j < len(dna) - 2: 
                if dna[j:j+3] in ["TAA", "TAG", "TGA"]: #ищет stop codon
                    orf_seq = dna[i:j+3]
                    if len(orf_seq) >= min_len:
                        orfs.append((i, j+2, orf_seq)) #start index, stop index, последовательность
                        break
                j += 3 
        i += 3
    return orfs

orfs = find_orfs_in_frame(dna, 0, min_len=300)
for start, stop, seq in orfs:
    print(f"ORF_1: {start}-{stop}, длина={len(seq)}, seq={seq}")

orfs = find_orfs_in_frame(dna, 1, min_len=300)
for start, stop, seq in orfs:
    print(f"ORF_2: {start}-{stop}, длина={len(seq)}, seq={seq}")

orfs = find_orfs_in_frame(dna, 2, min_len=300)
for start, stop, seq in orfs:
    print(f"ORF_3: {start}-{stop}, длина={len(seq)}, seq={seq}")