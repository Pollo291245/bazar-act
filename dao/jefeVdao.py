from clases.conexion import conexion
from clases.empleado import empleado
from clases.productos import productos
from beautifultable import BeautifulTable
import time

class jefeVdao:
    def __init__(self):
        conexion.getconnection()
        self.__mysql = conexion()
        
    @property
    def mysql(self):
        return self.__mysql
    
    def agregarProducto(self, producto):
        try:
            sentencia = "INSERT INTO producto(nombre,codigo,precio) VALUES(%s,%s,%s)"
            valores = (
                producto.nombre,
                producto.codigo,
                producto.precio,
            )
            self.mysql.cursor.execute(sentencia, valores)
            self.mysql.connection.commit()
            return "producto insertado correctamente"
        except Exception as e:
            return f"no se pudo insertar el producto: {e}"
            time.sleep(5)
            
    def ver_carrito(self):
        try:
            sentencia = "SELECT * FROM Carrito"
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if registros is None:
                return "No hay productos en el carrito"
            else:
                for registro in registros:
                    print(registro)
        except Exception as e:
            return f"No se pudo mostrar el carrito: {e}"
            time.sleep(5)
            
            
    def ver_ventas(self):
        try:
            sentencia = "SELECT * FROM venta"
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if not registros:
                return "No hay ventas"
            else:
                tabla = BeautifulTable()
                tabla.columns.header = ["ID", "Cantidad Productos", "Total Venta", "Tipo Venta", "Empleado ID"]
                for registro in registros:
                    tabla.rows.append(registro)
                print(tabla)
        except Exception as e:
            return f"No se pudo mostrar las ventas: {e}"

    def ventas_boleta(self):
        try:
            sentencia = "SELECT * FROM venta WHERE tipo_venta='boleta'"
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if not registros:
                return "No hay ventas"
            else:
                tabla = BeautifulTable()
                tabla.columns.header = ["ID", "Cantidad Productos", "Total Venta", "Tipo Venta", "Empleado ID"]
                for registro in registros:
                    tabla.rows.append(registro)
                print(tabla)
        except Exception as e:
            return f"No se pudo mostrar las ventas: {e}"

    def ventas_factura(self):
        try:
            sentencia = "SELECT * FROM venta WHERE tipo_venta='factura'"
            self.mysql.cursor.execute(sentencia)
            registros = self.mysql.cursor.fetchall()
            if not registros:
                return "No hay ventas"
            else:
                tabla = BeautifulTable()
                tabla.columns.header = ["ID", "Cantidad Productos", "Total Venta", "Tipo Venta", "Empleado ID"]
                for registro in registros:
                    tabla.rows.append(registro)
                print(tabla)
        except Exception as e:
            return f"No se pudo mostrar las ventas: {e}"