# --- ESTRUCTURA DE DATOS ---
inventario = []

# --- FUNCIONES (Partes modulares) ---

def agregar_producto():
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Nombre del producto: ")
    
    # Validación simple de números
    try:
        precio = float(input("Precio: "))
        stock = int(input("Cantidad en stock: "))
        
        # Guardamos la información en un diccionario
        producto = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }
        inventario.append(producto)
        print(f"✅ {nombre} agregado con éxito.")
    except ValueError:
        print("❌ Error: El precio y el stock deben ser números.")

def mostrar_inventario():
    print("\n--- Lista de Productos ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for p in inventario:
            # Uso de f-strings para mostrar datos
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}")

def calcular_valor_total():
    total = 0
    for p in inventario:
        total += p['precio'] * p['stock']
    print(f"\n💰 El valor total de la mercadería es: ${total}")

# --- MENÚ PRINCIPAL (Estructura de control) ---

def menu():
    while True:
        print("\n********** SISTEMA DE GESTIÓN **********")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Calcular valor total")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_valor_total()
        elif opcion == "4":
            print("Saliendo del sistema... ¡Adiós!")
            break
        else:
            print("❌ Opción no válida, intente de nuevo.")

# Iniciar el programa
menu()
