def validate_int(numero:str, minimo:int,maximo:int)->int|None:
    try:
        numero = int(numero)
        if numero < minimo or numero > maximo:
            numero = None
    except ValueError:
        numero = None
    return numero

def get_number_int(mensaje:str, minimo:int, maximo:int) -> int|None:
    while True:
        numero_ingresado = input(mensaje)
        resultado = validate_int(numero_ingresado,minimo,maximo)         
        if resultado != None:
            return resultado
        else:
            print(f"{numero_ingresado} no es un número válido o esta fuera del rango. Reingrese")    