import numpy as np
array1 = np.matrix("1 1 0 0 0 ; 1 1 1 0 0; 0 1 1 1 0; 0 0 1 1 1 ; 0 0 0 1 1 ")
array2 = np.matrix("1 0 0 0 0; 0 1 0 0 0 ; 0 0 1 0 0 ; 0 0 0 1 0 ; 0 0 0 0 1")
#resultat = np.matrix(np.zeros((5,5)))

def plus(a,b):
    if a==b:
        return 0
    else:
        return 1

def mult(a,b):
    if a==0 or b==0:
        return 0
    else:
        return 1

def addition(m1, m2):
    resultat = np.matrix("0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0")
    for x in range(5):
       for y in range(5):
           resultat[x, y] = plus(m1[x, y] , m2 [x, y])
    print(resultat)

def multiplication(m1,m2):
    resultat = np.matrix("0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0")
    for lig in range(5):
        for col in range(5):
            for a in range(5):
 
                resultat[lig, col] = plus(resultat[lig,col],mult(m1[lig,a], m2[a,col]))

    print(resultat)

def pivot(etape):
    

    # pivot : renvoie la ligne du 1er truc dont le coef est différent de 0 en haut à gauche, et de plus en plus à droite, qui prend en argument l'étape à laquelle on est
    # permuter : échange 2 lignes

# addition(array1, array2)
multiplication(array1,array2)
