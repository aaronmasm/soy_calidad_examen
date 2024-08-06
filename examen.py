import diccionario_productos


class ListaProductos:
    def __init__(self, productos, precios, stock):
        # Inicializa los diccionarios de productos, precios y stock
        self.productos = productos
        self.precios = precios
        self.stock = stock

    def mostrar_lista_productos(self):
        # Muestra la lista de productos en un formato tabular
        print("========================================")
        print("Lista de Productos:")
        print("========================================")

        # Imprime cada producto con su código, nombre, precio y stock
        for cod in self.productos:
            print(f"{cod} \t {self.productos[cod]} \t {self.precios[cod]} \t {self.stock[cod]}")

        print("========================================")

        # Opciones disponibles para el usuario
        print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")

    def agregar_producto(self):
        # Solicita al usuario los datos del nuevo producto y lo agrega a los diccionarios
        cod = int(input("Ingrese el código del nuevo producto: "))
        nombre = input("Ingrese el nombre del nuevo producto: ")
        precio = float(input("Ingrese el precio del nuevo producto: "))
        stock = int(input("Ingrese el stock del nuevo producto: "))

        # Agrega el nuevo producto a los diccionarios
        self.productos[cod] = nombre
        self.precios[cod] = precio
        self.stock[cod] = stock
        print("Producto agregado exitosamente!")

    def eliminar_producto(self):
        # Solicita al usuario el código del producto a eliminar y lo elimina de los diccionarios
        cod = int(input("Ingrese el código del producto a eliminar: "))

        if cod in self.productos:
            # Elimina el producto de los diccionarios si el código existe
            del self.productos[cod]
            del self.precios[cod]
            del self.stock[cod]
            print("Producto eliminado exitosamente!")
        else:
            # Mensaje si el código del producto no existe
            print("El código del producto no existe.")

    def actualizar_producto(self):
        # Solicita al usuario el código del producto a actualizar y sus nuevos datos
        cod = int(input("Ingrese el código del producto a actualizar: "))

        if cod in self.productos:
            # Actualiza los datos del producto si el código existe
            nombre = input(f"Ingrese el nuevo nombre del producto (anterior: {self.productos[cod]}): ")
            precio = float(input(f"Ingrese el nuevo precio del producto (anterior: {self.precios[cod]}): "))
            stock = int(input(f"Ingrese el nuevo stock del producto (anterior: {self.stock[cod]}): "))

            self.productos[cod] = nombre
            self.precios[cod] = precio
            self.stock[cod] = stock
            print("Producto actualizado exitosamente!")
        else:
            # Mensaje si el código del producto no existe
            print("El código del producto no existe.")

    def gestionar_productos(self):
        # Bucle para gestionar los productos hasta que el usuario decida salir
        while True:
            self.mostrar_lista_productos()
            opcion = input("Elija opción: ")
            if opcion == '1':
                # Llama al método para agregar un producto
                self.agregar_producto()
            elif opcion == '2':
                # Llama al método para eliminar un producto
                self.eliminar_producto()
            elif opcion == '3':
                # Llama al método para actualizar un producto
                self.actualizar_producto()
            elif opcion == '4':
                # Sale del bucle y termina el programa
                print("Saliendo...")
                break
            else:
                # Mensaje si la opción ingresada no es válida
                print("Opción no válida, intente nuevamente.")


# Crea una instancia de ListaProductos usando los diccionarios importados
lista_productos = ListaProductos(
    diccionario_productos.productos,
    diccionario_productos.precios,
    diccionario_productos.stock
)

# Llama al método para gestionar los productos
lista_productos.gestionar_productos()
