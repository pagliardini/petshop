from db import execute_query, fetch_query


def gestionar_empleados():
    while True:
        print("Gestionando empleados")
        print("1. Mostrar empleados")
        print("2. Añadir empleado")
        print("3. Eliminar empleado")
        print("4. Actualizar empleado")
        print("5. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_empleados()
        elif opcion == "2":
            añadir_empleado()
        elif opcion == "3":
            eliminar_empleado()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def mostrar_empleados():
    query = "SELECT CUIL_Empleado, Nombre, Apellido, Telefono, Email, Direccion, ID_Sucursal FROM Empleados"
    empleados = fetch_query(query)
    print("Empleados:")
    for empleado in empleados:
        print(
            f"CUIL: {empleado[0]}, Nombre: {empleado[1]}, Apellido: {empleado[2]}, Teléfono: {empleado[3]}, Email: {empleado[4]}, Dirección: {empleado[5]}, ID Sucursal: {empleado[6]}")


def añadir_empleado():
    cuil_empleado = input("Ingrese el CUIL del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    email = input("Ingrese el email del empleado: ")
    direccion = input("Ingrese la dirección del empleado (opcional): ")
    id_sucursal = input("Ingrese el ID de la sucursal: ")

    query = """
    INSERT INTO Empleados (CUIL_Empleado, Nombre, Apellido, Telefono, Email, Direccion, ID_Sucursal)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (cuil_empleado, nombre, apellido, telefono, email, direccion, id_sucursal)

    try:
        execute_query(query, params)
        print("Empleado añadido correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al añadir empleado: {err}")


def eliminar_empleado():
    cuil_empleado = input("Ingrese el CUIL del empleado a eliminar: ")

    # Verificar si el empleado existe
    query_check = "SELECT COUNT(*) FROM Empleados WHERE CUIL_Empleado = %s"
    params_check = (cuil_empleado,)
    empleado_existe = fetch_query(query_check, params_check)[0][0]

    if empleado_existe == 0:
        print("Error: El empleado con el CUIL especificado no existe.")
        return

    query = "DELETE FROM Empleados WHERE CUIL_Empleado = %s"
    params = (cuil_empleado,)

    try:
        execute_query(query, params)
        print("Empleado eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar empleado: {err}")


def actualizar_empleado():
    cuil_empleado = input("Ingrese el CUIL del empleado a actualizar: ")

    # Verificar si el empleado existe
    query_check = "SELECT COUNT(*) FROM Empleados WHERE CUIL_Empleado = %s"
    params_check = (cuil_empleado,)
    empleado_existe = fetch_query(query_check, params_check)[0][0]

    if empleado_existe == 0:
        print("Error: El empleado con el CUIL especificado no existe.")
        return

    nombre = input("Ingrese el nuevo nombre del empleado (dejar en blanco para no cambiar): ")
    apellido = input("Ingrese el nuevo apellido del empleado (dejar en blanco para no cambiar): ")
    telefono = input("Ingrese el nuevo teléfono del empleado (dejar en blanco para no cambiar): ")
    email = input("Ingrese el nuevo email del empleado (dejar en blanco para no cambiar): ")
    direccion = input("Ingrese la nueva dirección del empleado (dejar en blanco para no cambiar): ")
    id_sucursal = input("Ingrese el nuevo ID de la sucursal (dejar en blanco para no cambiar): ")

    query = "UPDATE Empleados SET "
    params = []
    if nombre:
        query += "Nombre = %s, "
        params.append(nombre)
    if apellido:
        query += "Apellido = %s, "
        params.append(apellido)
    if telefono:
        query += "Telefono = %s, "
        params.append(telefono)
    if email:
        query += "Email = %s, "
        params.append(email)
    if direccion:
        query += "Direccion = %s, "
        params.append(direccion)
    if id_sucursal:
        query += "ID_Sucursal = %s, "
        params.append(id_sucursal)

    if not params:
        print("No se ha actualizado ningún campo.")
        return

    query = query.rstrip(", ")
    query += " WHERE CUIL_Empleado = %s"
    params.append(cuil_empleado)

    try:
        execute_query(query, tuple(params))
        print("Empleado actualizado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar empleado: {err}")


# Ejemplo de uso
if __name__ == "__main__":
    gestionar_empleados()
