dna_transcription = {
    "A" : "U",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}
rna_transcription = {
    "A" : "T",
    "U" : "T",
    "C" : "G",
    "G" : "C" 
}

def transcription(sequence):

    rna_sequence = []   

    for i in sequence:

        rna_sequence.append(dna_transcription[i])

    return "".join(rna_sequence)



def reverse_transcription(sequence):

    dna_sequence = []

    for i in sequence:
        dna_sequence.append(rna_transcription[i])

    return "".join(dna_sequence)
