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

def FrequencyMap_t(Text, k, t):
    """
    :param Text: where to look for k-mers
    :param k: length of the string patterns
    :param t: minimum number of repetitions of k-mer
    :return: all k-mers in Text that appears at least t times
    """
    result = []
    frequency = FrequencyMap(Text, k)
    for key in frequency:
        if frequency[key] >= t:
            result.append(key)

    return result

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

def ClumpFinding(genome, k, L, t):
    """
    Find patterns forming clumps in a string.
        Input: A string Genome, and integers k, L, and t. 
        Output: All distinct k-mers forming (L, t)-clumps in Genome.

    Given integers L and t, a k-mer Pattern forms an (L, t)-clump inside a (longer) string Genome if there is an interval of Genome of length L in which this k-mer appears at least t times
    """
    assert(t < L)
    result = set()
    for i in range(len(genome) - L + 1):
        genome_region = genome[i:i+L]
        frequency = FrequencyMap_t(genome_region, k, t)
        for k_mer in frequency:
            result.add(k_mer)
    return result

if __name__ == '__main__':
    text = 'CTTGATCATCTTGATCATCTTGATCAT'
    k = 4
    pattern = 'ATGATCAAG'
    #result = PatternMatching(pattern, text)
    #result = Pattern_Matching_for_cholerae()

    Text = 'GCGCG'

    print(ClumpFinding('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5, 50, 4))