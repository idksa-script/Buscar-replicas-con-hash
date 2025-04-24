import pathlib

#Pide la carpeta donde se buscara los archivos similares
directorio = pathlib.Path(input("Introduce la carpeta: "))

print("Explorando carpeta....")

lista = []

for item in directorio.rglob("*"):
    if item.is_dir():
        print(f"Carpeta: {item}")
    elif item.is_file():
        #print(f"Archivo: {item}")
        lista.append(item)
        print(f"esta en la lista{item}")

