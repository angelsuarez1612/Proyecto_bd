from funciones import *

db = Conectar_BD("localhost","suarez","passwd","proyecto_bd")
menu = '''
1. Listar las empresas junto con el número de alumnos que han realizado prácticas en ellas
2. Pedir un sector y mostrar todas las empresas que pertenecen a ese sector
3. Pedir por teclado el nombre de un alumno y mostrar la empresa donde está realizando las prácticas
4. Insertar un nuevo alumno con todos sus datos e información acerca de las prácticas que 
ha realizado ese alumno (si en la información de las prácticas se introduce un identificador
de empresa inexistente, tendrás que añadir una nueva empresa con ese identificador y el resto de datos)
5. Pedir el nombre de un alumno por teclado y borrar ese alumno
6. Pide por teclado el nombre de una empresa y cambia su dirección por una que pidas porteclado
'''
print(menu)
opc = int(input("Introduce una opción: "))
while opc != 7:
    if opc == 1:
        listar_empryalum(db)
        print("-----------------------------------------------------")

    elif opc == 2:
        print("Estos son todos los sectores que hay:")
        todos_sectores(db)
        print()
        misector=input("Introduce un sector por el que buscar: ")
        print("\n")
        print("-- EMPRESAS CON EL SECTOR '%s' --" % misector)
        buscar_sector(db,misector)
        print("-----------------------------------------------------")

    elif opc == 3:
        print("Estos son todos los alumnos: ")
        todos_alumnos(db)
        mialumno=input("Introduce el nombre de uno de los alumnos: ")
        print("\n")
        print("Empresas donde realiza las prácticas %s" % mialumno)
        alumno_practicas(db,mialumno)
        print("-----------------------------------------------------")

    elif opc == 4:
        print("INSERTAR EN TABLA ALUMNOS")
        alumno={}
        alumno["dni_alumno"] = input("DNI: ")
        alumno["nombre"] = input("Nombre: ")
        alumno["direccion"] = input("Dirección: ")
        alumno["tlf"] = input("TLF: ")
        insertar_datos(db,alumno)
        preg = input("El alumno, ¿va a realizar las prácticas en una empresa no registrada en la base de datos?: (responder con s/n, si dejas en blanco = 'n') ")
        if preg == "s":
            #En caso de elegir "s" tendrás que crear la nueva empresa, si elijes "n" el programa entenderá que vas a asignar una empresa ya registrada
            print()
            print("INSERTAR EN TABLA EMPRESAS")
            empresas={}
            empresas["nif_empresa"] = input("Nif empresa: ")
            empresas["nombre_empresa"] = input("Nombre empresa: ")
            empresas["direccion"] = input("Dirección: ")
            empresas["res_legal"] = input("Resposable Legal: ")
            empresas["sector"] = input("Sector: ")
            encasode(db,empresas)
        print()
        print("INSERTAR EN TABLA PRÁCTICAS")
        practica={}
        practica["fk_dni_alumno"] = alumno["dni_alumno"]
        if preg == "s":
            practica["fk_nif_empresa"] = empresas["nif_empresa"]
        else:
            practica["fk_nif_empresa"] = input("Nif empresa:")
        #f_inicio hay que insertarlo como una fecha, si no, da error YYYY-MM-DD
        practica["f_inicio"] = input("Fecha de inicio: ")
        practica["numhoras"] = int(input("Número de horas: "))
        insertar_practicas(db,practica)
        print()
        print("RESULTADO DE LA TABLA PRÁCTICAS (engloba si hay un alumno nuevo y donde realiza las prácticas)")
        mostrar_practicas(db)
        
    elif opc == 5:
        print("Estos son todos los alumnos: ")
        todos_alumnos(db)
        print()
        minombre=input("Introduce el nombre de un alumno que quieras eliminar: ")
        print("\n")
        borrar_alumno(db,minombre)
        print("-----------------------------------------------------")

    elif opc == 6:
        print("Estas son todas las empresas y sus actuales direcciones: ")
        empresa(db)
        print()
        miempresa=input("Introduce el nombre de una empresa: ")
        midireccion=input("Introduce una dirección para sustituir la que ya tiene esa empresa: ")
        print("\n")
        cambiar_direccion(db,miempresa,midireccion)
        print("-----------------------------------------------------")

    else:
        print("Valor no válido")

    print("\n")
    print(menu)
    opc = int(input("Introduce una opción: "))

print("¡FIN DE PROGRAMA!")