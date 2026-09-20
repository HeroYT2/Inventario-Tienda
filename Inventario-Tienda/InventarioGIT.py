# inventario.py
# Sistema de inventario con actualización y total

inventario = {}

def agregar_producto(nombre, precio, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Use la opción actualizar stock.")
        return
    inventario[nombre] = {
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    print(f"Producto '{nombre}' agregado correctamente.")

def actualizar_stock(nombre, nueva_cantidad):
    if nombre in inventario:
        inventario[nombre]["cantidad"] = int(nueva_cantidad)
        print(f"Stock de '{nombre}' actualizado a {nueva_cantidad}.")
    else:
        print(f"El producto '{nombre}' no existe.")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n--- INVENTARIO ACTUAL ---")
    total_general = 0
    for nombre, datos in inventario.items():
        subtotal = datos["precio"] * datos["cantidad"]
        total_general += subtotal
        print(f"{nombre}: precio=${datos['precio']:.2f}, "
              f"stock={datos['cantidad']}, subtotal=${subtotal:.2f}")
    print(f"Valor total del inventario: ${total_general:.2f}")

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print(f"El producto '{nombre}' no existe.")

def main():
    print("=== SISTEMA DE INVENTARIO ===")
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Mostrar inventario total")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = input("Precio: ")
            cantidad = input("Cantidad en stock: ")
            agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad en stock: ")
            actualizar_stock(nombre, nueva_cantidad)
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
