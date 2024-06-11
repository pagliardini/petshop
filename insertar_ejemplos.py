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
        ("Ciudad A", "Calle 1, Ciudad A", "123456789", "sucursalA@example.com"),
        ("Ciudad B", "Calle 2, Ciudad B", "987654321", "sucursalB@example.com"),
        ("Ciudad C", "Calle 3, Ciudad C", "456123789", "sucursalC@example.com")
    ]
    query_sucursal = """
    INSERT INTO Sucursales (Ciudad, Direccion, Telefono, Email)
    VALUES (%s, %s, %s, %s)
    """
    for sucursal in sucursales:
        execute_query(query_sucursal, sucursal)

if __name__ == "__main__":
    insertar_datos_ejemplo()
