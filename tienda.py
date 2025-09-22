class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print(" El precio y la cantidad deben ser valores positivos.")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                print(" El producto ya existe en el inventario.")
                return

        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        self.productos.append(nuevo_producto)
        print(f" Producto '{nombre}' agregado correctamente.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad <= 0:
                    print(" La cantidad debe ser positiva.")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f" Venta realizada: {cantidad} unidad(es) de '{nombre}'.")
                else:
                    print(" No hay suficiente stock para realizar la venta.")
                return
        print(" El producto no existe en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print(" El inventario está vacío.")
            return
        print(f"\n Inventario de '{self.nombre_tienda}':")
        for producto in self.productos:
            print(f"- {producto['nombre']}: ${producto['precio']} | Stock: {producto['cantidad']}")
        print()

    def producto_mas_caro(self):
        if not self.productos:
            print(" No hay productos en el inventario.")
            return
        producto_caro = max(self.productos, key=lambda p: p["precio"])
        print(f" Producto más caro: {producto_caro['nombre']} (${producto_caro['precio']})\n")

def menu():
    nombre = input(" Ingresa el nombre de la tienda: ")
    tienda = InventarioTienda(nombre)

    while True:
        print("\n Menú de Inventario ")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto más caro")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_prod = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad en stock: "))
                tienda.agregar_producto(nombre_prod, precio, cantidad)
            except ValueError:
                print(" Entrada inválida. Usa números para precio y cantidad.")

        elif opcion == "2":
            nombre_prod = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                tienda.vender_producto(nombre_prod, cantidad)
            except ValueError:
                print(" Entrada inválida. Usa un número entero para la cantidad.")

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            tienda.producto_mas_caro()

        elif opcion == "5":
            print(" Gracias por usar el sistema de inventario.")
            break

        else:
            print(" Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
