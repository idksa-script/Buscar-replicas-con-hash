import pathlib
import hashlib as hs 

def archivo_hash(archivo):
    hash_obj = hs.new("sha256")
    with open(archivo, "rb") as ar:
        for bloque in  iter(lambda: ar.read(4096), b""):
            hash_obj.update(bloque)
    return hash_obj.hexdigest()


#Pide la carpeta donde se buscara los archivos similares
directorio = pathlib.Path(input("Introduce la carpeta: "))

print("Explorando carpeta....")

lista1 = []
lista2 = []

for item in directorio.rglob("*"):
    if item.is_dir():
        print(f"Carpeta: {item}")
    elif item.is_file():
        #print(f"Archivo: {item}")
        lista1.append(item)
        lista2.append(archivo_hash(item))
    

