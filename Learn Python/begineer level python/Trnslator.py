def translate(phrase):
    translator = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translator = translator + "G"
            else:
                translator = translator + "g"
        else:
            translator = translator + letter
    return translator

print(translate(input("Enter a phrase: ")))
                
        