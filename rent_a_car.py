import os, random

def menu(vehiculos,clientes,dia,plazodias,rangodinero):
    print("Bienvenido a RENT-A-CAR"); print("")
    print(f"Día #{dia}"); print("")
    print("1. Atender clientes")
    print("2. Añadir vehiculo al catalogo")
    print("3. Eliminar vehiculo del catalogo")
    print("4. Cambiar precios minimo/maximo del RENT-A-CAR")
    print("5. Cambiar plazo minimo/maximo de días")
    print("6. Pasar al siguiente día")
    print("7. Ver clientes en alquiler")
    print("8. Cerrar negocio"); print("")
    opcion=int(input("Escribe un numero para continuar: "))
    if opcion == 1:
        os.system("cls"); print("*"*60); print("")
        cliente(vehiculos,clientes,plazodias,rangodinero,dia)
    elif opcion == 2:
        os.system("cls"); print("*"*60); print("")
        print("Añadir vehiculo al catalogo"); print("")
        marca = input("Escribe la marca del vehiculo que deseas agregar: ")
        cantidad_modelo = int(input("Cuantos modelos deseas agregar?: "))
        print(""); print("-"*60); print("")
        if not isinstance(marca, int):
            vehiculos[marca] = []
            for i in range(cantidad_modelo):
                modelo = input(f"Escribe el modelo #{i+1} del vehiculo que deseas agregar: ")
                precio = int(input("Escribe el precio del vehiculo (de el 40$ al 140$): "))
                vehiculos[marca].append([modelo, precio, "Disponible"])
                print("")
            os.system("cls")
            print("Vehiculo(s) añadidos al catalogo"); print("")
            marcas = list(vehiculos.keys())
            contador = 0
            for i in range(len(marcas)):
                print(" "*15,f"{i+1}).","Marca:",marcas[i]); print("-"*60)
                print("{:<20}{:<20}{:<20}".format("Modelo", "Precio por día", "Disponibilidad"))
                print("-"*60)
                for j in range(len(vehiculos[marcas[i]])):
                    contador = contador + 1
                    print("{:<20}${:<19}{:<20}".format(*vehiculos[marcas[i]][j]))
                print("-"*60)
            print(""); input("Pulsa enter para continuar ")
            os.system("cls")
            menu(vehiculos,clientes,dia,plazodias,rangodinero)
        else: 
            os.system("cls")
            print("Erorr, intentalo de nuevo"); print("")
            menu(vehiculos,clientes,dia,plazodias,rangodinero)
    elif opcion == 3:
        os.system("cls"); print("*"*60); print("")
        print("Eliminar vehiculo del catalogo"); print("")
        print("1. Eliminar marca con sus respectivos modelos")
        print("2. Eliminar solo modelos"); print("")
        opcion=int(input("Escribe un numero para continuar: "))
        marcas = list(vehiculos.keys())
        if opcion == 1:
            os.system("cls")
            contador = 0
            for i in range(len(marcas)):
                print(" "*15,f"{i+1}).","Marca:",marcas[i]); print("-"*60)
                print("{:<20}{:<20}{:<20}".format("Modelo", "Precio por día", "Disponibilidad"))
                print("-"*60)
                for j in range(len(vehiculos[marcas[i]])):
                    contador = contador + 1
                    print("{:<20}${:<19}{:<20}".format(*vehiculos[marcas[i]][j]))
                print("-"*60); print("")
            marca = input("Escribe la marca del modelo que deseas eliminar: ")
            if not isinstance(marca, int):
                del vehiculos[marca]
                os.system("cls")
                print("Vehiculo(s) eliminado(s) del catalogo"); print("")
                marcas = list(vehiculos.keys())
                contador = 0
                for i in range(len(marcas)):
                    print(" "*15,f"{i+1}).","Marca:",marcas[i]); print("-"*60)
                    print("{:<20}{:<20}{:<20}".format("Modelo", "Precio por día", "Disponibilidad"))
                    print("-"*60)
                    for j in range(len(vehiculos[marcas[i]])):
                        contador = contador + 1
                        print("{:<20}${:<19}{:<20}".format(*vehiculos[marcas[i]][j]))
                    print("-"*60)
                print(""); input("Pulsa enter para continuar ")
                os.system("cls")
                menu(vehiculos,clientes,dia,plazodias,rangodinero)
            else: 
                os.system("cls")
                print("Erorr, intentalo de nuevo"); print("")
                menu(vehiculos,clientes,dia,plazodias,rangodinero)
        elif opcion == 2: 
            os.system("cls")
            contador = 0
            for i in range(len(marcas)):
                print(" "*15,f"{i+1}).","Marca:",marcas[i]); print("-"*60)
                print("{:<20}{:<20}{:<20}".format("Modelo", "Precio por día", "Disponibilidad"))
                print("-"*60)
                for j in range(len(vehiculos[marcas[i]])):
                    contador = contador + 1
                    print("{:<5}{:<15}${:<19}{:<20}".format(f"{contador}). ",*vehiculos[marcas[i]][j]))
                print("-"*60); print("")
            index_marcas = int(input("Escribe el numero de la marca del modelo que deseas eliminar: "))
            cantidad_modelo = int(input("Cuantos modelos deseas eliminar?: "))
            for h in range(cantidad_modelo):
                os.system("cls"); print("-"*60)
                marcas = list(vehiculos.keys())
                contador = 0
                for i in range(1):
                    print(" "*19,"Marca:",marcas[index_marcas-1]); print("-"*60)
                    print("{:<20}{:<20}{:<25}".format("Modelo", "Precio por día", "Disponibilidad"))
                    print("-"*60)
                    for j in range(len(vehiculos[marcas[index_marcas-1]])):
                        contador = contador + 1
                        print("{:<5}{:<15}${:<19}{:<20}".format(f"{contador}). ",*vehiculos[marcas[index_marcas-1]][j]))
                    print("-"*60)
                print("")
                modelos = int(input(f"Escribe el numero del {h+1}° modelo que desea eliminar: "))
                vehiculos[marcas[index_marcas-1]].pop(modelos-1)
                print("")
            os.system("cls")
            print("Vehiculo(s) eliminado(s) del catalogo"); print("")
            marcas = list(vehiculos.keys())
            contador = 0
            for i in range(len(marcas)):
                print(" "*15,f"{i+1}).","Marca:",marcas[i]); print("-"*60)
                print("{:<20}{:<20}{:<20}".format("Modelo", "Precio por día", "Disponibilidad"))
                print("-"*60)
                for j in range(len(vehiculos[marcas[i]])):
                    contador = contador + 1
                    print("{:<5}{:<15}${:<19}{:<20}".format(f"{contador}). ",*vehiculos[marcas[i]][j]))
                print("-"*60)
            print(""); input("Pulsa enter para continuar ")
            os.system("cls")
            menu(vehiculos,clientes,dia,plazodias,rangodinero)
        else: 
            os.system("cls")
            print("Erorr, intentalo de nuevo"); print("")
            menu(vehiculos,clientes,dia,plazodias,rangodinero)
    elif opcion == 4:
        os.system("cls"); print("*"*60); print("")
        print("Cambiar precios minimo/maximo del RENT-A-CAR"); print("")
        print(f"Precio minimo del RENT-A-CAR: {rangodinero[0]}$")
        print(f"Precio maximo del RENT-A-CAR: {rangodinero[1]}$"); print("")
        minimo=int(input("Escribe el nuevo precio minimo: "))
        maximo=int(input("Escribe el nuevo precio maximo: "))
        rangodinero.clear()
        rangodinero.append(minimo)
        rangodinero.append(maximo)
        os.system("cls")
        print("Los precios fueron modificados con exito"); print("")
        print(f"Precio minimo del RENT-A-CAR: {rangodinero[0]}$")
        print(f"Precio maximo del RENT-A-CAR: {rangodinero[1]}$")
        print(""); input("Pulsa enter para continuar ")
        os.system("cls")
        menu(vehiculos,clientes,dia,plazodias,rangodinero)
    elif opcion == 5:
        os.system("cls"); print("*"*60); print("")
        print("Cambiar plazo minimo/maximo de días"); print("")
        print(f"El día minimo para alquilar en el RENT-A-CAR es: {plazodias[0]}")
        print(f"El día maximo para alquilar en el RENT-A-CAR es: {plazodias[1]}"); print("")
        minimo=int(input("Escribe el nuevo día minimo para alquilar: "))
        maximo=int(input("Escribe el nuevo día maximo para alquilar: "))
        plazodias.clear()
        plazodias.append(minimo)
        plazodias.append(maximo)
        os.system("cls")
        print("Los plazos fueron modificados con exito"); print("")
        print(f"El día minimo para alquilar en el RENT-A-CAR es: {plazodias[0]}")
        print(f"El día maximo para alquilar en el RENT-A-CAR es: {plazodias[1]}")
        print(""); input("Pulsa enter para continuar ")
        os.system("cls")
        menu(vehiculos,clientes,dia,plazodias,rangodinero)
    elif opcion == 6:
        pass
    elif opcion == 7:
        os.system("cls")
        dias_clientes = list(clientes.keys())
        if dias_clientes:
            for i in range(len(dias_clientes)):
                print(dias_clientes[i]); print("")
                print("Posee el vehiculo:", clientes[dias_clientes[i]] ["Marca"], "-", clientes[dias_clientes[i]] ["Modelo"])
                print("Terminará su plazo en", clientes[dias_clientes[i]] ["Días"], "día(s)"); print("")
        else:
            print("No hay ningún cliente en alquiler")
        print(""); input("Pulsa enter para continuar ")
        os.system("cls")
        menu(vehiculos,clientes,dia,plazodias,rangodinero)
    elif opcion == 8:
        os.system("cls")
        print("Adios"); print("")
        exit()
    else:
        os.system("cls")
        print("Erorr, intentalo de nuevo"); print("")
        menu(vehiculos,clientes,dia,plazodias,rangodinero)
    return

