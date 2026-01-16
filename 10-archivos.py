from io import open

lectura = ""
text = open("archivo.txt,r")
lectura = text.readlines()
print(type(lectura))
print(lectura)
for i in lectura:
    print()
text.close()