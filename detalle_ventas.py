# detalle_ventas.py

detalle_ventas = []

def gestionar_detalle_ventas():
    while True:
        print("Gestionando Detalle de Ventas")
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

def mostrar_detalle_ventas():
    print("Detalle de Ventas:")
    for detalle in detalle_ventas:
        print(detalle)

def añadir_detalle_venta():
    id_venta = input("Ingrese el ID de la venta: ")
    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
    precio_unitario = float(input("Ingrese el precio unitario: "))
    descuento = float(input("Ingrese el descuento: "))
    total = float(input("Ingrese el total: "))
    codigo_barras = input("Ingrese el código de barras del producto: ")
    nuevo_detalle = {
        "id_venta": id_venta,
        "cantidad_unidades": cantidad_unidades,
        "precio_unitario": precio_unitario,
        "descuento": descuento,
        "total": total,
        "codigo_barras": codigo_barras
    }
    detalle_ventas.append(nuevo_detalle)
    print("Detalle de venta añadido correctamente.")

def eliminar_detalle_venta():
    id_detalle = input("Ingrese el ID del detalle de venta a eliminar: ")
    for detalle in detalle_ventas:
        if detalle.get("id_detalle") == id_detalle:
            detalle_ventas.remove(detalle)
            print("Detalle de venta eliminado correctamente.")
            break
    else:
        print("No se encontró el detalle de venta.")
