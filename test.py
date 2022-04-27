import numpy as np
array1 = np.matrix("1 0 0 0 0 ; 1 0 1 0 1; 1 1 1 0 0; 0 0 1 0 1 ; 0 0 0 0 1 ")
array2 = np.matrix("0 0 0 0 0; 0 0 0 0 0 ; 0 0 0 0 0 ; 0 0 0 0 0 ; 0 0 0 0 0")
array_solvable = np.matrix("0 0 0 0 0; 0 0 1 0 0 ; 0 1 1 1 0 ; 0 0 1 0 0 ; 0 0 0 0 0")

v1=[0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0]
v2=[1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]
a=[1,2,3,4,5]
b=[1,2,3,4]
c=[1,0,0,-1]
d=[0,1,0,0,1]
g = [1,1,1,1,1]
e = len(array1)
f = len(array2[0])
laulau=np.zeros([e,f])
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


def mult_reel(chiffre, matrice):
    resultat = np.matrix("0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0")
    for lig in range(5):
        for col in range(5):
            resultat[lig, col]=mult(matrice[lig, col], chiffre)
    return resultat



def multiplication(m1,m2):

  #  resultat=np.zeros(len(m1), len(m2[0]))
    resultat = np.matrix("0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0;0 0 0 0 0")
    for lig in range(5):
        for col in range(5):
            for a in range(5):
                resultat[lig,col] = plus(resultat[lig,col],mult(m1[lig,a], m2[a,col]))
    return resultat

def mult_vecteur(m,v):
    res=[]
    for lig in range(5):
        a = 0
        for col in range(5):
            a = plus(a, mult(m[lig,col],v[col]))
        res.append(a)
    return res

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
            somme= plus(somme,mult(a[i],b[i]))
        if somme !=0:
            return False
        else:
            return True

def soluble(conf_init):
    v1=[0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0]
    v2=[1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]
    vecteur = []
    for i in range(len(conf_init)):
        for j in range(5):
            vecteur.append(conf_init[i,j])
           
    return (perpendiculaire(v1, vecteur) and perpendiculaire(v2,vecteur))
        


    # pivot : renvoie la ligne du 1er truc dont le coef est différent de 0 en haut à gauche, et de plus en plus à droite, qui prend en argument l'étape à laquelle on est
    # permuter : échange 2 lignes
#a=transvection2(array1,0)
#print(a)
print(mult_vecteur(array1,g))
