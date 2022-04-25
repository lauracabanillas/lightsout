import numpy as np
array1 = np.matrix("1 1 0 0 0 ; 1 1 1 0 1; 1 1 1 0 0; 0 1 1 0 1 ; 0 0 0 1 1 ")
array2 = np.matrix("1 0 0 0 0; 0 1 0 0 0 ; 0 0 1 0 0 ; 0 0 0 1 0 ; 0 0 0 0 1")

A = np.matrix(" 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ;  0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ;  0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ;  0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ;  0 0 0 0 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ;0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 ;0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 ;0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 ;0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 ;0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 ;0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 ;0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 ;0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 1 ;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 ;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 ")


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


def mult_reel(chiffre, matrice):
    resultat = np.matrix("0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0")
    for lig in range(5):
        for col in range(5):
            resultat[lig, col]=mult(matrice[lig, col], chiffre)
    return resultat



def multiplication(m1,m2):
    resultat = np.matrix("0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0")
    for lig in range(5):
        for col in range(5):
            for a in range(5):
 
                resultat[lig, col] = plus(resultat[lig,col],mult(m1[lig,a], m2[a,col]))

    print(resultat)


def pivot(m,etape):
    n=len(m)
    np=etape #numéro d'étape provisoire
        
    for i in range(etape+1, n):#boucle sur les lignes restantes
        if abs(m[i, etape])>abs(m[np,etape]) :
            np=i
    return np

def transvection(mat, s): #s est le numéro du pivot utilisé
    n=len(mat)
    p=5
    result=mat
    for lig in range(s+1, n):
        for col in range(s,p):
            result[lig, col]=plus(result[lig,col], result[s,col])
    return result
        
def permute(m,i,j) :
    n=len(m)
    p=5
    mat=m # copie
    for k in range (p) : # boucle sur les colonnes
        mat[i,k],mat[j,k]=mat[j,k],mat[i,k]
    return mat

def solution(m):
    n=len(m)
    p=5
    sol=np.matrix("0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0")
    for i in range(n-1,-1,-1):
        sol[i]


def gauss(mat):
    n=len(mat)
    for s in range(n-1):
        piv=pivot(mat,s)
        if piv!=s:
            mat=permute(mat,s,piv)
        mat=transvection(mat,s)
    print(mat)

def perpendiculaire(a,b):
    somme=0
    if len(a)!=len(b):
        return False
    else:
        for i in range(len(a)):
            somme+= a[i]*b[i]
        if somme !=0:
            return False
        else:
            return True

def addition_ligne(mat, a,b): 
    result=mat
    for col in range (25):
        result[a, col]=plus(result[a,col], result[b,col])
    return result    



def pivot_de_gauss (matrice, etape):
    colonne = etape
    ligne_diff_0 = etape + 1
    while matrice[etape,colonne] == 0 :
        permute(matrice, etape, ligne_diff_0)
        ligne_diff_0 += 1
        print(matrice)
    for ligne in range (etape + 1,25):
        if matrice[ligne,colonne] != 0 :    
            permute (matrice,ligne,etape)
            print(matrice)
            print("")
            print("")
            print("")
    
    


def pivot_de_gauss_general (matrice):

    for i in range (25):
        pivot_de_gauss(matrice,i)
    
    return matrice
print(A)
print("")
print(pivot_de_gauss_general(A))








def pivot_de_gauss_I (mat, identite):
    matrice = mat
    I = identite
    for i in range(25) :
        colonne = i
        ligne_diff_0 = i + 1
        while matrice[i,colonne] == 0 and ligne_diff_0 < 25:
            permute(matrice, i, ligne_diff_0)
            permute(I, i, ligne_diff_0)
            ligne_diff_0 += 1
        for ligne in range (i + 1,25):
            if matrice[ligne,colonne] != 0 :    
                addition_ligne(matrice,ligne,i)
                addition_ligne(I,ligne,i)
    return I








