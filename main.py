import os; os.system("cls"); print("*"*60); print("")
from rent_a_car import menu

if __name__ == "__main__":
    plazodias = [1, 10]
    rangodinero = [40, 140]
    clientes = {}
    temporaL = []
    dia = 1
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
        menu(vehiculos,clientes,dia,plazodias,rangodinero)
        dia = dia + 1
        lista_clientes = list(clientes.keys())
        for i in range(len(lista_clientes)):
            clientes[lista_clientes[i]]["Días"] -= 1
            if clientes[lista_clientes[i]]["Días"] == 0:
                os.system("cls"); print("*"*60); print("")
                print(f"Día #{dia}"); print("")
                print(f"El plazo de {lista_clientes[i]} ha terminado")
                print("El vehiculo", clientes[lista_clientes[i]]["Marca"], "-", clientes[lista_clientes[i]]["Modelo"], "se ha marcado como Disponible")
                temporaL.append(lista_clientes[i])
                vehiculos[clientes[lista_clientes[i]]["Marca"]] [clientes[lista_clientes[i]]["IndexModelo"]] [2] = "Disponible"
                print(""); input("Pulsa enter para continuar ")
        if temporaL:
            for i in range(len(temporaL)):
                del clientes[temporaL[i]]
            temporaL.clear()
        os.system("cls"); print("*"*60); print("")