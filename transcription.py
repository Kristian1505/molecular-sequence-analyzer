dna_transcription = {
    "A" : "U",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}
reverse_transcription = {
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