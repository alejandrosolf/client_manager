import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Buscar cliente      ")
        print("[3] Agregar cliente     ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Cerrar Gestor       ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los clientes...\n")
            if len(db.Clientes.lista) > 0: 
                for cliente in db.Clientes.lista:
                    print(cliente)
            else:
                print("No hay clientes registrados")

        elif opcion == '2':
            print("Buscando cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado")

        elif opcion == '3':
            print("Agregando cliente...\n")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
                if helpers.validar_dni(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            cliente = db.Clientes.crear(dni, nombre, apellido)
            print(f"Cliente {cliente} agregado correctamente")

        elif opcion == '4':
            print("Modificando cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nuevo nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Nuevo apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                nuevo_cliente = db.Clientes.modificar(dni, nombre, apellido)
                print(nuevo_cliente)
            else:
                print("Cliente inexistente.")

        elif opcion == '5':
            print("Borrando cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(f"{cliente} borrado correctamente") if db.Clientes.borrar(dni) else print("Cliente inexistente.")

        elif opcion == '6':
            print("Saliendo cliente...\n")
            break

        input("\nPresiona ENTER para continuar...")
