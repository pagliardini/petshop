from db import execute_query, fetch_query

def gestionar_proveedores():
    while True:
        print("Gestionando proveedores")
        print("1. Mostrar proveedores")
        print("2. Añadir Proveedor")
        print("3. Eliminar Proveedor")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_proveedores()
        elif opcion == "2":
            añadir_proveedor()
        elif opcion == "3":
            eliminar_proveedor()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_proveedores():
    query = "SELECT ID_Proveedor, CUIT, Nombre, Apellido, Telefono FROM Proveedores"
    proveedores = fetch_query(query)
    print("Proveedores:")
    for proveedor in proveedores:
        print(f"ID: {proveedor[0]}, CUIT: {proveedor[1]}, Nombre: {proveedor[2]}, Apellido: {proveedor[3]}, Teléfono: {proveedor[4]}")

def añadir_proveedor():
    ID_Proveedor = input("Ingrese el ID del proveedor: ")
    CUIT = input("Ingrese el CUIT del proveedor: ")
    nombre = input("Ingrese el nombre del proveedor: ")
    apellido = input("Ingrese el apellido del proveedor: ")
    telefono = input("Ingrese el teléfono del proveedor: ")
    
    query = """
    INSERT INTO Proveedores (ID_Proveedor, CUIT, Nombre, Apellido, Telefono)
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (ID_Proveedor, CUIT, nombre, apellido, telefono)
    
    try:
        execute_query(query, params)
        print("Proveedor añadido correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al añadir proveedor: {err}")

def eliminar_proveedor():
    ID_Proveedor = input("Ingrese el ID del proveedor a eliminar: ")
    
    # Verificar si el proveedor existe
    query_check = "SELECT COUNT(*) FROM Proveedores WHERE ID_Proveedor = %s"
    params_check = (ID_Proveedor,)
    proveedor_existe = fetch_query(query_check, params_check)[0][0]

    if proveedor_existe == 0:
        print("Error: El proveedor con el ID especificado no existe.")
        return
    
    query = "DELETE FROM Proveedores WHERE ID_Proveedor = %s"
    params = (ID_Proveedor,)
    
    try:
        execute_query(query, params)
        print("Proveedor eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar proveedor: {err}")
