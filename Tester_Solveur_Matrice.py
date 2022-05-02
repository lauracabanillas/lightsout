import numpy as np

A = np.matrix(" 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 0 0 1 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 ")
I = np.matrix(" 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 ")



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

def addition25(m1, m2):
    #addition 2 matrices 25
    resultat = np.matrix("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ")
    for x in range(25):
       for y in range(25):
           resultat[x, y] = plus(m1[x, y] , m2 [x, y])
    return resultat

def multiplication25(m1,m2):
    #multiplication 2 matrices 25
    resultat = np.matrix("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ")
    for lig in range(25):
        for col in range(25):
            for a in range(25):
                 resultat[lig, col] = plus(resultat[lig,col],mult(m1[lig,a], m2[a,col]))
    return resultat

def mult_vecteur(m,v):
    #multiplication matrice 25 par vecteur 25
    # rend dans une liste []
    res=[]
    for lig in range(25):
        a = 0
        for col in range(25):
            a = plus(a, mult(m[lig,col],v[col]))
        res.append(a)
    return res 

def permute(mat,a,b) :  
    #permute lignes a et b de matrice de 25
    for colonne in range (25) : # boucle sur les colonnes
        mat[a,colonne],mat[b,colonne]=mat[b,colonne],mat[a,colonne]
    return mat  

def addition_ligne(mat,a,b): 
    #additione les lignes a et b, les remet dans a de la matrice de 25
    result=mat
    for col in range (25):
        result[a,col]=plus(result[a,col], result[b,col])
    return result   

def pivot_de_gauss(A, I):
    #fait le pivot de A en effectuant les mêmes actions sur I
    
    #retourne A_modif et I_modif dans un tuple
    #mais problèmes
    #il modifie A et I pris en arguments
    A_modif = A
    I_modif = I
    for i in range(25) :
        colonne = i
        ligne_diff_0 = i + 1
        while A_modif[i,colonne] == 0 and ligne_diff_0 < 25:
            permute(A_modif, i, ligne_diff_0)
            permute(I_modif, i, ligne_diff_0)
            ligne_diff_0 += 1
        for ligne in range (0,i):
            if A_modif[ligne,colonne] != 0 :    
                addition_ligne(A_modif,ligne,i)
                addition_ligne(I_modif,ligne,i)  
        for ligne in range (i + 1,25):
            if A_modif[ligne,colonne] != 0 :    
                addition_ligne(A_modif,ligne,i)
                addition_ligne(I_modif,ligne,i)
    return A_modif, I_modif

def recup_vecteur_colonne(mat,numero): 
    #renvoie le vecteur de 25 de la colonne choisie (allant de 1 a 25) 'numero' en liste
    vect = []
    for ligne in range(0,25):
        vect = vect + [mat[ligne,numero-1]]
    return vect

def perpendiculaire(a,b):
    #vérifie si 2 vecteurs sont perpendiculaires
    somme=0
    if len(a)!=len(b):
        return False
    else:
        for i in range(len(a)):
            somme= plus(somme,mult(a[i],b[i]))
        if somme !=0:
            return False
        else:
            return True

def vecteur25_to_matrice(v):
    #transforme vecteur 25 en matrice 5
    mat_finale = [[v[i] for i in range(5)],[v[i] for i in [5,6,7,8,9]], [v[i] for i in [10,11,12,13,14]], [v[i] for i in [15,16,17,18,19]], [v[i] for i in [20,21,22,23,24]]]   
    return np.matrix(mat_finale)

def soluble(conf_init):
    #dit si config soluble 
    v1=[0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0]
    v2=[1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]
    vecteur = []
    for i in range(len(conf_init)):
        for j in range(5):
            vecteur.append(conf_init[i,j])
           
    return (perpendiculaire(v1, vecteur) and perpendiculaire(v2,vecteur))

