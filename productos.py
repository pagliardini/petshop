from db import execute_query, fetch_query

def gestionar_productos():
    while True:
        print("Gestionando productos")
        print("1. Mostrar todos los productos")
        print("2. Añadir un nuevo producto")
        print("3. Eliminar un producto")
        print("4. Buscar productos por nombre")
        print("5. Ver la cantidad de productos por categoría")
        print("6. Filtrar productos por categoría y stock")
        print("7. Buscar productos por descripción")
        print("8. Buscar productos por rango de precios")
        print("9. Mostrar una cantidad limitada de productos")
        print("10. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            añadir_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            nombre_producto = input("Ingrese el nombre del producto: ")
            mostrar_productos_por_nombre(nombre_producto)
        elif opcion == "5":
            mostrar_cantidad_productos_por_categoria()
        elif opcion == "6":
            categoria_id = input("Ingrese el ID de la categoría: ")
            stock_minimo = input("Ingrese el stock mínimo: ")
            filtrar_productos_por_categoria_y_stock(categoria_id, stock_minimo)
        elif opcion == "7":
            descripcion = input("Ingrese una palabra clave para la descripción: ")
            buscar_productos_por_descripcion(descripcion)
        elif opcion == "8":
            precio_minimo = input("Ingrese el precio mínimo: ")
            precio_maximo = input("Ingrese el precio máximo: ")
            buscar_productos_por_rango_de_precios(precio_minimo, precio_maximo)
        elif opcion == "9":
            cantidad = input("Ingrese la cantidad de productos a mostrar: ")
            mostrar_cantidad_limitada_de_productos(int(cantidad))
        elif opcion == "10":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_productos():
    query = """
    SELECT p.Codigo_de_barras, p.Nombre, p.Precio_Unitario, p.Stock, c.Nombre AS Categoria, p.Descripcion, p.En_Promocion
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    """
    productos = fetch_query(query)
    print("Productos:")
    if productos:
        for producto in productos:
            promocion = "Sí" if producto[6] else "No"
            print(f"Codigo de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}, Descripción: {producto[5]}, En Promoción: {promocion}")

def mostrar_productos_por_nombre(nombre_producto):
    query = """
    SELECT p.Codigo_de_barras, p.Nombre, p.Precio_Unitario, p.Stock, c.Nombre AS Categoria, p.Descripcion, p.En_Promocion
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    WHERE p.Nombre = %s
    """
    productos = fetch_query(query, (nombre_producto,))
    print("Productos:")
    if productos:
        for producto in productos:
            promocion = "Sí" if producto[6] else "No"
            print(f"Codigo de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}, Descripción: {producto[5]}, En Promoción: {promocion}")

def mostrar_cantidad_productos_por_categoria():
    query = """
    SELECT c.Nombre AS Categoria, COUNT(p.Codigo_de_barras) AS Total_Productos
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    GROUP BY c.Nombre
    """
    categorias = fetch_query(query)
    print("Categorías y cantidad de productos:")
    if categorias:
        for categoria in categorias:
            print(f"Categoría: {categoria[0]}, Total Productos: {categoria[1]}")

def filtrar_productos_por_categoria_y_stock(categoria_id, stock_minimo):
    query = """
    SELECT p.Codigo_de_barras, p.Nombre, p.Precio_Unitario, p.Stock, c.Nombre AS Categoria, p.Descripcion, p.En_Promocion
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    WHERE p.ID_Categoria = %s AND p.Stock >= %s
    """
    productos = fetch_query(query, (categoria_id, stock_minimo))
    print("Productos:")
    if productos:
        for producto in productos:
            promocion = "Sí" if producto[6] else "No"
            print(f"Codigo de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}, Descripción: {producto[5]}, En Promoción: {promocion}")

def buscar_productos_por_descripcion(descripcion):
    query = """
    SELECT p.Codigo_de_barras, p.Nombre, p.Precio_Unitario, p.Stock, c.Nombre AS Categoria, p.Descripcion, p.En_Promocion
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    WHERE p.Descripcion LIKE %s
    """
    productos = fetch_query(query, (f"%{descripcion}%",))
    print("Productos:")
    if productos:
        for producto in productos:
            promocion = "Sí" if producto[6] else "No"
            print(f"Codigo de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}, Descripción: {producto[5]}, En Promoción: {promocion}")

def buscar_productos_por_rango_de_precios(precio_minimo, precio_maximo):
    query = """
    SELECT p.Codigo_de_barras, p.Nombre, p.Precio_Unitario, p.Stock, c.Nombre AS Categoria, p.Descripcion, p.En_Promocion
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    WHERE p.Precio_Unitario BETWEEN %s AND %s
    """
    productos = fetch_query(query, (precio_minimo, precio_maximo))
    print("Productos:")
    if productos:
        for producto in productos:
            promocion = "Sí" if producto[6] else "No"
            print(f"Codigo de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}, Descripción: {producto[5]}, En Promoción: {promocion}")

def mostrar_cantidad_limitada_de_productos(cantidad):
    query = """
    SELECT p.Codigo_de_barras, p.Nombre, p.Precio_Unitario, p.Stock, c.Nombre AS Categoria, p.Descripcion, p.En_Promocion
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    LIMIT %s
    """
    productos = fetch_query(query, (cantidad,))
    print("Productos:")
    if productos:
        for producto in productos:
            promocion = "Sí" if producto[6] else "No"
            print(f"Codigo de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}, Descripción: {producto[5]}, En Promoción: {promocion}")

def añadir_producto():
    codigo_de_barras = input("Ingrese el código de barras del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio_unitario = input("Ingrese el precio unitario del producto: ")
    stock = input("Ingrese el stock del producto: ")

    categorias = fetch_query("SELECT ID_Categoria, Nombre FROM Categoria")
    print("Seleccione la categoría del producto:")
    for idx, categoria in enumerate(categorias):
        print(f"{idx + 1}. {categoria[1]}")

    seleccion = int(input("Ingrese el número de la categoría: ")) - 1

    if seleccion < 0 or seleccion >= len(categorias):
        print("Selección inválida.")
        return

    id_categoria = categorias[seleccion][0]
    descripcion = input("Ingrese la descripción del producto: ")
    en_promocion = input("¿El producto está en promoción? (s/n): ").lower() == 's'

    query = """
    INSERT INTO Productos (Codigo_de_barras, Nombre, Precio_Unitario, Stock, ID_Categoria, Descripcion, En_Promocion)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (codigo_de_barras, nombre, precio_unitario, stock, id_categoria, descripcion, en_promocion)

    try:
        execute_query(query, params)
        print("Producto añadido correctamente.")
    except Exception as err:
        print(f"Error al añadir producto: {err}")

def eliminar_producto():
    codigo_de_barras = input("Ingrese el código de barras del producto a eliminar: ")

    query_check = "SELECT COUNT(*) FROM Productos WHERE Codigo_de_barras = %s"
    params_check = (codigo_de_barras,)
    producto_existe = fetch_query(query_check, params_check)[0][0]

    if producto_existe == 0:
        print("Error: El producto con el código de barras especificado no existe.")
        return

    query = "DELETE FROM Productos WHERE Codigo_de_barras = %s"
    params = (codigo_de_barras,)

    try:
        execute_query(query, params)
        print("Producto eliminado correctamente.")
    except Exception as err:
        print(f"Error al eliminar producto: {err}")

if __name__ == "__main__":
    gestionar_productos()
