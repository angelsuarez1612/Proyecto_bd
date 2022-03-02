import sys
import MySQLdb

def Conectar_BD(localhost,suarez,passwd,proyecto_bd):
    try:
        db = MySQLdb.connect(localhost,suarez,passwd,proyecto_bd)
        return db
    except MySQLdb.Error as e:
        print("No se puede conectar a la base de datos: ", e)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()

#1
def listar_empryalum(db):
    sql="SELECT nombre_empresa,count(*) as 'NumAlumnos' FROM Empresas,Practicas WHERE nif_empresa = fk_nif_empresa GROUP BY nombre_empresa"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        emp = cursor.fetchall()
        for ej1 in emp:
            print(ej1["nombre_empresa"],"---",ej1["NumAlumnos"])
    except:
        print("Error en la consulta")
#2 
def todos_sectores(db):
    sql="SELECT sector FROM Empresas GROUP BY sector"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        todsec = cursor.fetchall()
        for a in todsec:
            print(a["sector"])
    except:
        print("Error en la consulta")

def buscar_sector(db,sector):
    sql="SELECT nombre_empresa FROM Empresas WHERE sector='%s'" % sector
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("Ninguna empresa coincide con ese sector")
        else:
            sec = cursor.fetchall()
            for ej2 in sec:
                print(ej2["nombre_empresa"])
    except:
        print("Error en la consulta")
#3
def todos_alumnos(db):
    sql="SELECT nombre FROM Alumnos"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        todalum = cursor.fetchall()
        for a in todalum:
            print(a["nombre"])
    except:
        print("Error en la consulta")

def alumno_practicas(db,alumno):
    sql="SELECT nombre as 'Alumno',nombre_empresa as 'Empresa' FROM Alumnos,Empresas,Practicas WHERE nombre = '%s' AND dni_alumno = fk_dni_alumno AND nif_empresa = fk_nif_empresa" % alumno
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No encontramos datos acerca de ese alumno")
        else:
            alu = cursor.fetchall()
            for ej3 in alu:
                print(ej3["Empresa"])
    except:
        print("Error en la consulta")

#4
def encasode(db,empresas):
    sql="INSERT INTO Empresas VALUES ('%s','%s','%s','%s','%s')" % (empresas["nif_empresa"],empresas["nombre_empresa"],empresas["direccion"],empresas["res_legal"],empresas["sector"])
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar empresas")
        db.rollback()

def insertar_datos(db,alumno):
    cursor = db.cursor()
    sql="INSERT INTO Alumnos VALUES ('%s','%s','%s','%s')" % (alumno["dni_alumno"],alumno["nombre"],alumno["direccion"],alumno["tlf"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar alumnos")
        db.rollback()

def insertar_practicas(db,practica):
    cursor = db.cursor()
    sql="INSERT INTO Practicas VALUES ('%s','%s','%s',%d)" % (practica["fk_dni_alumno"],practica["fk_nif_empresa"],practica["f_inicio"],practica["numhoras"])
    cursor.execute(sql)
    db.commit()

def mostrar_practicas(db):
    sql="SELECT * FROM Practicas"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        muestra = cursor.fetchall()
        for a in muestra:
            print(a)
    except:
        print("Error al consultar prácticas")

#5
def borrar_alumno(db,nombre):
    sql="DELETE FROM Practicas WHERE fk_dni_alumno = (SELECT dni_alumno FROM Alumnos WHERE nombre='%s')" % nombre
    sql1="DELETE FROM Alumnos WHERE nombre='%s'" % nombre
    cursor = db.cursor()
    preg=input("Estás apunto de eliminar al alumno %s, ¿continuar?: (responder con s/n) " % nombre)    
    if preg == "s":
        try:
            cursor.execute(sql)
            cursor.execute(sql1)
            db.commit()
            if cursor.rowcount==0:
                print("No hay resultados de alumnos con ese nombre")
            else:
                print("\n")
                print("Alumno borrado exitosamente")
        except:
            print("Error al eliminar el alumno")
            db.rollback()
    sql2="SELECT * FROM Alumnos"
    cursorr = db.cursor()
    try:
        cursorr.execute(sql2)
        muestra=cursorr.fetchall()
        print("Este sería el resultado de la tabla alumnos despues del proceso:")
        for a in muestra:
            print(a)
    except:
        print("Error al mostrar la consulta")
#6
def empresa(db):
    sql="SELECT nombre_empresa,direccion FROM Empresas"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        todempresa = cursor.fetchall()
        for a in todempresa:
            print(a["nombre_empresa"],"---",a["direccion"])
    except:
        print("Error en la consulta")

def cambiar_direccion(db,empresa,direccion):
    sql="UPDATE Empresas SET direccion = '%s' WHERE nombre_empresa = '%s'" % (direccion,empresa)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error en la consulta")
        db.rollback()

    sql2="SELECT * FROM Empresas"
    cursorr = db.cursor()
    try:
        cursorr.execute(sql2)
        muestra=cursorr.fetchall()
        print("Este sería el resultado de la tabla empresas despues del proceso:")
        for a in muestra:
            print(a)
    except:
        print("Error al mostrar la consulta")