def solution(conf_init): 
    #renvoie solution en matrice
    I_modif = np.matrix("0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 1 0 1 0 0 0 1 1 1 0; 0 1 1 1 0 1 1 1 0 1 0 0 1 1 1 1 0 1 1 1 1 0 1 0 1; 0 1 1 0 0 1 0 1 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 1 1; 0 1 0 0 1 1 1 1 0 1 0 0 0 0 0 1 1 1 0 1 0 1 0 0 1; 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0 1 0 0 0 0 1 0 1 1 0; 1 1 1 1 0 0 1 1 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 1 1; 0 1 0 1 0 1 1 0 1 1 0 0 0 1 0 1 1 1 0 0 0 1 0 0 0; 0 1 1 1 1 1 0 1 1 0 1 1 0 1 0 1 0 1 0 1 0 1 1 1 1; 0 0 1 0 0 0 1 1 1 0 1 0 0 1 1 1 0 0 1 0 0 1 1 0 0; 0 1 0 1 1 1 1 0 0 0 0 1 1 1 0 0 1 1 0 1 1 1 1 1 1; 1 0 1 0 0 1 0 1 1 0 0 0 1 0 1 0 1 0 1 1 1 1 1 0 1; 1 0 1 0 1 1 0 1 0 1 0 0 0 0 0 1 1 1 0 1 0 1 0 0 1; 0 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 0 1 0 0 1 1 0 0 0; 0 1 0 0 1 1 1 1 1 1 0 0 1 1 1 1 0 1 1 1 1 0 1 0 1; 0 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 1 1 1 1 0 0 1 0 1; 1 1 1 1 1 0 1 1 1 0 0 1 0 1 0 1 0 1 0 1 0 1 1 1 1; 0 0 1 1 0 0 1 0 0 1 1 1 0 0 1 0 1 1 1 0 0 0 1 0 0; 1 1 1 1 0 0 1 1 0 1 0 1 1 1 1 1 1 0 1 1 0 1 0 1 1; 0 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 1 1 1 0 0 0 1 0 0; 0 1 1 1 0 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1 0 1 1 1 1; 0 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 1 1 0; 1 0 0 1 0 1 1 1 1 1 1 1 1 0 0 1 0 1 0 1 0 1 0 0 1; 1 1 0 0 1 0 0 1 1 1 1 0 0 1 1 1 1 0 1 1 1 0 0 1 1; 1 0 1 0 1 1 0 1 0 1 0 0 0 0 0 1 0 1 0 1 1 0 1 0 1; 0 1 1 1 0 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1 0 1 1 1 0")
    vecteur_init = []
    for i in range(len(conf_init)):
        for j in range(5):
            vecteur_init.append(conf_init[i,j])
    return vecteur25_to_matrice(mult_vecteur(I_modif,vecteur_init)) 



array_solvable1 = np.matrix("0 0 0 0 0; 0 0 1 0 0 ; 0 1 1 1 0 ; 0 0 1 0 0 ; 0 0 0 0 0")
array_solvable2 = np.matrix("1 1 0 1 1; 1 0 0 0 1 ; 0 0 0 0 0 ; 0 0 0 0 1 ; 0 0 0 1 1")
array_solvable3 = np.matrix("0 1 0 0 0; 1 1 1 1 0 ; 0 1 1 1 1 ; 0 0 0 1 0 ; 0 0 0 0 0")
array_solvable4 = np.matrix("1 0 0 0 0; 1 1 0 0 0 ;1 0 0 0 0 ;  0 0 0 0 0 ;  0 0 0 0 0")
array_solvable5 = np.matrix("1 0 0 0 0; 1 1 0 0 0 ;1 0 0 0 0 ;  0 0 0 0 1 ;  0 0 0 1 1")

array_nonsolvable1 = np.matrix("1 0 0 0 0; 0 0 0 0 0 ;0 0 0 0 0 ;  0 0 0 0 0 ;  0 0 0 0 0")



pivot = pivot_de_gauss(A,I)

A_modif = pivot[0]
I_modif = pivot[1]


#print(solution(array_solvable1))
print("")


print(array_solvable2)
print(solution(array_solvable2))
print("")

#print(solution(array_solvable3))
print("")
#print(soluble(array_solvable4))
print("")
#print(soluble(array_solvable5))
print("")
