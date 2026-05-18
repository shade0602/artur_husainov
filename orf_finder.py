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
header, dna = read_fasta("mt_genome.fasta")  # замени на реальное имя

print(f"Заголовок: {header[:100]}")
print(f"Длина ДНК: {len(dna)}")
print(f"Первые 100 символов: {dna[:100]}")
print(f"Последние 100 символов: {dna[-100:]}")