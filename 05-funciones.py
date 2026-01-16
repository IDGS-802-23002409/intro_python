import os 
def saludar (nombre):
    return f"hola{nombre}"

def suma(a, b):
    return a + b

os.system("cls")

os.system("pause")

def main():
    os.system("cls")
    saludar("Juan")
    resultado_suma = suma(5,7)
    print("la suma de 5 y 7 es:", resultado_suma)
    
    if __name__ == "__main__":
        main()