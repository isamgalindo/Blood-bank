def crear_banco(nombre:str, loc:str, cant_donantes:int, a_positivo:int, a_negativo:int,
                b_positivo:int, b_negativo:int, ab_positivo:int, ab_negativo:int,
                o_positivo:int, o_negativo:int)->dict:
    banco = {"nombre": nombre, "localidad" :loc, "donantes":cant_donantes, "A+":a_positivo, "A-":a_negativo, "B+":b_positivo,"B-":b_negativo,"AB+":ab_positivo,"AB-":ab_negativo,"O+":o_positivo,"O-":o_negativo}
    return banco

    """Crea un diccionario que representa un nuevo banco con todos sus atributos
       inicializados.
    Parametros:
        nombre (str): Nombre del banco.
        loc (str): Nombre de la localidad donde se encuentra el banco.
        cant_donantes (int): Numero de donantes que ha tenido el banco.
        a_positivo (int): Cantidad de bolsas disponibles de tipo A positivo.
        a_negativo (int): Cantidad de bolsas disponibles de tipo A negativo.
        b_positivo (int): Cantidad de bolsas disponibles de tipo B positivo.
        b_negativo (int): Cantidad de bolsas disponibles de tipo B negativo.
        ab_positivo (int): Cantidad de bolsas disponibles de tipo AB positivo.
        ab_negativo (int): Cantidad de bolsas disponibles de tipo AB negativo.
        o_positivo (int): Cantidad de bolsas disponibles de tipo O positivo.
        o_negativo (int): Cantidad de bolsas disponibles de tipo O negativo.
     Retorna:
        dict: Diccionario con los datos del banco.
    """


def buscar_banco(nombre_banco:str, b1:dict, b2:dict, b3:dict, b4:dict)->dict:
    banco= ""
    
    if b1['nombre']== nombre_banco:
        banco = b1
    if b2 ['nombre']== nombre_banco:
        banco = b2
    if b3 ['nombre']== nombre_banco:
        banco = b3
    if b4 ['nombre']== nombre_banco:
        banco = b4
    return banco
    
    """Busca en cual de los 4 diccionarios que se pasan por parametro esta
       el banco de sangre cuyo nombre es dado por parametro.
       Si no se encuentra el banco se debe retornar None.
    Parametros:
        nombre_banco (str): El nombre del banco que se desea buscar.
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    Retorna:
        dict: Diccionario del banco cuyo nombre fue dado por parametro.
        None si no se encuentra.
    """


def validar_donante(genero:str, edad:int, peso:int)->int:
    """Valida los datos del donante y calcula la cantidad de bolsas que este
       debe donar segun sus datos personales.
    Parametros:
        genero (str): Genero del donante, puede ser "M" o "F".
        edad (int): Edad del donante en años.
        peso (int): Peso del donante en kilogramos, como un número entero.
    Retorna:
        int: El numero de bolsas que el donante debe donar. Si la persona no
        es apta para donar por incumplir alguna de las reglas, se retorna 0.
    """
    cantidad_de_bolsas_que_se_pueden_donar = 0
    if edad >= 18 and edad <=65:
        if genero == "M":
            if peso < 80 and peso > 50:
               cantidad_de_bolsas_que_se_pueden_donar +=1
            elif peso >= 80 and peso < 120:
                cantidad_de_bolsas_que_se_pueden_donar +=2
            elif peso >120:
                cantidad_de_bolsas_que_se_pueden_donar +=3 
        
        if  genero == "F":
            if peso < 75 and peso > 50:
               cantidad_de_bolsas_que_se_pueden_donar +=1
            elif peso >= 75: 
               cantidad_de_bolsas_que_se_pueden_donar +=2
    return cantidad_de_bolsas_que_se_pueden_donar



def recibir_donacion(genero:str, edad:int, peso:int, tipo:str, banco:dict)->int:
    
    final =  0
    donante = validar_donante(genero, edad, peso)
    if tipo == 'O+' or tipo == 'A+':
        if donante == 0:
            final = 0
        if donante>=1:
            final = 1
    else:
        final = donante
    
    banco[tipo]+= final
    return final
    


