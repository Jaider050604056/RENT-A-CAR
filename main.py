import os; os.system("cls"); print("*"*60); print("")
import datetime
from rent_a_car import menu

if __name__ == "__main__":
    plazo_dias = [1, 5]
    rango_dinero = [40, 140]
    clientes = {}
    temporal = []
    dia = -1
    contador_cliente = 1
    vehiculos = {
        "Toyota" : [
            ["Corolla", 50, "Disponible"],
            ["Camry", 60, "Disponible"],
            ["RAV4", 80, "Disponible"],
            ["Highlander", 120, "Disponible"]
        ],
        "Nissan" : [
            ["Sentra", 40, "Disponible"],
            ["Altima", 60, "Disponible"],
            ["Rogue", 80, "Disponible"]
        ]
    }
    while True:
        dia = dia + 1
        fecha = datetime.timedelta(days=dia) + datetime.date.today()
        menu(vehiculos,clientes,plazo_dias,rango_dinero,fecha,contador_cliente)
        lista_clientes = list(clientes.keys())
        for i in range(len(lista_clientes)):
            clientes[lista_clientes[i]]["Días"] -= 1
            if clientes[lista_clientes[i]]["Días"] == 0:
                os.system("cls"); print("*"*60); print("")
                print(f"Fecha de hoy: {fecha}"); print("")
                print(f"El plazo de {lista_clientes[i]} ha terminado")
                print("El vehiculo", clientes[lista_clientes[i]]["Marca"], "-", clientes[lista_clientes[i]]["Modelo"], "se ha marcado como Disponible")
                temporal.append(lista_clientes[i])
                vehiculos[clientes[lista_clientes[i]]["Marca"]] [clientes[lista_clientes[i]]["IndexModelo"]] [2] = "Disponible"
                print(""); input("Pulsa enter para continuar ")
        if temporal:
            for i in range(len(temporal)):
                del clientes[temporal[i]]
            temporal.clear()
        os.system("cls"); print("*"*60); print("")