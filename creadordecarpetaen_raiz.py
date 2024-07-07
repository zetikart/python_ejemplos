import os
print(os.getcwd()) 
#muestra donde esta ubicado ahora el codigo

print(os.listdir)# listar los archivod de mi actual ubicacion

list = os.listdir()

for file in list:
    print(file)
    print('')

#moverme de directorio raiz
#os.chdir("C:\Windows\System32")
os.chdir("C:\Windows\System32")
print("estoy en directorio raiz")
print(os.getcwd()) 


# creamos una carpeta
os.mkdir("carpetita")

os.path.exists("carpetita")


#eliminarl un archivo
#os.remove("carpe")

if os.path.exists("carpetita") == True:
    print("la carpeta ya existe, asi que no hago nada")
else:
    os.mkdir("carpetita")

print("estoy en carpetita")
os.chdir("C:\Windows\System32\carpetita")


print("voy a crear un fichero en carpetita")

f = open('fichero' , 'w')
f.write('el fichero abierto en modo escrituran')
