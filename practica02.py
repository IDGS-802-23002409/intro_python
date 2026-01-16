import os 

def suma(a ,b):
    resultado = a+b
    return print(f"el resultado es:{resultado}")

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a * b 

def division(a,b):
    return a / b 

def salir():
    os.exit()
    
def main():
    print("selecciona una operacion para realizar:")
    funcion = int(input("operacion a realizar:"))
    while function != 0:
        if funcion == 1:
            a= int(input("ingresa el numero 1:"))
            b= int(input("ingresa el numero 2:"))
            suma(a,b)
        if funcion == 2:
            a= int(input("ingresa el numero 1:"))
            b= int(input("ingresa el numero 2:"))
            resta(a,b)
        if funcion == 3:
            a= int(input("ingresa el numero 1:"))
            b= int(input("ingresa el numero 2:"))
            multiplicacion(a,b)
        if funcion == 4:
            a= int(input("ingresa el numero 1:"))
            b= int(input("ingresa el numero 2:"))
            division(a,b)
        if funcion == 5:
            exit()
    
if __name__ == "__main__":
    main()
