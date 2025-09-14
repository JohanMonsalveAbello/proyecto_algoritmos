from datetime import datetime
import json

platos_elegidos = []
pedido_cliente = {}
nombre = ""
total = 0

ahora = datetime.now()
fecha_hora = str(ahora.strftime("%Y-%m-%d %H %M %S"))


def cantidad(eleccion,precio):
    ops2 = int(input("Digite la cantidad de platos similares que desea: "))
    while ops2 <= 0:
        ops2 = int(input("Cantidad inválida, debe ser mayor a 0. Digite nuevamente: "))

    for _ in range(ops2):  
        global total
        platos_elegidos.append(eleccion)
        total += precio

    print(platos_elegidos)
def facturacion(ops, eleccion,precio):
    global nombre  
    
    if ops == 1:
        cantidad(eleccion,precio)
        if nombre == "":
            nombre = input("Digite su nombre: ")
        pedido_cliente[nombre] = f"fecha de emicion de la factura {fecha_hora}",platos_elegidos,f"total = {total},identificador = {nombre}_{fecha_hora} "


        


def pedido(opcion):
    with open("blobs/platos/platos.json", "r", encoding="utf-8") as archivo:
        data = json.load(archivo)

    while True:
        for clave, plato in data.items():
            if clave == opcion:
                print(f"El plato que escogió es {clave}. {plato['Nombre']} - {plato['Precio']}")
                eleccion = f"{clave}. {plato['Nombre']} - {plato['Precio']}"
                precio = int(plato["Precio"])
                ops = int(input("¿Su opción es correcta? (1 = sí, 2 = no): "))
                while ops != 1 and ops != 2:
                    try:
                        ops = int(input("Ingrese una opción válida (1 = sí, 2 = no): "))
                    except ValueError:
                        print(" Solo se permiten números.")

                facturacion(ops, eleccion,precio)

                eleccionagregar = int(input("¿Desea agregar más platos? (1 = sí, 2 = no): "))
                while eleccionagregar != 1 and eleccionagregar != 2:
                    try:
                        eleccionagregar = int(input("Ingrese una opción válida (1 = sí, 2 = no): "))
                    except ValueError:
                        print(" Solo se permiten números.")

                if eleccionagregar == 1:
                    opcion = input("Digite su opción: ")
                elif eleccionagregar == 2:
                    print(" Pedido finalizado")
                    with open(f"blobs/facturas/{nombre}_{fecha_hora}.json", "w", encoding="utf-8") as archivo:
                        json.dump(pedido_cliente, archivo, indent=4,)
                    with open(f"blobs/facturas/{nombre}_{fecha_hora}.json", "r", encoding="utf-8") as archivo:
                        mostrar = json.load(archivo)
                        for clave,valor in mostrar.items():
                            print(clave,valor)
                  
                    return




