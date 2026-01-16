import os

def main():
    print("Ingrese 20 numeros para ordenarlos en una lista, contar las veces que se repitieron y separarlos en pares e impares")
    
    lista=[]
    pares=[]
    impares=[]
    repetidos=[]
    
    for i in range(20):
        numero=int(input("Numero {}:".format(i+1)))
        lista.append(numero)
        if(lista.count(numero)>1):
            repetidos.append(numero)
            
        if(numero%2==0):
            pares.append(numero)
        else:
            impares.append(numero)
        
    lista.sort()
    print("Lista ordenada:",lista)
    print("Pares:",pares)
    print("Impares:",impares)
    print("Repetidos:",repetidos)
    os.system("pause")

if __name__ == "_main_":
    main()