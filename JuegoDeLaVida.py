"""Nombres
    Lopez Granciano Mario Pablo 
    Lopez Valerio Leonardo Alexis
    Pintor Hernandez Emmanuel"""

"""Objetivo
    Generar una secuencia aleatoria de numeros binarios que represente una poblacion inicial 
    y a partir de esto mostrar la evolucion de un automata celular unidimensional, generando 
    triangulos de Sierpinski"""

"""FUNCIONES 
    random.randrange=Genera un numero aleatorio en un rango y un salto 
    random.choice = Genera un numero aleatorio, con base a una lista
    .copy = Copia una lista 
    .clear()= Vacia la lista """

import random
#011011001100101111010001010010001110100001100111011101100111010001000111
aux=[]
cadfi=[]
cad2=[]

#cadena=input("escribe la cadena ")
#print(cadena)
ciclos=int((random.randrange(1,100,1)))
m=0
num = ['0', '1']
#Generacion de la poblacion inicial aleatoria 
for m in range(ciclos):
    cad2.append(random.choice(num))
#cad2=list(cadena)
max=len(cad2)
print(cad2)
l=0
med=0


#ciclos=int(input("Numero de ciclos"))
#print(cad2[0])
#print(max)
print("numero de ciclos:"+str(ciclos))
erro=False
j=0
i=0
k=0
s=0
#Buscar algun numero que no sea binario
for l in range (len(cad2)):
    if cad2[l]=="1":
        erro=False
    elif cad2[l]=="0":
        erro=False
    else: 
        erro=True

"""Condicion en caso de que no exista algun error en la cadena """
if erro==False:
    #Caso de un solo numero binario en la poblacion 
    if(len(cad2))==1:
        cad2.clear()
        if (ciclos%2)!=0:
            med=int((ciclos/2)-0.5)
        else:
            med=int(ciclos/2)
        for k in range(ciclos):
            if k==med:
                cad2.append("1")
            else:
                cad2.append("0")
    #print(cad2)
    max=len(cad2)
    #print(max)
    """Imprimir la cadena de la poblacion inicial , expresandola con "*" y " " ."""
    for s in range(len(cad2)):
        if cad2[s]=="1":
            cadfi.append("*")
        else :
            cadfi.append(" ")
    #print(cadfi)
    au="".join(cadfi)
    print(au)
    cadfi.clear()
    """Ciclo para ir recorriendo el numero de ciclos , cada vez recorriendo la lista "cad2", ayudandonos 
    de la lista "cadfi" , que es la que almacenara los simbolos a mostrar .Y la lista "aux" que ocupamos para
    guardar la siguiente cadena obtenida a partir la evaluacion de la poblacio inicial .Posteriormente la lista auxilar
    se copia a la lista "cad2" para volverla a evaluar , repitiendo nuevamente el proceso mencionado"""
    
    for j in range(ciclos):
        for i in range(len(cad2)):
            if i==0: 
                if (cad2[0]=="0") and (cad2[1]=="0"):
                    cadfi.append(" ")
                    aux.append("0")
                else:
                    cadfi.append("*")
                    aux.append("1")
            elif i==max-1:
                if (cad2[max-1]=="0") and (cad2[max-2]=="0"):
                    cadfi.append(" ")
                    aux.append("0")
                else:
                    cadfi.append("*")
                    aux.append("1")
            else:
                if ((cad2[i-1]=="1") and (cad2[i]=="1") and (cad2[i+1]=="1")):
                    cadfi.append(" ")
                    aux.append("0")
                elif ((cad2[i-1]=="0") and (cad2[i]=="0") and (cad2[i+1]=="0")):
                    cadfi.append(" ")
                    aux.append("0")
                else:
                    cadfi.append("*")
                    aux.append("1")

        #print(cadfi)
        au="".join(cadfi)
        print(au)
        #print(aux)
        cad2=aux.copy()
        aux.clear()
        #print(aux)
        #print(cad2)
        cadfi.clear()
        #print(cadfi)
    cad2.clear()
else:
    print("Cadena Incorrecta\n")