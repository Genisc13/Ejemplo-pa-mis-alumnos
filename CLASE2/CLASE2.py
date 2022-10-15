"""
while True:
    Numero=int(input("Dime un numero primo para salir del bucle: "))
    if Numero==0:
        print("JAJAJA de locos es verdad")
        continue
    elif Numero==2 or Numero==3 or Numero==5 or Numero==7 or Numero==11:
        print("Es cierto, correcto")
        break
    elif Numero%2!=0 and Numero%3!=0 and Numero%5!=0 and Numero%7!=0 and Numero%11!=0 :
        print("Es cierto, correcto")
        break
    else:

        print("Cagaste, te quedaras aqui para siempre JAJAJAJAJAJA")
    print("Que buen codigo te sacaste")
"""
#repaso 1
"""
Quociente=170//8
residuo=44%2
print(str(Quociente) + "      "+ str(residuo))

Altura=float(input("Escribame algo: "))

if Altura<1.6:
    print("Lo siento eres muy bajito")
elif Altura>=1.6 and Altura<2.0:
    print("Estas en un rango aceptable")
else:
    print("Vaya pedazo de torre que eres")

"""

from this import d


print("Hola, la verdad es que ' asi ' es como se hace")


#Vectores y listas

words=["Hola","Que tal", "Esto es una lista?","De locos"]

Numbers=[2,5,7,9.6,8,10]

"""
print(words[0])
print(words[1])
print(words[2])
print(words[3])

print(Numbers[4])

Numbers[4]=5

print(Numbers)
"""

#matrices
'''
matrix=[[1,2,3],[1,4,7],[1,0,0]]
print(matrix)
print(matrix[1][2])

'''
"""
str="Hola buenas"
print(str[6])
"""
"""
x="DELOZOS"
print(x[1]+x[4])
"""

"""
nums=[1,2,3]
print(nums + [4,5,6])

print("Hola" in words)
print("Que" in words)
print("Tartamudo" in words)

y="Hola mundo"

if "Hola"in y:
    print("Hay un hola en y")

"""

#Deberes
#x=[42,2,5,7,123,884,75,37,139,11,342,446,33,77,55,73]
#y=[4,2,5,7,123,84,76,37,13,111,34,44,63,79,58,73]
#premio standard
#tres premios especiales

"""
print("Esto es la bonoloto, introduce un numero aleatorio de 3 cifras, puedes ganar premios!!!")
Importe=int(input("Pon aqui lo que quieras apostar: "))
Premnum=int(input("Estriba aqui el numero aleatorio: "))
Total=0
if (Premnum in x) and (Premnum in y):
    print("Felicidades ganaste 1000 euros!!!")
    Total=Importe+1000
elif Premnum in x:
    print("Felicidades ganaste 100 euros!!!")
    Total=Importe+100
else:
    print("No has dado ni uno")
    Total=Importe/2
    
if (Premnum in x) and Premnum==123:
    print("Ademas, has acertado un numero especial!! Te llevas una bicicleta")

if (Premnum in x) and Premnum==37:
    print("Ademas, wow eres epico, te vas a llevar un ferrari!!")

if (Premnum in x) and Premnum==446:
    print("Ademas, has acertado un numero especial!! Te llevas una Moto")

print("Has acabado con " + str(Total) + " euros")

if (Premnum==123) or (Premnum==37) or (Premnum==446):
    if Premnum==123:
        print("Ademas tienes una bici nueva")
    elif Premnum==37:
        print("Ademas tienes un ferrari")
    else:
        print("Ademas tienes una moto")
"""

#Listas, la continuación:
'''
x=[2,3,4,5,6,7]

Numero_2=0

for t in x:
    if t%2==1 and t>4:
        print(t)

'''

'''
nums = [1,2,3,4]
res=0

for r in nums:
    if(r%2==0):
        continue
    else:
        res += r
print(res)
'''

#Deberes
Deb=[1,5,6,7,9,3,6,7,2,3]

#hazme una operación en esta lista
# los 2 multiplican
# los 3 restan
# el resto suman
#ejemplo: deb=[1,4,3,2] --> Resultado :(1+4-3)*2
'''
Respuesta=0

for D in Deb:
    if D==2:
        Respuesta=Respuesta*2
    elif D==3:
        Respuesta=Respuesta-3
    else:
        Respuesta=Respuesta+D
print("La respuesta al calculo es: "+ str(Respuesta))
'''
#El usuario va a poner su peso y su altura, y el 
#Peso en kg
#altura en metros
#Peso/altura^2
# si, menos de 18.5 Underweight
# si entr 18.5-24.9 Normal
# por encima de 25 y por debajo de 29.9 tiene sobrepeso
# mas que esto es obesidad
'''
Davuri=float(input('Escribeme el peso que tienes vos:'))
Dabuten=float(input("Escribeme la altura que tienes vos (en metros):"))

IMC=Davuri/(Dabuten)**2

if IMC<18.5:
    print("Estas por debajo del peso (You are Underweight)")
elif IMC>=18.5 and IMC<=24.9:
    print("Eres normal, de locos, congratulations, you are nourmal ")
elif IMC>=25 and IMC<=29.9:
    print("Estas en sobrepeso, bueno es algo normal, tranqui")
elif IMC>29.9:
    print("Vaya, tienes un poquito de obesidad, no pasa nada, un poco de gym lo arregla")

print("Tu IMC actual es: "+ str(IMC))

'''
David=11;
Mauri=11;

nums=[1,2,3]
suma =0

"""
x=[2,4]
x+=[6,8]
print(x[2]//x[0])

print(nums*3)

N=nums*3
print(N)
print(N[7])

print(suma)
"""

"""
thislist = []
i=1
while i<=10:
    thislist.append(i)
    i+=1

print(thislist)
"""

thislist = ["apple", "banana","pineapple"]
thislist.remove("banana")
print(thislist)
