# 🧬 Molecular Sequence Analyzer

**Molecular Sequence Analyzer** is a command-line tool designed for converting DNA sequences into RNA (transcription) and vice versa (reverse transcription). This project serves as a practice in **Python programming**, particularly in handling **string manipulations, user interaction, and efficient memory usage** with generator expressions.

## 🚀 Features

- **🔬 DNA to RNA Transcription** – Converts a given DNA sequence into its complementary RNA sequence.
- **🧪 RNA to DNA Reverse Transcription** – Converts a given RNA sequence back into its corresponding DNA sequence.
- **📜 Menu-driven Interface** – Simple user interaction via a text-based menu.
- **⚡ Optimized Performance** – Uses generator expressions to handle large genetic sequences efficiently.

## 🛠️ Tech Stack

- **Language**: Python  
- **Concepts Used**: Functions, Loops, Conditionals, String Manipulation, User Input

## 📂 Project Structure

- `main.py` – Runs the application and calls the menu.
- `menu.py` – Displays the menu and handles user input.
- `transcription.py` – Contains functions for DNA transcription and reverse transcription.

## 🏗️ Installation and Usage

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Kristian1505/molecular-sequence-analyzer.git
   ```
2. **Navigate to the project directory**:
   ```sh
   cd molecular-sequence-analyzer
   ```
3. **Run the program**:
   ```sh
   python main.py
   ```

## 📌 Example Usage

```
--- DNA/RNA Transcription Tool---

Please select an option:

1. Convert DNA to RNA (Transcription)
2. Convert RNA to DNA (Reverse Transcription)
3. Exit

Enter your choice (1-3): 1
You selected: DNA to RNA Transcription
Enter the DNA sequence for transcription: ATCG
Result: UAGC
```

## ⚠️ Error Handling

- **Invalid Inputs**: Prompts users to enter only valid DNA or RNA sequences (A, T, C, G for DNA; A, U, C, G for RNA).
- **Invalid Selection**: Displays an error message when an option outside 1-3 is selected.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements, bug fixes, or additional features.

## 📄 License

This project does not have a specific license. You are free to use and modify it as needed.

---

Made with 🧬 by Kristian

