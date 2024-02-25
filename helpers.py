import re
import os
import platform

def limpiar_pantalla():
    """Helper para limpiar la pantalla independientemente del sistema operativo de la pc"""
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    """Helper para leer inputs de manera correcta"""
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def validar_dni(dni, lista):
    """Funcion para validar que el dni sea valido"""
    if not re.match('[0-9]{2}[A-Z]', dni):
        print("DNI incorrecto, formato invalido.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True
