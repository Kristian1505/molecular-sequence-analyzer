from transcription import dna_transcription
from transcription import reverse_transcription

def display_menu():

    print("""
    -._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _   
        '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
    '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '.  '.
    : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : '.  `.
    '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.'   `.
            `-..,..-'       `-..,..-'       `-..,..-'       `         `
        
    --- DNA/RNA Transcription ---
    Choose an option:
          
    1. Transcribe DNA to RNA
    2. Reverse Transcribe RNA to DNA
    3. Exit
    """)

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("You chose: Transcribe DNA to RNA")
            sequence = input("Paste here your DNA sequence: ")
            sequence = sequence.upper()
            print(dna_transcription(sequence))

        elif choice == "2":
            print("You chose: Reverse Transcribe RNA to DNA")
            sequence = input("Paste here your RNA sequence: ")
            sequence = sequence.upper()
            print(reverse_transcription(sequence))

        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Wrong option")
        
        if input("If you want to try another strand press 1: ") != "1":
            break