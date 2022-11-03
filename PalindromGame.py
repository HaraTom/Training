while (True):
    text = input("Enter your text and I will check the text is palindrom. For end of this game enter 'exit': ")
    if text == 'exit':
        break
    else:
        lowerText = text.lower()
        finalText = ""
        for character in lowerText:
            if character.isalnum():
                finalText += character
        palindrom = finalText == finalText[::-1]
        if palindrom == True:
            print("Great! Your text is a palindrom!")
        else:
            print("Sorry, but your text is not a palindrom.")