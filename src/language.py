def detect_language(text):
    
    for character in text:
        #print(character)
        if "\u0400" <= character <= "\u04ff":
            return "Russian"
    return "English" 