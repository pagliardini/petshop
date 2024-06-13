from db import execute_query

def insertar_datos_ejemplo():
    # Datos de ejemplo para Proveedores
    proveedores = [
        ("20359176377", "Nombre 1", "Apellido 1", "123456789"),
        ("20359176378", "Nombre 2", "Apellido 2", "987654321"),
        ("20359176379", "Nombre 3", "Apellido 3", "456123789")
    ]
    query_proveedor = """
    INSERT INTO Proveedores (CUIT, Nombre, Apellido, Telefono)
    VALUES (%s, %s, %s, %s)
    """
    for proveedor in proveedores:
        execute_query(query_proveedor, proveedor)

    # Datos de ejemplo para Categorias
    categorias = [
        ("Alimentos", "Comida para mascotas"),
        ("Juguetes", "Juguetes para mascotas"),
        ("Accesorios", "Accesorios para mascotas")
    ]
    query_categoria = """
    INSERT INTO Categoria (Nombre, Descripcion)
    VALUES (%s, %s)
    """
    for categoria in categorias:
        execute_query(query_categoria, categoria)

    # Datos de ejemplo para Productos
    productos = [
        ("1234567890123", "Comida para perros", 10.50, 100, 1, "Comida seca para perros adultos"),
        ("1234567890124", "Pelota para perros", 5.99, 50, 2, "Pelota de goma para perros"),
        ("1234567890125", "Collar para gatos", 7.99, 200, 3, "Collar ajustable para gatos")
    ]
    query_producto = """
    INSERT INTO Productos (Codigo_de_barras, Nombre, Precio_Unitario, Stock, ID_Categoria, Descripcion)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    for producto in productos:
        execute_query(query_producto, producto)

    # Datos de ejemplo para Clientes
    clientes = [
        ("Cliente A", "Apellido Cliente A", "123456789", "clientea@gmail.com"),
        ("Cliente B", "Apellido Cliente B", "987654321", "clientb@gmail.com"),
        ("Cliente C", "Apellido Cliente C", "321654987", "clientec@gmail.com")
    ]
    query_cliente = """
    INSERT INTO Clientes (Nombre, Apellido, Telefono, Email)
    VALUES (%s, %s, %s, %s)
    """
    for cliente in clientes:
        execute_query(query_cliente, cliente)

    # Datos de ejemplo para Sucursales
    sucursales = [
        ("Ciudad A", "Calle 1, Ciudad A", "123456789", "sucursalA@gmail.com"),
        ("Ciudad B", "Calle 2, Ciudad B", "987654321", "sucursalB@gmail.com"),
        ("Ciudad C", "Calle 3, Ciudad C", "456123789", "sucursalC@gmail.com")
    ]
    query_sucursal = """
    INSERT INTO Sucursales (Ciudad, Direccion, Telefono, Email)
    VALUES (%s, %s, %s, %s)
    """
    for sucursal in sucursales:
        execute_query(query_sucursal, sucursal)

    # Datos de ejemplo para Ventas
    ventas = [
        ("2023-06-01 12:34:56", "Efectivo", 0.00, 100.50, 1, 1),
        ("2023-06-02 13:45:00", "Tarjeta", 5.00, 95.00, 2, 2),
        ("2023-06-03 14:56:22", "Transferencia", 10.00, 90.50, 3, 3)
    ]
    query_venta = """
    INSERT INTO Ventas (Fecha, Forma_Pago, Descuento, Total_Venta, ID_Cliente, ID_Sucursal)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    for venta in ventas:
        execute_query(query_venta, venta)

    # Datos de ejemplo para Detalle_Ventas
    detalles_ventas = [
        (1, "1234567890123", 2, 10.50, 0.00, 21.00),
        (2, "1234567890124", 1, 5.99, 0.00, 5.99),
        (3, "1234567890125", 3, 7.99, 0.00, 23.97)
    ]
    query_detalle_venta = """
    INSERT INTO Detalle_Ventas (ID_Venta, Codigo_de_barras, Cantidad_Unidades, Precio_Unitario, Descuento, Total_Item)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    for detalle in detalles_ventas:
        execute_query(query_detalle_venta, detalle)

    # Datos de ejemplo para Empleados
    empleados = [
        ("20359176381", "Empleado 1", "Apellido 1", "123456789", "empleado1@example.com", "Calle 1, Ciudad A", 1),
        ("20359176382", "Empleado 2", "Apellido 2", "987654321", "empleado2@example.com", "Calle 2, Ciudad B", 2),
        ("20359176383", "Empleado 3", "Apellido 3", "456123789", "empleado3@example.com", "Calle 3, Ciudad C", 3)
    ]
    query_empleado = """
    INSERT INTO Empleados (CUIL_Empleado, Nombre, Apellido, Telefono, Email, Direccion, ID_Sucursal)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for empleado in empleados:
        execute_query(query_empleado, empleado)

    # Datos de ejemplo para Pedidos
    pedidos = [
        ("2023-06-01 10:30:00", 1, "Pendiente", 1),
        ("2023-06-02 11:45:00", 2, "En camino", 2),
        ("2023-06-03 12:50:00", 3, "Entregado", 3)
    ]
    query_pedido = """
    INSERT INTO Pedidos (Fecha, ID_Proveedor, Estado, ID_Sucursal)
    VALUES (%s, %s, %s, %s)
    """
    for pedido in pedidos:
        execute_query(query_pedido, pedido)

    # Datos de ejemplo para Detalle_Pedidos
    detalles_pedidos = [
        (1, "1234567890123", 10, 10.50, 105.00),
        (2, "1234567890124", 20, 5.99, 119.80),
        (3, "1234567890125", 30, 7.99, 239.70)
    ]
    query_detalle_pedido = """
    INSERT INTO Detalle_Pedidos (ID_Pedido, Codigo_de_barras, Cantidad, Precio_Unitario, Total)
    VALUES (%s, %s, %s, %s, %s)
    """
    for detalle in detalles_pedidos:
        execute_query(query_detalle_pedido, detalle)

if __name__ == "__main__":
    insertar_datos_ejemplo()
