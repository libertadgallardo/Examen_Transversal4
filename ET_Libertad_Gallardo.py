

caracteristicas = ["Marca", "Pantalla (pulgadas)", "RAM", "Tipo de Disco", "Capacidad", "Procesador", "Tarjeta Gráfica"]

productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "2175HD": ["Acer", 14, "4GB", "SSD", "512GB", "Intel Core i7", "Nvidia GTX1050"],
    "fgdxFHD": ["HP", 15.6, "12GB", "DD", "1T", "Intel Core i5", "integrada"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i5", "Nvidia RTX2080Ti"],
    "GF75HD": ["Asus", 15.6, "12GB", "DD", "1T", "Intel Core i3", "Nvidia GTX1050"]
}

precio = {
    "8475HD": [387990],
    "2175HD": [327990],
    "JjfFHD": [424990],
    "fgdxFHD": [664990],
    "GF75HD": [749990]
}

unidades = {
    "8475HD": 10,
    "2175HD": 4,
    "JjfFHD": 1,
    "fgdxFHD": 21,
    "GF75HD": 2
}

def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1. Stock por marca")
    print("2. Búsqueda por precio")
    print("3. Listado de productos")
    print("4. Salir")

def stock_por_marca():
    marca = input("Ingrese la marca a buscar: ").capitalize()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0] == marca:
            print(f"Modelo: {modelo}, Unidades disponibles: {unidades[modelo]}")
            encontrados = True
    if not encontrados:
        print("No se encontraron productos de esa marca.")

def busqueda_por_precio():
    try:
        minimo = int(input("Ingrese el precio mínimo: "))
        maximo = int(input("Ingrese el precio máximo: "))
        encontrados = False
        print(f"\nProductos entre ${minimo} y ${maximo}:")
        for modelo, precio_modelo in precio.items():
            if minimo <= precio_modelo[0] <= maximo:
                print(f"Modelo: {modelo}, Precio: ${precio_modelo[0]}, Unidades: {unidades[modelo]}")
                encontrados = True
        if not encontrados:
            print("No se encontraron productos entre esos rangos de precio")
    except ValueError:
        print("Por favor, ingresa valores válidos")

def listar_productos():
    print("\nListado de todos los productos:")
    for modelo, datos in productos.items():
        info = ', '.join([f"{caracteristicas[i]}: {dato}" for i, dato in enumerate(datos)])
        print(f"Modelo: {modelo} -> {info}, Precio: ${precio[modelo][0]}, Unidades: {unidades[modelo]}")

# Bucle principal 
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        stock_por_marca()
    elif opcion == "2":
        busqueda_por_precio()
    elif opcion == "3":
        listar_productos()
    elif opcion == "4":
        print("Gracias por usar el sistema. ¡Nos vemos!")
        break
    else:
        print("Opción inválida")
