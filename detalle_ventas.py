from db import execute_query, fetch_query

def gestionar_detalle_ventas():
    while True:
        print("\nGestionando Detalle de Ventas")
        print("1. Mostrar Detalle de Ventas")
        print("2. Añadir Detalle de Venta")
        print("3. Eliminar Detalle de Venta")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_detalle_ventas()
        elif opcion == "2":
            añadir_detalle_venta()
        elif opcion == "3":
            eliminar_detalle_venta()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def listar_ventas_con_detalles():
    query = """
    SELECT v.ID_Venta, v.Fecha, v.Total_Venta
    FROM Ventas v
    JOIN Detalle_Ventas d ON v.ID_Venta = d.ID_Venta
    GROUP BY v.ID_Venta, v.Fecha, v.Total_Venta
    """
    ventas = fetch_query(query)
    print("Ventas con detalles:")
    for index, venta in enumerate(ventas):
        print(f"{index + 1}. ID: {venta[0]}, Fecha: {venta[1]}, Total: {venta[2]}")
    return ventas

def seleccionar_venta():
    ventas = listar_ventas_con_detalles()
    seleccion = None
    while seleccion is None:
        try:
            opcion = int(input("Seleccione el número de la venta: "))
            if 1 <= opcion <= len(ventas):
                seleccion = ventas[opcion - 1][0]  # Devuelve el ID de la venta seleccionada
            else:
                print("Número de venta inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    return seleccion

def mostrar_detalle_ventas():
    id_venta = seleccionar_venta()
    query = """
    SELECT d.ID_Detalle, d.Codigo_de_barras, d.Cantidad_Unidades, d.Precio_Unitario, d.Descuento, d.Total_Item
    FROM Detalle_Ventas d
    WHERE d.ID_Venta = %s
    """
    detalles = fetch_query(query, (id_venta,))
    if detalles:
        print("Detalles de Ventas:")
        for detalle in detalles:
            print(f"ID Detalle: {detalle[0]}, Código de Barras: {detalle[1]}, Cantidad: {detalle[2]}, Precio Unitario: {detalle[3]}, Descuento: {detalle[4]}, Total: {detalle[5]}")
    else:
        print("No se encontraron detalles para esta venta.")

def añadir_detalle_venta():
    id_venta = seleccionar_venta()
    codigo_de_barras = input("Ingrese el código de barras del producto: ")

    # Verificar si el producto existe
    producto_existe = fetch_query("SELECT COUNT(*) FROM Productos WHERE Codigo_de_barras = %s", (codigo_de_barras,))[0][0]
    if producto_existe == 0:
        print(f"Error: El producto con el código de barras {codigo_de_barras} no existe.")
        return

    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
    precio_unitario = float(input("Ingrese el precio unitario: "))
    descuento = float(input("Ingrese el descuento (opcional, puede dejar en blanco): ") or 0)
    total_item = cantidad_unidades * precio_unitario - descuento

    query = """
    INSERT INTO Detalle_Ventas (ID_Venta, Codigo_de_barras, Cantidad_Unidades, Precio_Unitario, Descuento, Total_Item)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (id_venta, codigo_de_barras, cantidad_unidades, precio_unitario, descuento, total_item)

    try:
        execute_query(query, params)
        print("Detalle de venta añadido correctamente.")
    except Exception as err:
        print(f"El error '{err}' ocurrió al añadir detalle de venta.")

def eliminar_detalle_venta():
    id_detalle = input("Ingrese el ID del detalle de venta a eliminar: ")

    # Verificar si el detalle existe
    query_check = "SELECT COUNT(*) FROM Detalle_Ventas WHERE ID_Detalle = %s"
    params_check = (id_detalle,)
    detalle_existe = fetch_query(query_check, params_check)[0][0]

    if detalle_existe == 0:
        print("Error: El detalle de venta con el ID especificado no existe.")
        return

    query = "DELETE FROM Detalle_Ventas WHERE ID_Detalle = %s"
    params = (id_detalle,)

    try:
        execute_query(query, params)
        print("Detalle de venta eliminado correctamente.")
    except Exception as err:
        print(f"Error al eliminar detalle de venta: {err}")

# Ejemplo de uso
if __name__ == "__main__":
    gestionar_detalle_ventas()
