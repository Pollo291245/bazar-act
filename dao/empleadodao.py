from clases.conexion import conexion
from clases.empleado import empleado
from clases.productos import productos
from beautifultable import BeautifulTable
from dao.factura import Factura
import time


class empleadodao:
    def __init__(self):
        conexion.getconnection()
        self.__mysql = conexion()

    @property
    def mysql(self):
        return self.__mysql
    
    def agregar_carrito_id(self, producto_id, cantidad):
        try:
            sentencia_producto = "SELECT * FROM producto WHERE id=%s"
            valores_producto = (producto_id,)
            self.mysql.cursor.execute(sentencia_producto, valores_producto)
            registro = self.mysql.cursor.fetchone()

            if registro is None:
                return "El producto no existe"
            else:
                cant=(cantidad)
                total=registro[3]*cantidad
                carr=productos(registro[1],registro[2],registro[3])
                sentencia_carrito = """
                INSERT INTO Carrito (producto_id, cantidad, total_por_producto)
                VALUES (%s, %s, %s)
                """
                valores_carrito = (producto_id, cant, total)
                self.mysql.cursor.execute(sentencia_carrito, valores_carrito)
                self.mysql.connection.commit()

                return f"{carr}\nProducto agregado al carrito correctamente\nPrecio total: {total}"
        except Exception as e:
            return f"No se pudo agregar el producto al carrito: {e}"




    def mostrar_carrito(self):
        try:
            sentencia = """
            SELECT p.nombre, p.precio, c.cantidad, c.total_por_producto
            FROM Carrito c
            INNER JOIN Producto p ON c.producto_id = p.id
            """
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if registros is None or len(registros) == 0:
                return "No hay productos en el carrito"
            else:
                tabla = BeautifulTable()
                tabla.columns.header = ["Nombre", "Precio", "Cantidad", "Total por Producto"]
                for registro in registros:
                    nombre = registro[0]
                    precio = registro[1]
                    cantidad = registro[2]
                    total_por_producto = registro[3]
                    tabla.rows.append([nombre, precio, cantidad, total_por_producto])
                print(tabla)
        except Exception as e:
            print (f"No se pudo mostrar el carrito: {e}")  
            
            
            
            
    def mostrar_productos(self):
        try:
            sentencia = "SELECT * FROM producto"
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if registros is None or len(registros) == 0:
                return "No hay productos"
            else:
                tabla = BeautifulTable()
                tabla.columns.header = ["ID", "Nombre", "Codigo", "Precio"]
                for registro in registros:
                    id = registro[0]
                    nombre = registro[1]
                    codigo = registro[2]
                    precio = registro[3]
                    tabla.rows.append([id, nombre, codigo, precio])
                print(tabla)
        except Exception as e:
            print(f"No se pudo mostrar los productos: {e}")
            
            
            
    
    def vaciar_carrito(self):
        try:
            sentencia = "Delete From carrito"
            self.mysql.cursor.execute(sentencia)
            self.mysql.connection.commit()
            return f"Carrito vaciado correctamente"
        except Exception as e:
            return f"no se pudo vaciar el carrito"
        
        
        
        
    def generar_venta(self,id_empleado_actual, tipo_venta):
        try:
            sentencia = "SELECT * FROM carrito"
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if registros is None or len(registros) == 0:
                return "No hay productos en el carrito"
            else:
                total_producto = 0
                for registro in registros:
                    total_producto += registro[3]
                iva = total_producto * 0.19
                total = total_producto + iva
                
                if tipo_venta == 1:
                    tipo_venta = "boleta"
                elif tipo_venta == 2:
                    tipo_venta = "factura"
                else:
                    return "Tipo de venta no válido"

                sentencia = "INSERT INTO venta (cantidad_productos, total_venta, tipo_venta, empleado_id) VALUES (%s, %s, %s, %s)"
                valores = (len(registros), total, tipo_venta, id_empleado_actual)
                self.mysql.cursor.execute(sentencia, valores)
                self.mysql.connection.commit()
                
                return f"Venta generada correctamente, total: {total_producto} con iva: {total}"
            
        except Exception as e:
            time.sleep(5)
            return f"No se pudo generar la venta: {e}"




    def generar_boleta(self):
        try:
            sentencia_venta = "SELECT * FROM venta ORDER BY ID DESC LIMIT 1"
            self.mysql.cursor.execute(sentencia_venta)
            registro_venta = self.mysql.cursor.fetchone()

            if registro_venta is None:
                return "No hay ventas"
            id_venta, cantidad_productos, total_venta, tipo_venta, empleado_id = registro_venta

            sentencia_carrito = """
            SELECT p.nombre, p.precio, c.cantidad, c.total_por_producto
            FROM carrito c
            INNER JOIN producto p ON c.producto_id = p.id
            """
            self.mysql.cursor.execute(sentencia_carrito)
            productos_carrito = self.mysql.cursor.fetchall()

            if not productos_carrito:
                return "No hay productos en el carrito"

            tabla = BeautifulTable()
            tabla.columns.header = ["Producto", "Cantidad", "Precio", "Total por Producto", "Total de la Venta", "Tipo de Venta", "Empleado ID"]
            
            for producto in productos_carrito:
                nombre, precio, cantidad, total_por_producto = producto
                tabla.rows.append([nombre, cantidad, precio, total_por_producto, total_venta, tipo_venta, empleado_id])

            print(tabla)

        except Exception as e:
            return f"No se pudo generar la boleta: {e}"
                        
            
            
        
    def ver_ventas(self):
        try:
            sentencia = "SELECT * FROM venta"
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if registros is None:
                return "No hay ventas"
            else:
                for registro in registros:
                    print(registro)
        except Exception as e:
            return f"No se pudo mostrar las ventas: {e}"
            time.sleep(5)    




    def generar_factura(self):
        try:
            sentencia = "SELECT * FROM venta ORDER BY ID DESC LIMIT 1"
            self.mysql.cursor.execute(sentencia)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                return "No hay ventas"
            else:
                tabla = BeautifulTable()
                tabla.columns.header = ["ID", "Cantidad Productos", "Total Venta", "Tipo Venta", "Empleado ID"]
                id = registro[0]
                cantidad_productos = registro[1]
                total_venta = registro[2]
                tipo_venta = registro[3]
                empleado_id = registro[4]
                tabla.rows.append([id, cantidad_productos, total_venta, tipo_venta, empleado_id])
                print(tabla)
                
                if tipo_venta == "factura":
                    factura = Factura()
                    sentencia = "SELECT * FROM carrito"
                    self.mysql.cursor.execute(sentencia)
                    registros = self.mysql.cursor.fetchall()
                    if registros is None or len(registros) == 0:
                        return "No hay productos en el carrito"
                    else:
                        for registro in registros:
                            nombre = registro[2]
                            precio = registro[3]
                            factura.agregar_producto(nombre, precio)
                    
                    return factura.generar_factura()
        except Exception as e:
            return f"No se pudo generar la factura: {e}"
            time.sleep(5)
        
        
    