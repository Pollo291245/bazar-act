from dao.usuariodao import usuariodao
from clases.usuario import usuario
from clases.empleado import empleado
from dao.empleadodao import empleadodao
from dao.admindao import admindao
from dao.jefeVdao import jefeVdao

from beautifultable import BeautifulTable
from clases.productos import productos

from os import system
from datetime import datetime
import time
import getpass

system('cls')
i_empleadodao = empleadodao()
i_admindao=admindao()
i_jefeVdao=jefeVdao()

def menu1():
    menu1 = BeautifulTable()
    menu1.column_headers = ["----------Inicio de sesion----------"]
    menu1.rows.append(["1) Iniciar sesion"])
    menu1.rows.append(["2) salir"])
    menu1.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu1)



def menu_empleado():
    menu_empleado = BeautifulTable()
    menu_empleado.column_headers = ["----------Menu de empleados----------"]
    menu_empleado.rows.append(["1) generar venta"])
    menu_empleado.rows.append(["2) salir"])
    menu_empleado.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu_empleado)

def menu_empleado2():
    menu_empleado2 = BeautifulTable()
    menu_empleado2.column_headers = ["----------Menu de empleados----------"]
    menu_empleado2.rows.append(["1) agregar producto al carrito"])
    menu_empleado2.rows.append(["2) ver carrito"])
    menu_empleado2.rows.append(["3) vender"])
    menu_empleado2.rows.append(["4) volver"])
    menu_empleado2.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu_empleado2)

def menu_empleado3():
    menu_empleado3 = BeautifulTable()
    menu_empleado3.column_headers = ["----------Menu de empleados----------"]
    menu_empleado3.rows.append(["1) boleta"])
    menu_empleado3.rows.append(["2) factura"])
    menu_empleado3.rows.append(["3) volver"])
    menu_empleado3.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu_empleado3)

def menu_jefeV():
    menu_jefeV = BeautifulTable()
    menu_jefeV.column_headers = ["----------Menu de jefe de ventas----------"]
    menu_jefeV.rows.append(["1) Agregar producto al inventario"])
    menu_jefeV.rows.append(["2) agregar producto al carrito"])
    menu_jefeV.rows.append(["3) Ver carrito"])
    menu_jefeV.rows.append(["4) Vender"])
    menu_jefeV.rows.append(["5) ver ventas del dia"])
    menu_jefeV.rows.append(["6) abrir dia"])
    menu_jefeV.rows.append(["7) cerrar dia"])
    menu_jefeV.rows.append(["8) salir"])

    menu_jefeV.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu_jefeV)

def menu_jefeV2():
    menu_jefeV2 = BeautifulTable()
    menu_jefeV2.column_headers = ["----------ver ventas----------"]
    menu_jefeV2.rows.append(["1) ventas por boleta"])
    menu_jefeV2.rows.append(["2) ventas por factura"])
    menu_jefeV2.rows.append(["3) Todas las ventas"])
    menu_jefeV2.rows.append(["4) volver"])


def menu_admin():
    menu_admin = BeautifulTable()
    menu_admin.column_headers = ["----------Menu de administrador----------"]
    menu_admin.rows.append(["1) Agregar empleado"])
    menu_admin.rows.append(["2) Modificar empleado"])
    menu_admin.rows.append(["3) Eliminar empleado"])
    menu_admin.rows.append(["4) Listar empleados"])
    menu_admin.rows.append(["5) Volver"])
    print(menu_admin)
    
intentos = 5
sesion_iniciada = False 
rol_id = None 
adm = False
jefev=False 
emp=False 
venta=False 
global id_empleado_actual
id_empleado_actual = None
dia = True

