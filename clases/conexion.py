import pymysql

class conexion:
    connection = None
    cursor = None

    def __init__(self):
        pass

    @classmethod
    def getconnection(cls):
        if cls.connection is None:
            conex = pymysql.connect(
                host="localhost", port=3306, user="root", password="", db="sistemabazar"
            )
            cls.cursor = conex.cursor()
            cls.connection = conex

    @classmethod
    def closeconnection(cls):
        try:
            if cls.connection is not None:
                if cls.connection.open:
                    cls.connection.close()
                    print("conexion cerrada")
                else:
                    print("conexion no abierta")
            else:
                print("conexion no establecida")
        except pymysql.error as e:
            print(f"error al cerrar la conexion: {e}")
        finally:
            cls.connection = None
            cls.cursor = None