def suministrar_bolsas(tipo:str,cantidad:int,banco:dict)->bool:
    resta = banco[tipo]-cantidad
    if resta< 5:
        resultado = False
    if resta >=5:
        resultado = True
        
    if resultado ==True:
        banco[tipo] = resta
    
    return resultado
    
    """Registra un suministro de bolsas de sangre a un hospital segun las reglas
       descritas en el enunciado. Esta funcion es responsable de verificar previamente
       que el suministro sea viable.
    Parametros:
        tipo (str): Tipo de sangre que se necesita. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
        cantidad (int): Cantidad de bolsas que se desean suministrar.
        banco (banco): Banco de sangre que suministrara las bolsas.
    Retorna:
        bool: True si el suministro pudo ser realizado. False de lo contrario.
    """


def transferir_bolsas(tipo:str,cantidad:int,banco1:dict,banco2:dict)->int:
    resta = banco1[tipo]-cantidad
    si_puede = suministrar_bolsas(tipo,cantidad,banco1)
    if si_puede == True:
        banco2[tipo]+= resta
    else:
        resta = 0
        
    return resta

        

    """Registra una transferencia de bolsas de sangre entre bancos segun las reglas
       descritas en el enunciado. Esta funcion es responsable de verificar previamente
       que la transferencia sea viable.
    Parametros:
        tipo (str): Tipo de sangre que se necesita. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
        cantidad (int): Cantidad de bolsas que se desean transferir.
        banco1 (banco): Banco de sangre origen.
        banco2 (banco): Banco de sangre destino.
    Retorna:
        int: Numero de bolsas efectivamente transferidas. 0 en caso de que no se haya
        podido realizar la transferencia.
    """



def buscar_por_localidad(b1:dict, b2:dict, b3:dict, b4:dict, cadena: str)->str:
    busqueda =""
    if cadena == b1["localidad"]:
       if busqueda == "":
          busqueda= b1["nombre"]      
    elif cadena == b2["localidad"]:
        if busqueda == "":
          busqueda= b2["nombre"]
        else:
          busqueda += ","+ b2["nombre"]
    elif cadena ==b3["localidad"]:
        if busqueda == "":
          busqueda = b3["nombre"]
        else:
          busqueda += ","+ b3["nombre"]
    elif cadena ==b4["localidad"]:
        if busqueda == "":
          busqueda = b4["nombre"]
        else:
          busqueda += ","+ b4["nombre"]
    return busqueda
        
        
    """Busca entre los bancos de sangre cuales tienen en su localidad la cadena recibida
       por parametro. La busqueda no tiene en cuenta mayusculas o minusculas.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        cadena (str): La cadena usada para la busqueda.
    Retorna:
        str: Una cadena con el nombre del banco que contiene la cadena parámetro
        en su localidad. Si hay mas de un banco, entonces se retornan los
        nombres de todos los bancos relevantes separados por comas. Si ningún banco
        tiene la cadena entonces retorna una cadena vacía.
    """


def banco_con_mas_bolsas_de_un_tipo(b1:dict, b2:dict, b3:dict, b4:dict,tipo:str)->dict:
    mayor = b1
    if b2[tipo]>= mayor[tipo]:
        mayor = b2
    if b3[tipo]>= mayor[tipo]:
        mayor = b3
    if b4[tipo]>= mayor[tipo]:
        mayor = b4
        
    return mayor
    
    """Busca el banco de sangre que tiene la mayor cantidad de bolsas del tipo recibido
    
       por parametro.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        tipo (str): Tipo de sangre a buscar. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
    Retorna:
        dict: El diccionario del banco con mayor disponibilidad de bolsas del tipo
        recibido por parametro.
    """


def disponibilidad_por_tipo(b1:dict, b2:dict, b3:dict, b4:dict, tipo:str)->int:
    suma = b1[tipo] + b2[tipo] + b3[tipo] + b4[tipo]
    return suma 
    
    """Calcula la cantidad de bolsas de sangre disponibles en todos los bancos
       de un tipo de sangre en especifico.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        tipo (str): Tipo de sangre a consultar. Corresponde a uno de los tipos válidos
                    A+, A-, AB+, AB-, B+, B-, O+, O-
    Retorna:
        int: La suma de todas las bolsas disponibles en todos los bancos del
        tipo de sangre a consultar.
    """

