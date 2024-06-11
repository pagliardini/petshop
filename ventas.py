from db import execute_query, fetch_query

def gestionar_ventas():
    while True:
        print("Gestionando Ventas")
        print("1. Mostrar Ventas")
        print("2. Añadir Venta")
        print("3. Eliminar Venta")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            añadir_venta()
        elif opcion == "3":
            eliminar_venta()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_ventas():
    query = """
    SELECT v.ID_Venta, v.Fecha, v.Forma_Pago, v.Descuento, v.Total_Venta, c.Nombre AS Cliente, s.Nombre AS Sucursal
    FROM Ventas v
    JOIN Clientes c ON v.ID_Cliente = c.ID_Cliente
    JOIN Sucursales s ON v.ID_Sucursal = s.ID_Sucursal
    """
    ventas = fetch_query(query)
    print("Ventas:")
    for venta in ventas:
        print(f"ID Venta: {venta[0]}, Fecha: {venta[1]}, Forma de Pago: {venta[2]}, Descuento: {venta[3]}, Total Venta: {venta[4]}, Cliente: {venta[5]}, Sucursal: {venta[6]}")

def añadir_venta():
    # Obtener datos de la venta
    forma_pago = input("Ingrese la forma de pago: ")
    descuento = float(input("Ingrese el descuento (opcional, puede dejar en blanco): ") or 0)
    total_venta = float(input("Ingrese el total de la venta: "))
    id_cliente = input("Ingrese el ID del cliente: ")
    id_sucursal = input("Ingrese el ID de la sucursal: ")

    # Insertar en la tabla Ventas
    query_venta = """
    INSERT INTO Ventas (Forma_Pago, Descuento, Total_Venta, ID_Cliente, ID_Sucursal)
    VALUES (%s, %s, %s, %s, %s)
    """
    params_venta = (forma_pago, descuento, total_venta, id_cliente, id_sucursal)
    
    try:
        execute_query(query_venta, params_venta)
        id_venta = fetch_query("SELECT LAST_INSERT_ID()")[0][0]
        print(f"Venta añadida correctamente con ID: {id_venta}")
    except Exception as err:
        print(f"Error al añadir venta: {err}")
        return

    # Añadir detalles de la venta
    while True:
        codigo_de_barras = input("Ingrese el código de barras del producto (o 'fin' para terminar): ")
        if codigo_de_barras.lower() == 'fin':
            break
        cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))
        descuento_item = float(input("Ingrese el descuento para este item: ") or 0)
        total_item = cantidad_unidades * precio_unitario - descuento_item
        
        query_detalle = """
        INSERT INTO Detalle_Ventas (ID_Venta, Codigo_de_barras, Cantidad_Unidades, Precio_Unitario, Descuento, Total_Item)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params_detalle = (id_venta, codigo_de_barras, cantidad_unidades, precio_unitario, descuento_item, total_item)
        
        try:
            execute_query(query_detalle, params_detalle)
            print("Detalle de venta añadido correctamente.")
        except Exception as err:
            print(f"Error al añadir detalle de venta: {err}")

def eliminar_venta():
    id_venta = input("Ingrese el ID de la venta a eliminar: ")

    # Verificar si la venta existe
    query_check = "SELECT COUNT(*) FROM Ventas WHERE ID_Venta = %s"
    params_check = (id_venta,)
    venta_existe = fetch_query(query_check, params_check)[0][0]

    if venta_existe == 0:
        print("Error: La venta con el ID especificado no existe.")
        return
    
    # Eliminar detalles de la venta
    query_detalle = "DELETE FROM Detalle_Ventas WHERE ID_Venta = %s"
    params_detalle = (id_venta,)
    
    try:
        execute_query(query_detalle, params_detalle)
    except Exception as err:
        print(f"Error al eliminar detalles de venta: {err}")
        return
    
    # Eliminar venta
    query = "DELETE FROM Ventas WHERE ID_Venta = %s"
    params = (id_venta,)
    
    try:
        execute_query(query, params)
        print("Venta eliminada correctamente.")
    except Exception as err:
        print(f"Error al eliminar venta: {err}")

# Ejemplo de uso
if __name__ == "__main__":
    gestionar_ventas()
