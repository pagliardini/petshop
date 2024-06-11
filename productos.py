from db import execute_query, fetch_query

def gestionar_productos():
    while True:
        print("Gestionando productos")
        print("1. Mostrar productos")
        print("2. Añadir producto")
        print("3. Eliminar producto")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            añadir_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_productos():
    query = """
    SELECT p.Codigo_de_barras, p.Nombre, p.Precio_Unitario, p.Stock, c.Nombre AS Categoria, p.Descripcion
    FROM Productos p
    JOIN Categoria c ON p.ID_Categoria = c.ID_Categoria
    """
    productos = fetch_query(query)
    print("Productos:")
    for producto in productos:
        print(f"Codigo de Barras: {producto[0]}, Nombre: {producto[1]}, Precio Unitario: {producto[2]}, Stock: {producto[3]}, Categoría: {producto[4]}, Descripción: {producto[5]}")

def añadir_producto():
    codigo_de_barras = input("Ingrese el código de barras del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio_unitario = input("Ingrese el precio unitario del producto: ")
    stock = input("Ingrese el stock del producto: ")
    
    # Obtener y mostrar las categorías disponibles
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
    
    query = """
    INSERT INTO Productos (Codigo_de_barras, Nombre, Precio_Unitario, Stock, ID_Categoria, Descripcion)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (codigo_de_barras, nombre, precio_unitario, stock, id_categoria, descripcion)
    
    try:
        execute_query(query, params)
        print("Producto añadido correctamente.")
    except Exception as err:
        print(f"Error al añadir producto: {err}")

def eliminar_producto():
    codigo_de_barras = input("Ingrese el código de barras del producto a eliminar: ")
    
    # Verificar si el producto existe
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

# Ejemplo de uso
if __name__ == "__main__":
    gestionar_productos()
