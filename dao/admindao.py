from clases.conexion import conexion
from clases.empleado import empleado
from beautifultable import BeautifulTable
import time

class admindao:
    def __init__(self):
        conexion.getconnection()
        self.__mysql = conexion()

    @property
    def mysql(self):
        return self.__mysql

    def agregarempleado(self, empleado):
        try:
            sentencia = "SELECT * FROM empleado WHERE rut=%s"
            valores = empleado.rut
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                sentencia = "INSERT INTO empleado(nombre,rut,cargo,fecha_ingreso,sueldo) VALUES(%s,%s,%s,%s,%s)"
                valores = (
                    empleado.nombre,
                    empleado.rut,
                    empleado.cargo,
                    empleado.fecha_ingreso,
                    empleado.sueldo,
                )
                self.mysql.cursor.execute(sentencia, valores)
                self.mysql.connection.commit()
                return "empleado insertado correctamente"
            else:
                return "el empleado ya existe"
        except Exception as e:
            return f"no se pudo insertar el empleado: {e}"
            time.sleep(5)
            
    def eliminarempleado(self, id):
        try:
            sentencia = "SELECT * FROM empleado WHERE id=%s"
            valores = id
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                return "el empleado no existe"
            else:
                sentencia = 'DELETE FROM usuario WHERE empleado_id=%s'
                self.mysql.cursor.execute(sentencia, (id,))
                self.mysql.connection.commit()
                sentencia = "DELETE FROM empleado WHERE id=%s"
                self.mysql.cursor.execute(sentencia, (id,))
                self.mysql.connection.commit()
                return "empleado eliminado correctamente"
        except Exception as e:
            return f"no se pudo eliminar el empleado: {e}"
            time.sleep(5)

    def actualizarempleado(self, empleado):
        try:
            sentencia = "SELECT * FROM empleado WHERE rut=%s"
            valores = empleado.rut
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                return "el empleado no existe"
            else:
                sentencia = "UPDATE empleado SET nombre=%s,cargo=%s,fecha_ingreso=%s,sueldo=%s WHERE rut=%s"
                valores = (
                    empleado.nombre,
                    empleado.cargo,
                    empleado.fecha_ingreso,
                    empleado.sueldo,
                    empleado.rut,
                )
                self.mysql.cursor.execute(sentencia, valores)
                self.mysql.connection.commit()
                return "empleado actualizado correctamente"
        except Exception as e:
            return f"no se pudo actualizar el empleado: {e}"
            time.sleep(5)

            
    def listarempleado(self):
        try:
            tabla=BeautifulTable()
            tabla.column_headers=['id','nombre','rut','cargo','fecha de ingreso','sueldo']
            sentencia='SELECT * FROM empleado'
            self.mysql.cursor.execute(sentencia)
            rows=self.mysql.cursor.fetchall()
            for row in rows:
                tabla.append_row(row)
            if len(tabla.rows)>0:
                print(tabla)
            else:
                print('no hay empleados registrados')
                print('volviendo al menu principal')
                time.sleep(2)
        except Exception as e:
            print(f'error al obtener los empleados: {e}')
            print('volviendo al menu principal')
        time.sleep(2)

    def buscarempleado(self, rut):
        try:
            sentencia = "SELECT * FROM empleado WHERE rut=%s"
            valores = rut
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                return "el empleado no existe"
            else:
                emp = empleado(
                    registro[0], registro[1], registro[2], registro[3], registro[4]
                )
                return emp
        except Exception as e:
            return f"no se pudo buscar el empleado: {e}"
            time.sleep(5)