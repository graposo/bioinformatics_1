
oriC_vibrio_cholerae = 'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC'

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    # hint: your code goes here!
    keys = freq.keys()
    for key in keys:
        freq[key] = PatternCount(Text, key)
    return freq

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    result = ''
    for char in Pattern:
        result = char + result
    return result

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    result = ''
    for char in Pattern:
        if char == 'A':
            result += 'T'
        elif char == 'T':
            result += 'A'
        elif char == 'C':
            result += 'G'
        elif char == 'G':
            result += 'C'
        else:
            print('error')
    return result

def PatternMatching(Pattern, Genome):
    positions = [] # output variable

    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)

    return positions

def Pattern_Matching_for_cholerae():
    with open('vibrio_cholerae_genome.txt') as genome_file:
        genome = genome_file.read()
        pattern = 'ATGATCAAG'
        return PatternMatching(pattern, genome)

if __name__ == '__main__':
    text = 'CTTGATCATCTTGATCATCTTGATCAT'
    k = 4
    pattern = 'ATGATCAAG'
    #result = PatternMatching(pattern, text)
    #result = Pattern_Matching_for_cholerae()

    Text = 'GCGCG'

    print(ReverseComplement('GATTACA'))