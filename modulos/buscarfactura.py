import json
def buscarfactura(identificador):
    with open(f"blobs/facturas/{identificador}.json","r", encoding = "utf-8") as archivo:
       archivo = json.load(archivo)
    print(archivo)

