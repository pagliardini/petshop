from sucursales import gestionar_sucursales
from productos import gestionar_productos
from ventas import gestionar_ventas
from proveedores import gestionar_proveedores
from categoria_productos import gestionar_categorias
from clientes import gestionar_clientes
from empleados import gestionar_empleados


def menu_principal():
    while True:
        print("Bienvenido al Sistema de Control de Stock")
        print("1. Gestionar Sucursales")
        print("2. Gestionar Productos")
        print("3. Gestionar Ventas")
        print("4. Gestionar Proveedores")
        print("5. Gestionar Clientes")
        print("6. Gestionar Categorías de Productos")
        print("7. Gestionar empleados")
        print("8. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            gestionar_sucursales()
        elif opcion == "2":
            gestionar_productos()
        elif opcion == "3":
            gestionar_ventas()
        elif opcion == "4":
            gestionar_proveedores()
        elif opcion == "5":
            gestionar_clientes()
        elif opcion == "6":
            gestionar_categorias()            
        elif opcion == "7":
            gestionar_empleados()
        elif opcion == "8":
            print("Gracias por usar el Sistema de Control de Stock.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_principal()
