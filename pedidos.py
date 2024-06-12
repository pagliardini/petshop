from db import execute_query, fetch_query, ultimoid

def gestionar_pedidos():
    while True:
        print("Gestionando Pedidos")
        print("1. Mostrar Pedidos")
        print("2. Añadir Pedido")
        print("3. Eliminar Pedido")
        print("4. Detalles de Pedidos")
        print("5. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_pedidos()
        elif opcion == "2":
            añadir_pedido()
        elif opcion == "3":
            eliminar_pedido()
        elif opcion == "4":
            detalle_pedidos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_pedidos():
    query = """
    SELECT p.ID_Pedido, p.Fecha, p.Estado, pr.Nombre AS Proveedor, s.Ciudad AS Sucursal
    FROM Pedidos p
    JOIN Proveedores pr ON p.ID_Proveedor = pr.ID_Proveedor
    JOIN Sucursales s ON p.ID_Sucursal = s.ID_Sucursal
    """
    pedidos = fetch_query(query)
    if pedidos:
        print("Pedidos:")
        for pedido in pedidos:
            print(
                f"ID Pedido: {pedido[0]}, Fecha: {pedido[1]}, Estado: {pedido[2]}, Proveedor: {pedido[3]}, Sucursal: {pedido[4]}")
    else:
        print("No se encontraron pedidos.")

def añadir_pedido():
    # Obtener datos del pedido sin solicitar fecha
    id_proveedor = input("Ingrese el ID del proveedor: ")
    estado = input("Ingrese el estado del pedido: ")
    id_sucursal = input("Ingrese el ID de la sucursal: ")

    # Insertar en la tabla Pedidos con la fecha actual
    query_pedido = """
    INSERT INTO Pedidos (Fecha, ID_Proveedor, Estado, ID_Sucursal)
    VALUES (NOW(), %s, %s, %s)
    """
    params_pedido = (id_proveedor, estado, id_sucursal)

    try:
        id_pedido = ultimoid(query_pedido, params_pedido)
        print(f"Pedido añadido correctamente con ID {id_pedido}")
    except Exception as err:
        print(f"Error al añadir pedido: {err}")
        return

    # Añadir detalles del pedido
    while True:
        codigo_de_barras = input("Ingrese el código de barras del producto (o 'fin' para terminar): ")
        if codigo_de_barras.lower() == 'fin':
            break

        # Verificar si el producto existe
        producto_existe = fetch_query("SELECT COUNT(*) FROM Productos WHERE Codigo_de_barras = %s", (codigo_de_barras,))[0][0]
        if producto_existe == 0:
            print(f"Error: El producto con el código de barras {codigo_de_barras} no existe.")
            continue

        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))
        total = cantidad * precio_unitario

        query_detalle = """
        INSERT INTO Detalle_Pedidos (ID_Pedido, Codigo_de_barras, Cantidad, Precio_Unitario, Total)
        VALUES (%s, %s, %s, %s, %s)
        """
        params_detalle = (id_pedido, codigo_de_barras, cantidad, precio_unitario, total)

        try:
            execute_query(query_detalle, params_detalle)
            print("Detalle de pedido añadido correctamente.")
        except Exception as err:
            print(f"El error '{err}' ocurrió al añadir detalle de pedido.")

def eliminar_pedido():
    id_pedido = input("Ingrese el ID del pedido a eliminar: ")

    # Verificar si el pedido existe
    query_check = "SELECT COUNT(*) FROM Pedidos WHERE ID_Pedido = %s"
    params_check = (id_pedido,)
    pedido_existe = fetch_query(query_check, params_check)[0][0]

    if pedido_existe == 0:
        print("Error: El pedido con el ID especificado no existe.")
        return

    # Eliminar detalles del pedido
    query_detalle = "DELETE FROM Detalle_Pedidos WHERE ID_Pedido = %s"
    params_detalle = (id_pedido,)

    try:
        execute_query(query_detalle, params_detalle)
    except Exception as err:
        print(f"Error al eliminar detalles de pedido: {err}")
        return

    # Eliminar pedido
    query = "DELETE FROM Pedidos WHERE ID_Pedido = %s"
    params = (id_pedido,)

    try:
        execute_query(query, params)
        print("Pedido eliminado correctamente.")
    except Exception as err:
        print(f"Error al eliminar pedido: {err}")

def detalle_pedidos():
    id_pedido = input("Ingrese el ID del pedido para ver sus detalles: ")
    query = """
    SELECT d.ID_Detalle, d.Codigo_de_barras, d.Cantidad, d.Precio_Unitario, d.Total
    FROM Detalle_Pedidos d
    WHERE d.ID_Pedido = %s
    """
    detalles = fetch_query(query, (id_pedido,))
    if detalles:
        print("Detalles de Pedidos:")
        for detalle in detalles:
            print(f"ID Detalle: {detalle[0]}, Código de Barras: {detalle[1]}, Cantidad: {detalle[2]}, Precio Unitario: {detalle[3]}, Total: {detalle[4]}")
    else:
        print("No se encontraron detalles para este pedido.")

# Ejemplo de uso
if __name__ == "__main__":
    gestionar_pedidos()
