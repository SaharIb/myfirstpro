def clean (word):

    if (len(word)==1): return word 
    
    if word[0]==word[1]:
        return clean(word[1:])
    return word[0] + clean(word[1:])

word = "SSSaaaharrr"
print(clean(word))
