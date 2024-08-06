import diccionario_productos


class ListaProductos:
    def __init__(self, productos, precios, stock):
        self.productos = productos
        self.precios = precios
        self.stock = stock

    def mostrar_lista_productos(self):
        print("========================================")
        print("Lista de Productos:")
        print("========================================")

        for cod in self.productos:
            print(f"{cod} \t {self.productos[cod]} \t {self.precios[cod]} \t {self.stock[cod]}")

        print("========================================")

        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")

    def agregar_producto(self):
        cod = int(input("Ingrese el código del nuevo producto: "))
        nombre = input("Ingrese el nombre del nuevo producto: ")
        precio = float(input("Ingrese el precio del nuevo producto: "))
        stock = int(input("Ingrese el stock del nuevo producto: "))

        self.productos[cod] = nombre
        self.precios[cod] = precio
        self.stock[cod] = stock
        print("Producto agregado exitosamente!")

    def eliminar_producto(self):
        cod = int(input("Ingrese el código del producto a eliminar: "))

        if cod in self.productos:
            del self.productos[cod]
            del self.precios[cod]
            del self.stock[cod]
            print("Producto eliminado exitosamente!")
        else:
            print("El código del producto no existe.")

    def actualizar_producto(self):
        cod = int(input("Ingrese el código del producto a actualizar: "))

        if cod in self.productos:
            nombre = input(f"Ingrese el nuevo nombre del producto (anterior: {self.productos[cod]}): ")
            precio = float(input(f"Ingrese el nuevo precio del producto (anterior: {self.precios[cod]}): "))
            stock = int(input(f"Ingrese el nuevo stock del producto (anterior: {self.stock[cod]}): "))

            self.productos[cod] = nombre
            self.precios[cod] = precio
            self.stock[cod] = stock
            print("Producto actualizado exitosamente!")
        else:
            print("El código del producto no existe.")

    def gestionar_productos(self):
        while True:
            self.mostrar_lista_productos()
            opcion = input("Elija opción: ")
            if opcion == '1':
                self.agregar_producto()
            elif opcion == '2':
                self.eliminar_producto()
            elif opcion == '3':
                self.actualizar_producto()
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente nuevamente.")


lista_productos = ListaProductos(
    diccionario_productos.productos,
    diccionario_productos.precios,
    diccionario_productos.stock
)

lista_productos.gestionar_productos()
