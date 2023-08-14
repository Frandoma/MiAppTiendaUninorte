class TiendaProductos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

def mostrar_menu(productos):
    
    print("Productos disponibles:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto.nombre} - ${producto.precio}")

def calcular_total(carrito):
    total = sum(producto.precio * cantidad for producto, cantidad in carrito.items())
    return total

