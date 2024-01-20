import bancos_de_sangre as mod

def mostrar_banco(banco: dict)-> None:
    """ Muestra en pantalla la informacion de un banco
    Parametros:
        banco (dict): El banco de sangre del que se van a mostrar los detalles.
    """
    nombre = banco["nombre"]
    localidad = banco["localidad"]
    donantes = banco["donantes"]
    a_positivo = banco["A+"]
    a_negativo = banco["A-"]
    b_positivo = banco["B+"]
    b_negativo = banco["B-"]
    ab_positivo = banco["AB+"]
    ab_negativo = banco["AB-"]
    o_positivo = banco["O+"]
    o_negativo = banco["O-"]

    cantidades1 = "A+:  {:3d}\t\tA-:  {:3d}\t\tB+: {:3d}\t\tB-: {:3d}"
    cantidades2 = "AB+: {:3d}\t\tAB-: {:3d}\t\tO+: {:3d}\t\tO-: {:3d}"

    print("Nombre: " + nombre + " - Localidad: " + localidad + " - Donantes: " + str(donantes) )
    print("Bolsas Disponibles:")
    print(cantidades1.format(a_positivo, a_negativo, b_positivo, b_negativo))
    print(cantidades2.format(ab_positivo, ab_negativo, o_positivo, o_negativo))



