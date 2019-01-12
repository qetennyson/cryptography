import string

message = 'tolgx,pjrgiyv!ugmv?gq,twzgv;lyg13gsh "gkvnza'
ALPHA = string.ascii_letters + '.,;!?" ' + '0123456789'

for key in range(len(ALPHA)):

    translated = ''
    for letter in message:
        # access every letter in the message to subtract our key guess from it, and add it to our
        # potentially translated text.
        if letter in ALPHA:
            poss = ALPHA.index(letter) - key

            if poss >= len(ALPHA):
                poss -= len(ALPHA)
            elif poss < 0:
                poss += len(ALPHA)

            translated += ALPHA[poss]

    print(f"Key of {key}: {translated}")