def cliente(vehiculos,clientes,plazodias,rangodinero,dia):
    vacio = all(modelo[2] == "No disponible" for modelos in vehiculos.values() for modelo in modelos)
    dias = random.randint(plazodias[0],plazodias[1])
    dinero = dias*(random.randint(rangodinero[0], rangodinero[1]))
    os.system("cls"); print("*"*60); print("")
    if vacio:
        print("Ningún vehiculo se encuentra disponible")
        print("Espere unos días o añade más vehiculos para atender a más clientes")
        print(""); input("Pulsa enter para continuar ")
        os.system("cls"); print("*"*60); print("")
        menu(vehiculos,clientes,dia,plazodias,rangodinero)
    minimo = min(marca[1] for i in vehiculos.values() for marca in i if marca[2] == "Disponible")
    if (round(dinero/dias)) < minimo:
        cliente(vehiculos,clientes,plazodias,rangodinero,dia)
    else:
        print("-"*12,"Un cliente desea alquilar un coche","-"*12); print("")
        print(f"El cliente posee {dinero}$ en efectivo")
        print(f"Dinero dividido en días: {round(dinero/dias)}$")
        print("Cantidad de días deseados:", dias); print("")
        print("-"*6,"Elije un coche que se ajuste a sus comodidades","-"*6); print("")
        clientes[f"Cliente del día #{dia}"] = {"Días" : dias, "Dinero total" : dinero, "Dinero por días" : round(dinero/dias)}
        listadovehiculos(vehiculos,clientes,plazodias,rangodinero,dia)
    return

