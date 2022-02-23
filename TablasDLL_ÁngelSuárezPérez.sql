CREATE TABLE Alumnos
(
    dni_alumno varchar2(10),
    nombre varchar2(20),
    direccion varchar2(20),
    tlf varchar2(10),
    CONSTRAINT CK_dni_alumno PRIMARY KEY (dni_alumno)
);

CREATE TABLE Empresas
(
    nif_empresa varchar2(10),
    nombre_empresa varchar(20),
    direccion varchar2(10),
    res_legal varchar2(20),
    sector varchar(10),
    CONSTRAINT CK_nif_empresa PRIMARY KEY (nif_empresa)
);

CREATE TABLE Practicas
(
    fk_dni_alumno varchar(10),
    fk_nif_empresa varchar2(10),
    f_inicio timestamp,
    numhoras number(4) DEFAULT 0,
    CONSTRAINT CK_prim_prac PRIMARY KEY (fk_dni_alumno,fk_nif_empresa),
    CONSTRAINT CK_FK_dni FOREIGN KEY (fk_dni_alumno) REFERENCES Alumnos(dni_alumno),
    CONSTRAINT CK_FK_nif FOREIGN KEY (fk_nif_empresa) REFERENCES Empresas(nif_empresa)
);