def tipo_mas_escaso(b1:dict, b2:dict, b3:dict, b4:dict)->str:
    
    suma_opositivo=b1["O+"]+b2["O+"]+b3["O+"]+b4["O+"]
    suma_onegativo=b1["O-"]+b2["O-"]+b3["O-"]+b4["O-"]
    suma_apositivo=b1["A+"]+b2["A+"]+b3["A+"]+b4["A+"]
    suma_anegativo=b1["A-"]+b2["A-"]+b3["A-"]+b4["A-"]
    suma_abpositivo=b1["AB+"]+b2["AB+"]+b3["AB+"]+b4["AB+"]
    suma_abnegativo=b1["AB-"]+b2["AB-"]+b3["AB-"]+b4["AB-"]
    suma_bpositivo=b1["B+"]+b2["B+"]+b3["B+"]+b4["B+"]
    suma_bnegativo=b1["B-"]+b2["B-"]+b3["B-"]+b4["B-"]
    
    menor= suma_opositivo
    tipo="O+"
    if suma_onegativo<menor:
       menor=suma_onegativo
       tipo="O-"
    if suma_apositivo<menor:
       menor=suma_apositivo
       tipo="A+"
    if suma_anegativo<menor:
       menor=suma_anegativo
       tipo="A-"
    if suma_abpositivo<menor:
       menor=suma_abpositivo
       tipo="AB+"
    if suma_abnegativo<menor:
       menor=suma_abnegativo
       tipo="AB-"
    if suma_bpositivo<menor:
       menor=suma_bpositivo
       tipo="B+"
    if suma_bnegativo<menor:
       menor=suma_bnegativo
       tipo="B-"
    
    return tipo 

"""Busca el tipo de sangre que tiene la menor cantidad de bolsas disponibles
       teniendo en cuenta todos los bancos.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    Retorna:
        str: Cadena de caracteres con el tipo de sangre menos disponible.
    """


def hay_tipo_en_riesgo(b1:dict, b2:dict, b3:dict, b4:dict, riesgo:int)->bool:
    tipo_riesgo = True
    suma_opositivo=b1["O+"]+b2["O+"]+b3["O+"]+b4["O+"]
    suma_onegativo=b1["O-"]+b2["O-"]+b3["O-"]+b4["O-"]
    suma_apositivo=b1["A+"]+b2["A+"]+b3["A+"]+b4["A+"]
    suma_anegativo=b1["A-"]+b2["A-"]+b3["A-"]+b4["A-"]
    suma_abpositivo=b1["AB+"]+b2["AB+"]+b3["AB+"]+b4["AB+"]
    suma_abnegativo=b1["AB-"]+b2["AB-"]+b3["AB-"]+b4["AB-"]
    suma_bpositivo=b1["B+"]+b2["B+"]+b3["B+"]+b4["B+"]
    suma_bnegativo=b1["B-"]+b2["B-"]+b3["B-"]+b4["B-"]
     
    if suma_opositivo<riesgo:
       tipo_riesgo
    elif suma_onegativo<riesgo:
       tipo_riesgo
    elif suma_apositivo<riesgo:
       tipo_riesgo 
    elif suma_anegativo<riesgo:
       tipo_riesgo 
    elif suma_abpositivo<riesgo:
       tipo_riesgo 
    elif suma_abnegativo<riesgo:
       tipo_riesgo 
    elif suma_bpositivo<riesgo:
       tipo_riesgo 
    elif suma_bnegativo<riesgo:
       tipo_riesgo
    return tipo_riesgo 

    """Determina si existe un tipo de sangre cuya cantidad total de bolsas (teniendo
       en cuenta los 4 bancos) es inferior al numero recibido por parametro.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
        riesgo (int): Numero minimo para considerar un tipo de sangre como en riesgo.
    Retorna:
        bool: True si hay algun tipo en riesgo, False de lo contrario.
    """



def promedio_donantes(b1:dict, b2:dict, b3:dict, b4:dict)->float:
    promedio = (b1['donantes']+ b2['donantes'] + b3['donantes'] + b4['donantes'])/4
    return round(promedio,2)
    """Calcula la cantidad promedio de donantes por banco de sangre.
    Parametros:
        b1 (dict): Diccionario con la informacion del banco 1.
        b2 (dict): Diccionario con la informacion del banco 2.
        b3 (dict): Diccionario con la informacion del banco 3.
        b4 (dict): Diccionario con la informacion del banco 4.
    Retorna:
        float: Promedio de donantes entre los 4 bancos, redondeado a 2
        decimales.
    """
