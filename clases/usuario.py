class usuario:
    def __init__(self):
        self.__correo=''
        self.__contrasena=''
        self.__conectado=False


    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self,valor):
        self.__correo=valor

    @property
    def contrasena(self):
        return self.__contrasena
    @contrasena.setter
    def contrasena(self,valor):
        self.__contrasena=valor
    
    @property
    def conectado(self):
        return self.__conectado
    @conectado.setter
    def conectado(self,valor):
        self.__conectado=valor
    

    def __str__(self):
        if self.__conectado:
            estado='conectado'
        else :
            estado='desconectado'
        return f'usuario: {self.__correo} - contraseña: {self.__contrasena} - estado: {estado}'
