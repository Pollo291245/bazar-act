class empleado:
    def __init__(self, nombre, rut, cargo, fecha_ingreso, sueldo):
        self.nombre = nombre
        self.rut = rut
        self.cargo = cargo
        self.fecha_ingreso = fecha_ingreso
        self.sueldo = sueldo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def rut(self):
        return self._rut

    @rut.setter
    def rut(self, rut):
        self._rut = rut

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def fecha_ingreso(self):
        return self._fecha_ingreso

    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