while True: 
    if not sesion_iniciada: 
        i_usuariodao=usuariodao(intentos) 
        res=usuario() 
        system('cls')
        menu1()
        op = input("ingrese una opcion: " )
        if op =='1': 
            while intentos > 0 and sesion_iniciada == False:
                correo=input('ingrese su correo: ')
                contrasena=getpass.getpass('ingrese su contraseña: ')
                res=i_usuariodao.conectar(correo,contrasena) 
                system('cls')
                if res is not None: 
                    print('sesion iniciada correctamente') 
                    rol_id = i_usuariodao.obt_rol_id(correo)
                    id_empleado_actual = i_usuariodao.obt_empleado_id(correo)
                    sesion_iniciada = True 
                    time.sleep(2)
                    break
            else:
                intentos -= 1
                if intentos == 0:
                    print('se acabaron los intentos')
                    time.sleep(2)
                    break
                time.sleep(2)
        elif op == '2':
            print('saliendo...')
            time.sleep(2)
            break
        else:
            print('opcion incorrecta')
            time.sleep(2)
    else:
        system('cls')
        if rol_id == 1: 
            adm = True    
            def agregar_empleado(): 
                print('agregar empleado')
                nombre = input('ingrese el nombre: ')
                rut = input('ingrese el rut: ')
                cargo = input('ingrese el cargo:')
                fecha_ingreso = datetime.now().strftime('%Y-%m-%d')
                sueldo = input('ingrese el sueldo: ')
                emp = empleado(nombre, rut, cargo, fecha_ingreso, sueldo)
                print(i_admindao.agregarempleado(emp))
                time.sleep(3)
                pass
                        
            def crear_usuario():
                system('cls')
                print('----------empleados----------')
                i_admindao.listarempleado()
                print('agregar usuario')
                correo = input('ingrese el correo: ')
                contrasena = getpass.getpass('ingrese la contraseña: ')
                rol_id = int(input('ingrese el rol\n1) administrador\n2) empleado\n3) jefe de ventas\n->  '))
                empleado_id = int(input('ingrese el id del empleado: '))
                print(i_usuariodao.crearusuario(correo, contrasena,rol_id,empleado_id))
                time.sleep(3)
                pass
                            
            def modificar_empleado():
                system('cls')
                print('----------empleados----------')
                i_admindao.listarempleado()
                print('modificar empleado')
                rut = input('ingrese el rut del empleado: ')
                nombre = input('ingrese el nombre: ')
                cargo = input('ingrese el cargo:')
                fecha_ingreso = input('ingrese la fecha de ingreso: ')
                sueldo = input('ingrese el sueldo: ')
                emp = empleado(rut, nombre, cargo, fecha_ingreso, sueldo)
                print(i_admindao.actualizarempleado(emp))
                time.sleep(2)
                pass
                            
            
            def eliminar_empleado():
                system('cls')
                print('----------empleados----------')
                i_admindao.listarempleado()
                print('----------eliminar empleado----------')
                id = int(input('ingrese el id del empleado: '))
                if id==1:
                    print('no se puede eliminar el administrador')
                    time.sleep(2)
                    pass
                else:
                    print(i_admindao.eliminarempleado(id))
                    time.sleep(3)
                pass
                            
            def listar_empleados():
                system('cls')
                print('----------Mostrar todos los empleados----------')
                print()
                i_admindao.listarempleado()
                time.sleep(3)
                            
            def incorrecto():
                system('cls')
                print('----------Opcion incorrecta----------')
                print()
                print('volviendo al menu principal')
                time.sleep(1)
                pass
                                
            while adm == True:
                system('cls')
                menu_admin()
                op = input('ingrese una opcion: ')
                if op == '1':
                    agregar_empleado()
                    crear_usuario()
                elif op == '2':
                    modificar_empleado()
                elif op == '3':
                    eliminar_empleado()
                elif op == '4':
                    listar_empleados()
                elif op == '5':
                    print('volviendo al menu principal')
                    sesion_iniciada = False
                    time.sleep(2)
                    break
                else:
                    incorrecto()
        elif rol_id == 2: 
            emp = True 
            def agregar_carrito():
                print('----------agregar producto al carrito----------')
                print()
                while True:
                    try: 
                        producto_id = int(input('ingrese el id del producto: '))
                        if producto_id <= 0:
                            print('Por favor, ingrese un id válido.')
                            time.sleep(2)
                            continue
                        break
                    except ValueError:
                        print('Por favor, ingrese un id válido.')
                        time.sleep(2)
                
                while True:
                    try:
                        cantidad = int(input('ingrese la cantidad: '))
                        if cantidad <= 0:
                            print('Por favor, ingrese una cantidad válida.')
                            time.sleep(2)
                            continue
                        break
                    except ValueError:
                        print('Por favor, ingrese una cantidad válida.')
                        
                i_empleadodao.agregar_carrito_id(producto_id,cantidad)
                time.sleep(2)
                
            def mostrar_productos():
                system('cls')
                print('----------productos----------')
                print()
                i_empleadodao.mostrar_productos()
                time.sleep(2)
                
            def mostrar_carrito():
                system('cls')
                print('----------carrito----------')
                print()
                i_empleadodao.mostrar_carrito()
                time.sleep(3.5)
            
            def boleta():
                system('cls')
                print('----------boleta----------')
                print()
                print(i_empleadodao.generar_boleta())
                time.sleep(7)
                
            def factura():
                system('cls')
                print('----------factura----------')
                print()
                print(i_empleadodao.generar_factura())
                time.sleep(7)
                
            
                
            def generar_venta():
                if dia==True:
                    system('cls')
                    print('----------generar venta----------')
                    print()
                    tipo_venta = int(input('ingrese el tipo de venta\n1) boleta\n2) factura\n-> '))
                    
                    i_empleadodao.generar_venta(id_empleado_actual,tipo_venta)
                    time.sleep(2)
                    if tipo_venta == 1:
                        tipo_venta ='boleta'
                        boleta()
                        time.sleep(5)
                    elif tipo_venta == 2:
                        tipo_venta ='factura'
                        factura()
                        time.sleep(8)
                    else:
                        print('opcion incorrecta')
                        time.sleep(1)
                else:
                    print('no se puede vender, el dia no esta abierto')
                    time.sleep(2)
            
            
            def vaciar_carrito():
                system('cls')
                print('----------vaciar carrito----------')
                print()
                print(i_empleadodao.vaciar_carrito())
                time.sleep(2)
                
            while emp == True:
                system('cls')
                menu_empleado()
                op = input('ingrese una opcion: ')
                if op == '1':
                    venta=True
                    while venta==True:
                        system('cls')
                        menu_empleado2()
                        op = input('ingrese una opcion: ')
                        if op == '1':
                            mostrar_productos()
                            agregar_carrito()
                        elif op == '2':
                            mostrar_carrito()
                        elif op == '3':
                            generar_venta()
                            vaciar_carrito()
                            time.sleep(2)
                        elif op == '4':
                            print('volviendo al menu principal')
                            time.sleep(2)
                            venta=False
                            break
                        
                elif op == '2':
                    print('volviendo al menu principal')
                    sesion_iniciada = False
                    time.sleep(2)
                    break
                else:
                    print('opcion incorrecta')
                    time.sleep(2)
            
        elif rol_id == 3:
            jefev = True 
            
            def agregar_carrito():
                print('----------agregar producto al carrito----------')
                print()
                while True:
                    try: 
                        producto_id = int(input('ingrese el id del producto: '))
                        if producto_id <= 0:
                            print('Por favor, ingrese un id válido.')
                            time.sleep(2)
                            continue
                        break
                    except ValueError:
                        print('Por favor, ingrese un id válido.')
                        time.sleep(2)
                
                while True:
                    try:
                        cantidad = int(input('ingrese la cantidad: '))
                        if cantidad <= 0:
                            print('Por favor, ingrese una cantidad válida.')
                            time.sleep(2)
                            continue
                        break
                    except ValueError:
                        print('Por favor, ingrese una cantidad válida.')   
                i_empleadodao.agregar_carrito_id(producto_id,cantidad)
                time.sleep(2)
                
            def mostrar_productos():
                system('cls')
                print('----------productos----------')
                print()
                i_empleadodao.mostrar_productos()
                time.sleep(2)
                
            def mostrar_carrito():
                system('cls')
                print('----------carrito----------')
                print()
                i_empleadodao.mostrar_carrito()
                time.sleep(3.5)
            
            def boleta():
                system('cls')
                print('----------boleta----------')
                print()
                print(i_empleadodao.generar_boleta())
                time.sleep(7)
                
            def factura():
                system('cls')
                print('----------factura----------')
                print()
                print(i_empleadodao.generar_factura())
                time.sleep(7)
                
            
                
            def generar_venta():
                if dia==True:
                    system('cls')
                    print('----------generar venta----------')
                    print()
                    tipo_venta = int(input('ingrese el tipo de venta\n1) boleta\n2) factura\n-> '))
                    
                    i_empleadodao.generar_venta(id_empleado_actual,tipo_venta)
                    time.sleep(2)
                    if tipo_venta == 1:
                        tipo_venta ='boleta'
                        boleta()
                        time.sleep(5)
                    elif tipo_venta == 2:
                        tipo_venta ='factura'
                        factura()
                        time.sleep(8)
                    else:
                        print('opcion incorrecta')
                        time.sleep(1)
                else:
                    print('no se puede vender, el dia no esta abierto')
                    time.sleep(2)
            
            
            def vaciar_carrito():
                system('cls')
                print('----------vaciar carrito----------')
                print()
                print(i_empleadodao.vaciar_carrito())
                time.sleep(2)
                
                
            def agregar_producto(): 
                system('cls')
                print('----------agregar producto----------')
                print()
                nombre=input('ingrese el nombre del producto: ')
                codigo=input('ingrese el codigo del producto: ')
                while True:
                    precio_input = input('ingrese el precio del producto: ')
                    if precio_input.isnumeric():
                        precio = int(precio_input)
                        break
                    else:
                        print('Por favor, ingrese el precio del producto en números.')
                        time.sleep(2)
                prod=productos(nombre,codigo,precio)
                print(i_jefeVdao.agregarProducto(prod))
                time.sleep(3)
    
            
            def ver_ventas():
                system('cls')
                print('----------ver ventas----------')
                print()
                print(i_jefeVdao.ver_ventas())
                time.sleep(2)
                
            def ventas_boletas():
                system('cls')
                print('----------ventas por boleta----------')
                print()
                print(i_jefeVdao.ventas_boleta())
                time.sleep(2)
                
            def ventas_factura():
                system('cls')
                print('----------ventas por factura----------')
                print()
                print(i_jefeVdao.ventas_factura())
                time.sleep(2)
                
            while jefev==True:
                system('cls')
                system('cls')
                menu_jefeV()
                op = input('ingrese una opcion: ')
                if op == '1':
                    agregar_producto()
                elif op=='2':
                    mostrar_productos()
                    agregar_carrito()
                elif op=='3':
                    mostrar_carrito()
                elif op=='4':
                    generar_venta()
                    vaciar_carrito()
                    time.sleep(2)
                    
                    
                    
                elif op=='5':
                    menu_jefeV2()
                    op = input('ingrese una opcion: ')
                    if op=='1':
                        print('ventas por boleta')
                        print(i_jefeVdao.ventas_boleta())
                        time.sleep(2)
                    elif op=='2':
                        print('ventas por factura')
                        print(i_jefeVdao.ventas_factura())
                        time.sleep(2)
                    elif op=='3':
                        print('todas las ventas')
                        print(i_jefeVdao.ver_ventas())
                        time.sleep(2)
                    elif op=='4':
                        print('volviendo al menu principal')
                        time.sleep(2)
                        break
                    
                    
                    
                    
                    
                    
                    
                    
                elif op=='6':
                    print('abrir dia')
                    dia=True
                    time.sleep(2)
                elif op=='7':
                    print('cerrar dia')
                    dia=False
                    time.sleep(2)
                elif op=='8':
                    print('volviendo al menu principal')
                    sesion_iniciada = False
                    time.sleep(2)
                    break
        else:
            break