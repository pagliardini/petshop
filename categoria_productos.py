from db import execute_query, fetch_query

def gestionar_categorias():
    while True:
        print("Gestionando categorías de productos")
        print("1. Mostrar categorías")
        print("2. Añadir categoría")
        print("3. Eliminar categoría")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_categorias()
        elif opcion == "2":
            añadir_categoria()
        elif opcion == "3":
            eliminar_categoria()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_categorias():
    query = "SELECT ID_Categoria, Nombre, Descripcion FROM Categoria"
    categorias = fetch_query(query)
    print("Categorías:")
    for categoria in categorias:
        print(f"ID: {categoria[0]}, Nombre: {categoria[1]}, Descripción: {categoria[2]}")

def añadir_categoria():
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría (opcional): ")
    
    query = """
    INSERT INTO Categoria (Nombre, Descripcion)
    VALUES (%s, %s)
    """
    params = (nombre, descripcion)
    
    try:
        execute_query(query, params)
        print("Categoría añadida correctamente.")
    except Exception as err:
        print(f"Error al añadir categoría: {err}")

def eliminar_categoria():
    id_categoria = input("Ingrese el ID de la categoría a eliminar: ")
    
    # Verificar si la categoría existe
    query_check = "SELECT COUNT(*) FROM Categoria WHERE ID_Categoria = %s"
    params_check = (id_categoria,)
    categoria_existe = fetch_query(query_check, params_check)[0][0]

    if categoria_existe == 0:
        print("Error: La categoría con el ID especificado no existe.")
        return
    
    query = "DELETE FROM Categoria WHERE ID_Categoria = %s"
    params = (id_categoria,)
    
    try:
        execute_query(query, params)
        print("Categoría eliminada correctamente.")
    except Exception as err:
        print(f"Error al eliminar categoría: {err}")

# Ejemplo de uso
if __name__ == "__main__":
    gestionar_categorias()
