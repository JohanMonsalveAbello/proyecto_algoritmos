import json
def buscarfactura(identificador):
    with open(f"restaurante_proyecto/blobs/facturas/{identificador}.json","r", encoding = "utf-8") as archivo:
       archivo = json.load(archivo)
    print(archivo)

