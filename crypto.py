import random
import os.path
import base64
import sys
class NoModularInverse(Exception):
    pass
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx


def primeNumber(start,end,tab_prime_number):
    for val in range(start, end + 1):
        if val > 1:
            for n in range(2,val):
                if(val % n) == 0:
                    break
            else:
                tab_prime_number.append(val)
    #print (tab_prime_number)
    #Si on choisi le paramètre keygen
print("valeur de sys ",sys.argv[0])
if (len(sys.argv)>1):
    if (sys.argv[1]=="keygen"):
        if(len(sys.argv)<=2 and sys.argv[1]=="keygen"):
            print('Veuillez rentrer le fichier dans lequel rentrer la clé')
        else:
        ##########Génération de la clé publique ##########
            tab = []
            #Génération du tableau d'entier
            primeNumber(0,20,tab)

            print("tab",tab)
            #Génération de p
            p = random.choice(tab)
            print("p egale :",p)

            #Génération de q
            q = random.choice(tab)
            #Pour que q ne soit pas égale à P
            while q==p:
                q = random.choice(tab)
            print("q egale:",q)

            #Calcul de n
            n = p*q
            print("n egale",n,)

            #On calcul
            n_prime = (p-1)*(q-1)
            print(" n'egale ",n_prime,)

            # Trouver e et d
             #Génération d'un tableau de premier inférieur à n'
            tab2 = []
            primeNumber(0,n_prime,tab2)
            print("tab 2",tab2)
            e = random.choice(tab2)
            print("e egale ",e)
            #pour rentrer dans la boucle
            d = e
            while d ==e :
                d=multiplicative_inverse(e,n_prime)
                print('dans la boucle d =',d)
                e = random.choice(tab2)
                print('dans la boucle e =',e)
            print("d egale",d," e egale ",e)

            print ("\nCle publique (",e,",",n,")")
            print ("\nLa Cle privé (",n,",",d,")")



            hex_n = hex(n)
            hex_e = hex(e)
            hex_d = hex(d)


            #Génération du fichier
            public_Key = str(base64.b64encode((hex_n+'\n'+hex_e).encode()))
            print("La valeur hexa de n est ",hex_n,"La valeur de e est ",hex_e )

            #Génération du fichier de la clé public
            f = open(sys.argv[2]+".pub","w")
            f.write(" ---begin monRSA public key --- \n ")
            f.write(public_Key+'\n')
            f.write(" ---end monRSA key --- ")
            f = open(sys.argv[2]+".pub","r")
            contenu = f.read()
            print(contenu)
            f.close()

            #Génération du fichier de la clé privé
            public_Key = str(base64.b64encode((hex_n+'\n'+hex_d).encode()))
            print("La valeur hexa de n est ",hex_n,"La valeur de d est ",hex_d )

            f2 = open(sys.argv[2]+".priv","w")
            f2.write(" ---begin monRSA privateKe --- \n ")
            f2.write(public_Key+'\n')
            f2.write(" ---end monRSA key --- ")
            f2 = open(sys.argv[2]+".priv","r")
            contenu = f2.read()
            print(contenu)
            f2.close()
    if (sys.argv[1] == "crypt"):


    #Si les paramètres sont différents de ceux attendus
    if ((sys.argv[1] != "keygen") or(sys.argv[1] != "crypt") or (sys.argv[1] != "decrypt")):
        print("Rentrer un argument entre keygen + nom du fichier, crypt, decrypt")
    #Si aucun paramètre n'est rentré
else:
    print("aucun paramètre n'a été rentré")
