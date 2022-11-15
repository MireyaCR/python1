# Your code here!!


def sing() :

    lib='let it be'
    frase1= 'whisper words of wisdom'
    frase2= 'there will be an answer'
    cancion =''

    for i in range(1,9):
        cancion+=lib+', ' 
        if (i%4 == 0) :
            if (i/4==1):
                cancion += frase1+', '
                cancion += lib +', '     
            else:
                cancion += frase2+', ' 
                cancion += lib   
    return cancion

print(sing())
