import csv
import config


class Cliente:
    """Clase para la estructura de cada cliente"""
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

class Clientes:
    """Clase para manejar la informacion de cada cliente"""

    lista = []
    with open(config.DATABASE_PATH, newline='\n', encoding='utf-8') as fichero:
        reader = csv.reader(fichero, delimiter=',')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(dni):
        """Metodo para buscar por dni"""
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        """Metodo para crear un cliente"""
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        """Metodo para modificar la informacion de un cliente"""
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        """Metodo para borrar un cliete por dni"""
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente


    @staticmethod
    def guardar():
        """Metodo para guardar datos en el csv"""
        with open(config.DATABASE_PATH, 'w', newline='\n', encoding='utf-8') as fichero:
            writer = csv.writer(fichero, delimiter=',')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
