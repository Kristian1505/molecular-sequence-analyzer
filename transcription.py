# Notes:
# I chose to use generator expressions instead of list comprehension 
# because genetic material strands can be very large, and using a 
# generator helps optimize memory usage and improve performance.


# This dictionary maps DNA nucleotides to their corresponding RNA bases
dna_transcription_values = {
    "A" : "U",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}


# This dictionary maps RNA nucleotides to their corresponding DNA bases
rna_transcription_values = {
    "A" : "T",
    "U" : "A",
    "C" : "G",
    "G" : "C" 
}


# Converts a DNA sequence into its corresponding RNA sequence.
#
# Parameters:
# sequence (str): A string representing the DNA sequence.
#
# Returns:
# str: The transcribed RNA sequence.
def transcription(sequence):

    return "".join(dna_transcription_values[i] for i in sequence)


# Converts an RNA sequence back into its corresponding DNA sequence.
#
# Parameters:
# sequence (str): A string representing the RNA sequence.
#
# Returns:
# str: The reverse-transcribed DNA sequence.
def reverse_transcription(sequence):

    return "".join(rna_transcription_values[i] for i in sequence)