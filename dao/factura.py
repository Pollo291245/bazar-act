class Factura:
    def __init__(self):
        self.razon_social = input("Ingrese la razón social del cliente: ")
        self.rut = input("Ingrese el RUT del cliente: ")
        self.giro = input("Ingrese el giro del cliente: ")
        self.direccion = input("Ingrese la dirección del cliente: ")
        self.productos = []  # Lista para almacenar los productos

    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))

    def generar_factura(self):
        total_neto = sum(precio for _, precio in self.productos)
        iva = total_neto * 0.19
        total_final = total_neto + iva

        factura = f"""
        Razón Social: {self.razon_social}
        RUT: {self.rut}
        Giro: {self.giro}
        Dirección: {self.direccion}
        Detalle de Productos:
        """
        for nombre, precio in self.productos:
            factura += f"\n- {nombre}: ${precio}"
        factura += f"\nTotal Neto: ${total_neto}\nIVA (19%): ${iva}\nTotal Final: ${total_final}"
        
        return factura
