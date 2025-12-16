from morse.mapping import MORSE

REVERSED_MORSE = {value: key for key, value in MORSE.items()}

def decode_word(morse_word):
    """
    Decodes a single Morse word into text.
    Letters are concatenated without spaces.
    """
    letters = []

    for code in morse_word.split():
        if code in REVERSED_MORSE:
            letters.append(REVERSED_MORSE[code])

    return "".join(letters)


def decode(morse_text):
    """
    Decodes Morse code into readable text.
    Words are separated by a pipe (|).
    """
    words = morse_text.split("|")
    decoded_words = [decode_word(w) for w in words]
    return " ".join(decoded_words)


if __name__ == "__main__":
    print(decode(".... . -.--|.--- ..- -.. ."))  # HEY JUDE
