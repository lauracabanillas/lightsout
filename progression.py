
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
    # rend dans une liste []
    res=[]
    for lig in range(25):
        a = 0
        for col in range(25):
            a = plus(a, mult(m[lig,col],v[col]))
        res.append(a)
    return res 

def pivot(m,etape): 
    #renvoie le numéro du pivot qu'on va utiliser : le 1er avec un chiffre différent de 0
    n=len(m)
    np=etape #numéro d'étape provisoire
        
    for i in range(etape+1, n):#boucle sur les lignes restantes
        if abs(m[i, etape])>abs(m[np,etape]) :
            np=i
    return np

def transvection(mat, s): 
    #s est le numéro du pivot utilisé / additionne la ligne et la ligne du dessous
    n=len(mat)
    p=25
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








