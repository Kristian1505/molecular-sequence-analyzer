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
        
--- DNA/RNA Transcription Tool---
""", end="")

    while True:
        
        print("""
Please select an option:
                
1. Convert DNA to RNA (Transcription)
2. Convert RNA to DNA (Reverse Transcription)
3. Exit
        """)
        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("You selected: DNA to RNA Transcription")
            sequence = input("Enter the DNA sequence for transcription: ").upper()
            #sequence = sequence.upper()
            print(dna_transcription(sequence))

        elif choice == "2":
            print("You selected: RNA to DNA Reverse Transcription")
            sequence = input("Enter the RNA sequence for reverse transcription: ").upper()
            #sequence = sequence.upper()
            print(reverse_transcription(sequence))

        elif choice == "3":
            print("Thank you for using the DNA/RNA Transcription Tool.")
            break
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")
        
        if input("Press 1 to process another sequence or any other key to exit: ") != "1":
            print("Thank you for using the DNA/RNA Transcription Tool.")
            break