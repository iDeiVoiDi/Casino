#=============================
# ADMIN TOOLS
#=============================
# Panel de herramientas de desarrollador por consola

from app import db

def menu():
    db.crear_tablas()  # iniciamos la base de datos y la tabla si no existía

    while True:
        print("\n|| HERRAMIENTAS DE DESARROLLADOR ||")
        print("1| Listar cuentas")
        print("2| Crear cuenta")
        print("3| Modificar puntos")
        print("4| Renombrar cuenta")
        print("5| Eliminar cuenta")
        print("0| Salir")
        opcion = input("> ")

        if opcion == "1":
            print("\nID | NOMBRE | PUNTOS")
            for cuenta in db.listar_cuentas():
                print(f"{cuenta['id']} | {cuenta['nombre']} | {cuenta['puntos']} pts")

        elif opcion == "2":
            nombre = input("• Nombre: ")
            db.crear_cuenta(nombre)

        elif opcion == "3":
            nombre = input("• Nombre: ")
            cantidad = int(input("• Cantidad: ")) # Los negativos restan
            db.modificar_puntos(nombre, cantidad)

        elif opcion == "4":
            actual = input("• Nombre actual: ")
            nuevo = input("• Nombre nuevo: ")
            db.renombrar_cuenta(actual, nuevo)

        elif opcion == "5":
            nombre = input("• Nombre a eliminar: ")
            db.eliminar_cuenta(nombre)

        elif opcion == "0":
            break

        else:
            print("| Opción no válida |")


# Esto solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    menu()
