# Step 1: Define the Morse code dictionary for encoding
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    "'": '.----.', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Step 2: Create a reverse dictionary for decoding
REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# Step 3: Define function to encode text to Morse code
def text_to_morse(text):
    morse = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append('?')  # Unknown character
    return ' '.join(morse)

# Step 4: Define function to decode Morse code to text
def morse_to_text(code):
    words = code.strip().split(' / ')  # Split Morse words by '/'
    decoded = []
    for word in words:
        letters = word.split()
        decoded_word = ''
        for letter in letters:
            decoded_word += REVERSE_MORSE_DICT.get(letter, '?')  # Unknown code
        decoded.append(decoded_word)
    return ' '.join(decoded)

# Step 5: Display menu and get user choice
def main():
    print("===== Morse Code Translator =====")
    print("1. Text to Morse")
    print("2. Morse to Text")
    choice = input("Enter your choice (1 or 2): ").strip()

    # Step 6: Handle encoding
    if choice == '1':
        text = input("Enter text to convert to Morse: ")
        result = text_to_morse(text)
        print("🔤 Morse Code:", result)

    # Step 7: Handle decoding
    elif choice == '2':
        code = input("Enter Morse code to convert to text:\n(use '/' for space between words): ")
        result = morse_to_text(code)
        print("📝 Decoded Text:", result)

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

# Step 8: Run the program
if __name__ == "__main__":
    main()