def listadovehiculos(vehiculos,clientes,plazodias,rangodinero,dia):
    marcas = list(vehiculos.keys())
    contador = 0
    for i in range(len(marcas)):
        print(" "*15,f"{i+1}).","Marca:",marcas[i]); print("-"*60)
        print("{:<20}{:<20}{:<20}".format("Modelo", "Precio por día", "Disponibilidad"))
        print("-"*60)
        for j in range(len(vehiculos[marcas[i]])):
            contador = contador + 1
            print("{:<20}${:<19}{:<20}".format(*vehiculos[marcas[i]][j]))
        print("-"*60)
    print("")
    index_marcas = int(input("Escribe el número de la marca para seleccionar el coche adecuado: ")); print("")
    os.system("cls"); print("-"*60)
    contador = 0
    for i in range(1):
        print(" "*19,"Marca:",marcas[index_marcas-1]); print("-"*60)
        print("{:<20}{:<20}{:<25}".format("Modelo", "Precio por día", "Disponibilidad"))
        print("-"*60)
        for j in range(len(vehiculos[marcas[index_marcas-1]])):
            contador = contador + 1
            print("{:<5}{:<15}${:<19}{:<20}".format(f"{contador}). ",*vehiculos[marcas[index_marcas-1]][j]))
        print("-"*60)
    print("")
    index_modelos = int(input("Escribe un número del modelo para seleccionar el coche adecuado: "))
    os.system("cls"); print("*"*60); print("")
    if (vehiculos[marcas[index_marcas-1]][index_modelos-1][2]) == "Disponible" and (vehiculos[marcas[index_marcas-1]][index_modelos-1][1]) <= clientes[f"Cliente del día #{dia}"] ["Dinero por días"]:
        print("-"*25,"Factura","-"*26); print("")
        print(f"Cliente del día #{dia}"); print("")
        print("Vehiculo alquilado:", marcas[index_marcas-1], "-", vehiculos[marcas[index_marcas-1]][index_modelos-1][0])
        print(f"Coste por día: {vehiculos[marcas[index_marcas-1]][index_modelos-1][1]}$")
        print("Días de alquiler:",clientes[f"Cliente del día #{dia}"]["Días"]); print("")
        print("Dinero recibido:", clientes[f"Cliente del día #{dia}"]["Dinero total"],"$")
        print("Dinero entregado:",clientes[f"Cliente del día #{dia}"]["Dinero total"] - (clientes[f"Cliente del día #{dia}"]["Días"] * vehiculos[marcas[index_marcas-1]][index_modelos-1][1]),"$"); print("")
        print("Dinero total:", clientes[f"Cliente del día #{dia}"]["Días"] * vehiculos[marcas[index_marcas-1]][index_modelos-1][1],"$")
        del clientes[f"Cliente del día #{dia}"] ["Dinero por días"]
        clientes[f"Cliente del día #{dia}"].update({"Marca" : marcas[index_marcas-1], "Modelo" : vehiculos[marcas[index_marcas-1]][index_modelos-1][0], "IndexModelo" : index_modelos-1})
        vehiculos[marcas[index_marcas-1]] [index_modelos-1][2] = "No disponible"
        print(""); print("El vehiculo",marcas[index_marcas-1], "-", vehiculos[marcas[index_marcas-1]][index_modelos-1][0], "se marcó como No disponible")
        print(""); input("Pulsa enter para continuar ") 
    else: 
        os.system("cls"); print("*"*60); print("")
        print("Vehiculo no disponible o fuera de precio, intentalo de nuevo")
        print(""); input("Pulsa enter para continuar ")
        del clientes[f"Cliente del día #{dia}"]
        cliente(vehiculos,clientes,plazodias,rangodinero,dia)
    return