def ejecutar_recibir_donacion(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de recibir una donacion para uno de los bancos de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """
    nombre_banco = input("Ingrese el nombre del banco de sangre que recibira al donante: ")

    banco_donante = mod.buscar_banco(nombre_banco, b1, b2, b3, b4)
    if banco_donante is None:
        print("No se encontro el banco " + nombre_banco + " en los registros.")
    else:
        genero =input('Ingrese el genero: ')
        edad = int(input('Ingrese la edad: '))
        peso = int(input(' Ingrese el peso: '))
        tipo = input('Ingrese el tipo de sangre: ')
        donacion = mod.recibir_donacion(genero, edad, peso, tipo, banco_donante)
        print('Puede donar ' + str(donacion) + ' bolsas')
       
        
    # TODO: Completar


def ejecutar_suministrar_bolsas(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de suministrar bolsas desde un banco de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """

    nombre_banco = input("Ingrese el nombre del banco de sangre que suministrara las bolsas: ")

    banco_suministro = mod.buscar_banco(nombre_banco, b1, b2, b3, b4)
    if banco_suministro is None:
        print("No se encontro el banco " + nombre_banco + " en los registros.")
    else:
        tipo =input('Ingrese el tipo de sangre: ')
        cantidad = int(input('Ingrese la cantidad de bolsas: '))
        donacion = mod.suministrar_bolsas(tipo, cantidad, banco_suministro)
    if donacion == True:
        print('Se pueden suministrar bolsas ' + tipo)
    else:
        print('No se pueden suministrar bolsas ' + tipo)



def ejecutar_transferir_bolsas(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de transferir bolsas entre dos bancos de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """
    nombre_banco1 = input("Ingrese el nombre del banco de sangre origen: ")
    nombre_banco2 = input("Ingrese el nombre del banco de sangre destino: ")

    banco1 = mod.buscar_banco(nombre_banco1, b1, b2, b3, b4)
    banco2 = mod.buscar_banco(nombre_banco2, b1, b2, b3, b4)
    if banco1 is None:
        print("No se encontro el banco origen " + nombre_banco1 + " en los registros.")
    elif banco2 is None:
        print("No se encontro el banco destino " + nombre_banco2 + " en los registros.")
    else:
        tipo= input('Ingrese el tipo de sangre: ')
        cantidad = int(input('Ingrese la cantidad de bolsas: '))
        transferir = mod.transferir_bolsas(tipo, cantidad, banco1, banco2)
        print('Quedan '+ str(transferir) + " bolsas en el banco "+ nombre_banco1)


def ejecutar_buscar_por_localidad(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """ Ejecuta la opcion de buscar por localidad.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """
    print("Buscando por localidad")
    cadena = input("Por favor indique la cadena para buscar por localidad: ")
    buscar_por_localidad = mod.buscar_por_localidad(b1, b2, b3, b4, cadena)
    print('En la localidad de '+ cadena + ' estan los siguientes bancos: ' + buscar_por_localidad)
  


def ejecutar_banco_con_mas_bolsas_de_un_tipo(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de encontrar el banco con mas bolsas de un tipo de sangre
       en especifico.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """

    tipo = input("Ingrese el tipo de sangre a consultar (A+, A-, B+, B-, AB+, AB-, O+, O-): ")
    mas_bolsas = mod.banco_con_mas_bolsas_de_un_tipo(b1, b2, b3, b4,tipo)
    print('El banco con mas bolsas del tipo ' + tipo + ' es ' + mas_bolsas['nombre'])


def ejecutar_disponibilidad_por_tipo(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de consultar la disponibilidad de bolsas de un tipo
       de sangre en especifico.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """

    tipo = input("Ingrese el tipo de sangre a consultar (A+, A-, B+, B-, AB+, AB-, O+, O-): ")
    disponibilidad_por_tipo =mod.disponibilidad_por_tipo(b1, b2, b3, b4, tipo)
    print('Hay '+ str(disponibilidad_por_tipo) + ' bolsas ' + tipo)


def ejecutar_tipo_mas_escaso(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de encontrar el tipo de sangere mas escaso sumando
       todos los bancos.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    """
    tipo_mas_escaso = mod.tipo_mas_escaso(b1, b2, b3, b4)
    print('El tipo mas escaso de sangre es ' + tipo_mas_escaso)



def ejecutar_hay_tipo_en_riesgo(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """ Ejecuta la opcion de encontrar si hay algun tipo de sangre en riesgo.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4
    """

    riesgo = int(input("Ingrese el valor minimo para que un tipo sea considerado en riesgo: "))
    tipo_en_riesgo= mod.hay_tipo_en_riesgo(b1, b2, b3, b4, riesgo)
    if tipo_en_riesgo == True:
        print('Si esta en riesgo')
    else:
        print('No esta en riesgo')


def ejecutar_promedio_donantes(b1: dict, b2: dict, b3: dict, b4: dict)->None:
    """Ejecuta la opcion de consultar la cantidad promedio de donantes por
       banco de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4
    """
    promedio_donantes = mod.promedio_donantes(b1, b2, b3, b4)
    print('El promedio de donantes es '+ str(promedio_donantes))


def iniciar_aplicacion():
    """Inicia la ejecucion de la aplicacion por consola.
    Esta funcion primero crea los cuatro bancos de sangre.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    banco1 = mod.crear_banco("Techo", "Kennedy", 0, 48, 42, 36, 13, 31, 50, 43, 42)
    banco2 = mod.crear_banco("Shaio", "Suba", 0, 20, 23, 21, 28, 32, 7, 36, 5)
    banco3 = mod.crear_banco("Bachue", "Engativa", 0, 23, 42, 45, 15, 50, 34, 20, 26)
    banco4 = mod.crear_banco("Cardioinfantil", "Usaquen",  0, 7, 20, 16, 37, 7, 43, 25, 10)

    ejecutando = True
    while ejecutando:
        print("\n\nEstado de los bancos" + ("-"*50))
        print("Banco de Sangre 1")
        mostrar_banco(banco1)
        print("-"*50)

        print("Banco de Sangre 2")
        mostrar_banco(banco2)
        print("-"*50)

        print("Banco de Sangre 3")
        mostrar_banco(banco3)
        print("-"*50)

        print("Banco de Sangre 4")
        mostrar_banco(banco4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(banco1, banco2, banco3, banco4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(b1: dict, b2: dict, b3: dict, b4:dict) -> bool:
    """Le muestra al usuario las opciones de ejecucion disponibles.
    Parametros:
        b1 (dict): Diccionario que contiene la informacion del banco 1.
        b2 (dict): Diccionario que contiene la informacion del banco 2.
        b3 (dict): Diccionario que contiene la informacion del banco 3.
        b4 (dict): Diccionario que contiene la informacion del banco 4.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opcion para salir
        de la aplicacion.

    """
    print("Menu de opciones")
    print(" 1 - Recibir donacion")
    print(" 2 - Suministrar bolsas")
    print(" 3 - Transferir bolsas")
    print(" 4 - Buscar por localidad")
    print(" 5 - Consultar banco con mas bolsas de un tipo")
    print(" 6 - Consultar disponibilidad por tipo")
    print(" 7 - Consultar tipo de sangre mas escaso")
    print(" 8 - Consultar tipo de sangre en riesgo")
    print(" 9 - Consultar promedio de donantes")
    print(" 10 - Salir de la aplicacion.")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_recibir_donacion(b1, b2, b3, b4)
    elif opcion_elegida == "2":
        ejecutar_suministrar_bolsas(b1, b2, b3, b4)
    elif opcion_elegida == "3":
        ejecutar_transferir_bolsas(b1, b2, b3, b4)
    elif opcion_elegida == "4":
        ejecutar_buscar_por_localidad(b1, b2, b3, b4)
    elif opcion_elegida == "5":
        ejecutar_banco_con_mas_bolsas_de_un_tipo(b1, b2, b3, b4)
    elif opcion_elegida == "6":
        ejecutar_disponibilidad_por_tipo(b1, b2, b3, b4)
    elif opcion_elegida == "7":
        ejecutar_tipo_mas_escaso(b1, b2, b3, b4)
    elif opcion_elegida == "8":
        ejecutar_hay_tipo_en_riesgo(b1, b2, b3, b4)
    elif opcion_elegida == "9":
        ejecutar_promedio_donantes(b1, b2, b3, b4)
    elif opcion_elegida == "10":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    return continuar_ejecutando


iniciar_aplicacion()
