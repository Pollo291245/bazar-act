from clases.usuario import usuario
from clases.conexion import conexion
from os import system
import time
import hashlib
import sys


class usuariodao:
    def __init__(self, intentos):
        conexion.getconnection()
        self.__mysql = conexion()
        self.__intentos = intentos

    @property
    def mysql(self):
        return self.__mysql


    def encriptarcontrasena(self, contrasena):
        hashobject = hashlib.md5(contrasena.encode("utf-8"))
        contrasena = hashobject.hexdigest()
        return contrasena


    def buscarusuario(self, correo, contrasena):
        try:
            contrasena = self.encriptarcontrasena(contrasena)
            sentencia = "SELECT * FROM usuario WHERE correo=%s AND contrasena=%s"
            valores = (correo, contrasena)
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                return None
            else:
                us = usuario()
                us.correo = registro[0]
                us.contrasena = registro[1]
                us.conectado = False
                us.intentos = 3
                return us
        except Exception as e:
            print(f"el usuario ingresado no existe: {e}")

    def conectar(self, correo, contrasena):
        usuario = self.buscarusuario(correo,contrasena)
        if usuario is None:
            print("usuario o contraseña incorrectos")
            self.__intentos -= 1
            print(f"le quedan {self.__intentos} intentos")
            time.sleep(1)
            if self.__intentos == 0:
                print("se acabaron los intentos, cerrando el programa")
                time.sleep(1)
                sys.exit()
            time.sleep(1)
            return None
        elif usuario.conectado:
            print("el usuario ya esta conectado")
            time.sleep(1)
            return usuario
        else:
            print("conectando...")
            usuario.conectado = True
            time.sleep(2)
            return usuario

    def desconectar(self, us):
        if us is not None and us.conectado:
            us.conectado = False
            conexion.closeconnection()
        else:
            print("no se inicio sesion previamente")
            time.sleep(5)

    def crearusuario(self, correo, contrasena,rol_id,empleado_id):
        try:
            contrasena = self.encriptarcontrasena(contrasena)
            sentencia = "SELECT * FROM usuario WHERE correo=%s"
            valores = correo
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                sentencia = "INSERT INTO usuario (correo,contrasena,rol_id,empleado_id) VALUES(%s,%s,%s,%s)"
                valores = (correo, contrasena,rol_id,empleado_id)
                self.mysql.cursor.execute(sentencia, valores)
                self.mysql.connection.commit()
                return "usuario creado correctamente"
            else:
                return "el usuario ya existe"
        except Exception as e:
            return f"no se pudo insertar el usuario: {e}"
            time.sleep(5)

    def obt_rol_id(self, correo):
        try:
            sentencia = "SELECT rol_id FROM usuario WHERE correo=%s"
            valores = (correo,)
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                return None
            else:
                return registro[0]
        except Exception as e:
            print(f"error al buscar el rol: {e}")
            print("volviendo al menu principal")
            time.sleep(2)

    def obt_empleado_id(self, correo):
        try:
            sentencia = "SELECT empleado_id FROM usuario WHERE correo=%s"
            valores = (correo,)
            self.mysql.cursor.execute(sentencia, valores)
            registro = self.mysql.cursor.fetchone()
            if registro is None:
                return None
            else:
                return registro[0]
        except Exception as e:
            print(f"error al buscar el empleado: {e}")
            print("volviendo al menu principal")
            time.sleep(2)