from db import execute_query, fetch_query
from pedidos import gestionar_pedidos
def gestionar_sucursales():
    while True:
        print("\nGestionar Sucursales")
        print("1. Ver Sucursales")
        print("2. Agregar Sucursal")
        print("3. Actualizar Sucursal")
        print("4. Eliminar Sucursal")
        print("5. Pedidos Sucursales")
        print("6. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ver_sucursales()
        elif opcion == "2":
            agregar_sucursal()
        elif opcion == "3":
            actualizar_sucursal()
        elif opcion == "4":
            eliminar_sucursal()
        elif opcion == "5":
            gestionar_pedidos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def ver_sucursales():
    query = "SELECT * FROM Sucursales"
    results = fetch_query(query)
    for row in results:
        print(row)

def agregar_sucursal():
    ciudad = input("Ingrese la Ciudad: ")
    direccion = input("Ingrese la Dirección: ")
    telefono = input("Ingrese el Teléfono: ")
    email = input("Ingrese el Email: ")

    query = """
    INSERT INTO Sucursales (Ciudad, Direccion, Telefono, Email)
    VALUES (%s, %s, %s, %s)
    """
    params = (ciudad, direccion, telefono, email)
    execute_query(query, params)
    print("Sucursal agregada correctamente.")

def actualizar_sucursal():
    sucursales = fetch_query("SELECT ID_Sucursal, Ciudad, Direccion FROM Sucursales")
    
    print("Seleccione la sucursal que desea actualizar:")
    for idx, sucursal in enumerate(sucursales):
        print(f"{idx + 1}. ID: {sucursal[0]}, Ciudad: {sucursal[1]}, Dirección: {sucursal[2]}")
    
    seleccion = int(input("Ingrese el número de la sucursal a actualizar: ")) - 1
    
    if seleccion < 0 or seleccion >= len(sucursales):
        print("Selección inválida.")
        return

    id_sucursal = sucursales[seleccion][0]
    ciudad = input("Ingrese la nueva Ciudad: ")
    direccion = input("Ingrese la nueva Dirección: ")
    telefono = input("Ingrese el nuevo Teléfono: ")
    email = input("Ingrese el nuevo Email: ")

    query = """
    UPDATE Sucursales
    SET Ciudad = %s, Direccion = %s, Telefono = %s, Email = %s
    WHERE ID_Sucursal = %s
    """
    params = (ciudad, direccion, telefono, email, id_sucursal)
    execute_query(query, params)
    print("Sucursal actualizada correctamente.")

def eliminar_sucursal():
    sucursales = fetch_query("SELECT ID_Sucursal, Ciudad, Direccion FROM Sucursales")
    
    print("Seleccione la sucursal que desea eliminar:")
    for idx, sucursal in enumerate(sucursales):
        print(f"{idx + 1}. ID: {sucursal[0]}, Ciudad: {sucursal[1]}, Dirección: {sucursal[2]}")
    
    seleccion = int(input("Ingrese el número de la sucursal a eliminar: ")) - 1
    
    if seleccion < 0 or seleccion >= len(sucursales):
        print("Selección inválida.")
        return

    id_sucursal = sucursales[seleccion][0]
    
    query = "DELETE FROM Sucursales WHERE ID_Sucursal = %s"
    params = (id_sucursal,)
    execute_query(query, params)
    print("Sucursal eliminada correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    gestionar_sucursales()
