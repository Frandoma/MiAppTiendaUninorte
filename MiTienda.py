class TiendaProductos:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

def mostrar_menu(productos):
    print("TIENDA APP_TECNOLOGY")
    print("LISTADO DE PRODUCTOS:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto.nombre} - ${producto.precio}")

def calcular_total(carrito):
    total = sum(producto.precio * cantidad for producto, cantidad in carrito.items())
    return total

def main():
    teclados = TiendaProductos("TECLADO", 78000, "Teclado ASUS")
    portatil = TiendaProductos("PORTATIL", 25000000, "Portatil ideapad5 acer")
    impresora = TiendaProductos("IMPRESORA", 890000, "Impresora EPSON 9015")
    celular = TiendaProductos("CELULAR", 590000, "Celular motorola moto e30 ")
    mac= TiendaProductos("IPHONE", 3200000, "Celular iPhone 13 Pro")

    productos = [teclados, portatil, impresora, celular, mac]
    carrito = {}

    mostrar_menu(productos)

    while True:
        try:
            seleccion = int(input("Seleccione un producto - 0 para finalizar: "))
            if seleccion == 0:
                break
            elif 1 <= seleccion <= len(productos):
                cantidad = int(input(f"Ingrese la cantidad de {productos[seleccion - 1].nombre} que desea comprar: "))
                carrito[productos[seleccion - 1]] = carrito.get(productos[seleccion - 1], 0) + cantidad
            else:
                print("Selección inválida.")
        except ValueError:
            print("Ingrese un número válido.")

    if not carrito:
        print("No se han seleccionado productos.")
        return

    print("\nResumen del pedido:")
    for producto, cantidad in carrito.items():
        print(f"{producto.nombre} - Cantidad: {cantidad} - Subtotal: ${producto.precio * cantidad}")
    
    total = calcular_total(carrito)
    print(f"Total a pagar: ${total}")

    aprobar_pedido = input("¿Desea aprobar el pedido? (si/no): ").lower()
    if aprobar_pedido == "si":
        print("\nCompra aprobada.")
        print("\nResumen de la compra:")
        for producto, cantidad in carrito.items():
            print(f"{producto.nombre} - Cantidad: {cantidad} - Subtotal: ${producto.precio * cantidad}")
        print(f"Total pagado: ${total}")
    else:
        print("\nPedido cancelado.")

if __name__ == "__main__":
    main()