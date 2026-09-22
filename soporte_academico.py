def mostrar_menu():
    """Muestra el menú principal del sistema de soporte académico."""
    print("\n" + "=" * 45)
    print("   SISTEMA DE SOPORTE ACADÉMICO")
    print("=" * 45)
    print("1. Registrar solicitud")
    print("2. Mostrar solicitudes")
    print("3. Salir")
    print("=" * 45)


def validar_texto(texto):
    texto_limpio = texto.strip()
    return texto_limpio != ""


def validar_codigo(codigo):
    codigo_limpio = codigo.strip()
    return codigo_limpio != "" and len(codigo_limpio) >= 8


def obtener_tipos_consulta():
    return ("matrícula", "pagos", "constancia", "plataforma", "otro")


def validar_tipo_consulta(tipo):
    tipo_limpio = tipo.strip().lower()
    return tipo_limpio in obtener_tipos_consulta()


def asignar_prioridad(tipo):
    tipo_limpio = tipo.strip().lower()

    # Regla definida para el sistema:
    # matrícula y pagos = ALTA
    # constancia, plataforma y otro = BAJA

    tipos_prioridad_alta = ("matrícula", "pagos")

    if tipo_limpio in tipos_prioridad_alta: 
        return "ALTA"
    else:
        return "BAJA"


def registrar_solicitud(solicitudes):
    print("\n--- REGISTRO DE SOLICITUD ---")
    print("Ingrese los datos básicos de la solicitud.")

    codigo = input("Código del estudiante: ")

    if not validar_codigo(codigo):
        if codigo.strip() == "":
            print("Error: el código no puede estar vacío.")
        else:
            print("Error: el código debe tener al menos 8 caracteres.")
        return None

    nombre = input("Nombre del estudiante: ")

    if not validar_texto(nombre):
        print("Error: el nombre no puede estar vacío.")
        return None

    print("\nTipos de consulta disponibles:")

    for i, tipo_disponible in enumerate(obtener_tipos_consulta(), start=1):
        print(f"{i}. {tipo_disponible}")

    tipo = input("Tipo de consulta: ").strip().lower()

    if not validar_tipo_consulta(tipo):
        print("Error: tipo de consulta no válido.")
        return None

    descripcion = input("Descripción breve: ")

    if not validar_texto(descripcion):
        print("Error: la descripción no puede estar vacía.")
        return None

    prioridad = asignar_prioridad(tipo)

    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo,
        "descripcion": descripcion.strip(),
        "prioridad": prioridad
    }

    solicitudes.append(solicitud)

    print("\nSolicitud registrada correctamente.")
    print(f"Prioridad asignada: {prioridad}")

    return solicitud


def mostrar_resumen(solicitud):
    print("\n--- RESUMEN DE SOLICITUD ---")
    print(f"Código: {solicitud['codigo']}")
    print(f"Nombre: {solicitud['nombre']}")
    print(f"Tipo de consulta: {solicitud['tipo']}")
    print(f"Descripción: {solicitud['descripcion']}")
    print(f"Prioridad: {solicitud['prioridad']}")


def mostrar_solicitudes(solicitudes):
    if len(solicitudes) == 0:
        print("\nNo existen solicitudes registradas.")
        return

    print("\n" + "=" * 45)
    print("       SOLICITUDES REGISTRADAS")
    print("=" * 45)

    for i, solicitud in enumerate(solicitudes, start=1):
        print(f"\nSolicitud #{i}")
        print(f"Código: {solicitud['codigo']}")
        print(f"Nombre: {solicitud['nombre']}")
        print(f"Tipo: {solicitud['tipo']}")
        print(f"Descripción: {solicitud['descripcion']}")
        print(f"Prioridad: {solicitud['prioridad']}")


def main():
    solicitudes = []

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            solicitud = registrar_solicitud(solicitudes)

            if solicitud is not None:
                mostrar_resumen(solicitud)

        elif opcion == "2":
            mostrar_solicitudes(solicitudes)

        elif opcion == "3":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nError: opción no válida.")


if __name__ == "__main__":
    main()
    