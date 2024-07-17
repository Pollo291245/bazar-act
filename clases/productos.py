class productos:
    def __init__(self, nombre, codigo, precio):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"{self.__nombre} - {self.__codigo} - {self.__precio}"