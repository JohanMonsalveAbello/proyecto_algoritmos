import json
from modulos.pedido import*
from modulos.buscarfactura import*
def menu():
    while True:
        print("Bienvenido")
        print("Dijite 1 para mostrar los plastos del dia")
        print("Dijite 2 para realizar pedido")
        print("Dijite 3 para consultar factura")
        print("Dijite 4 para salir")
        decision = int(input())


        if decision == 1:
            with open("blobs\platos\platos.json", "r", encoding = "utf-8" ) as documento:
                menu_casa = json.load(documento)
            for clave,producto in menu_casa.items():
                print(f"{clave}.  {producto['Nombre']} {producto['Precio']}")
        if decision == 2:
            eleccion = input("dijite el numero del plato de su preferencia")
            pedido(eleccion)
            break
        if decision == 3:
           buscar = input("Dijite el identificador de la factura")
           buscarfactura(buscar)
        if decision == 4:
            break