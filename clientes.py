from db import execute_query, fetch_query

def gestionar_clientes():
    while True:
        print("Gestionando clientes")
        print("1. Mostrar clientes")
        print("2. Añadir cliente")
        print("3. Eliminar cliente")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_clientes()
        elif opcion == "2":
            añadir_cliente()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_clientes():
    query = "SELECT `ID_Cliente`, Nombre, Apellido, Telefono, Email FROM Clientes"
    clientes = fetch_query(query)
    print("Clientes:")
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Teléfono: {cliente[3]}, Email: {cliente[4]}")

def añadir_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    email = input("Ingrese el email del cliente (opcional): ")
    
    query = """
    INSERT INTO Clientes (Nombre, Apellido, Telefono, Email)
    VALUES (%s, %s, %s, %s)
    """
    params = (nombre, apellido, telefono, email)
    
    try:
        execute_query(query, params)
        print("Cliente añadido correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al añadir cliente: {err}")

def eliminar_cliente():
    ID_Cliente = input("Ingrese el ID del cliente a eliminar: ")
    
    # Verificar si el cliente existe
    query_check = "SELECT COUNT(*) FROM Clientes WHERE `ID_Cliente` = %s"
    params_check = (ID_Cliente,)
    cliente_existe = fetch_query(query_check, params_check)[0][0]

    if cliente_existe == 0:
        print("Error: El cliente con el ID especificado no existe.")
        return
    
    query = "DELETE FROM Clientes WHERE `ID_Cliente` = %s"
    params = (ID_Cliente,)
    
    try:
        execute_query(query, params)
        print("Cliente eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar cliente: {err}")
