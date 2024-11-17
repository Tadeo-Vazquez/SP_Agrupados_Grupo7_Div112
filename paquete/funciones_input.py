def validate_int(numero:str, minimo:int,maximo:int)->int|None:
    """valida si un numero se puede castear a entero y luego si esta dentro de los valores permitidos
    Args:
        numero (str): numero a validar
        minimo (int): valor minimo permitido
        maximo (int): valor maximo permitido

    Returns:
        int|None: retorna el numero casteado a entero si es válido y si no lo es, None
    """
    try:
        numero = int(numero)
        if numero < minimo or numero > maximo:
            numero = None
    except ValueError:
        numero = None
    return numero

def get_number_int(mensaje:str, minimo:int, maximo:int) -> int:
    """solicita un numero al usuario y lo valida. 
    En caso de no poder validarlo lo vuelve a solicitar hasta poder
    Args:
        mensaje (str): solicitud de ingreso de numero
        minimo (int): minimo valor permitido
        maximo (int): maximo valor permitido
    Returns:
        int: retorna el numero validado
    """
    while True:
        numero_ingresado = input(mensaje)
        resultado = validate_int(numero_ingresado,minimo,maximo)         
        if resultado != None:
            return resultado
        else:
            print(f"{numero_ingresado} no es un número válido o esta fuera del rango. Reingrese")    