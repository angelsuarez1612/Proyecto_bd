-- Entramos con root y creamos el usuario, por eso luego he puesto un exit
GRANT ALL PRIVILEGES ON *.* TO 'suarez'@'localhost' IDENTIFIED BY 'passwd' WITH GRANT OPTION;
exit
mysql -u suarez -p
CREATE DATABASE proyecto_bd;
use proyecto_bd;

CREATE TABLE Alumnos
(
    dni_alumno varchar(10),
    nombre varchar(20),
    direccion varchar(20),
    tlf varchar(10),
    CONSTRAINT CK_dni_alumno PRIMARY KEY (dni_alumno)
);

CREATE TABLE Empresas
(
    nif_empresa varchar(10),
    nombre_empresa varchar(20),
    direccion varchar(20),
    res_legal varchar(20),
    sector varchar(20),
    CONSTRAINT CK_nif_empresa PRIMARY KEY (nif_empresa)
);

CREATE TABLE Practicas
(
    fk_dni_alumno varchar(10),
    fk_nif_empresa varchar(10),
    f_inicio date,
    numhoras int(4) DEFAULT 0,
    CONSTRAINT CK_prim_prac PRIMARY KEY (fk_dni_alumno,fk_nif_empresa),
    CONSTRAINT CK_FK_dni FOREIGN KEY (fk_dni_alumno) REFERENCES Alumnos(dni_alumno),
    CONSTRAINT CK_FK_nif FOREIGN KEY (fk_nif_empresa) REFERENCES Empresas(nif_empresa)
);

INSERT INTO Alumnos VALUES ('111-A','David','Sevilla Este','954025122');
INSERT INTO Alumnos VALUES ('222-B','Mariano','Los Remedios','954221541');
INSERT INTO Alumnos VALUES ('333-C','Raul','Triana','955124455');
INSERT INTO Alumnos VALUES ('444-D','Rocio','La Oliva','955236654');
INSERT INTO Alumnos VALUES ('555-E','Marilo','Triana','954085211');
INSERT INTO Alumnos VALUES ('666-F','Benjamin','Montequinto','955662512');
INSERT INTO Alumnos VALUES ('777-G','Carlos','Los Remedios','955662211');
INSERT INTO Alumnos VALUES ('888-H','Manolo','Montequinto','954725414');

INSERT INTO Empresas VALUES ('41001-A','Sandiel','Pab. Moldavia','Ramon','Informática');
INSERT INTO Empresas VALUES ('41002-B','Condelans','Pab. Chechenia','Juan','Informática');
INSERT INTO Empresas VALUES ('41003-C','Guadartes','Pab. La Algaba','Pepe','Informática');
INSERT INTO Empresas VALUES ('41004-D','Jindras','c/Pi, 4','Mari','I+D');
INSERT INTO Empresas VALUES ('41005-E','SGI Tesnologi','c/ Cabañeros, 2','Carmela','I+D');
INSERT INTO Empresas VALUES ('41006-F','Nesus','c/ Sierpes, 12','Pepi','Electrónica');
INSERT INTO Empresas VALUES ('41007-G','Abengoa','c/ Tajo, 2','Gabriel','Electrónica');

INSERT INTO Practicas VALUES ('111-A','41001-A','2002-10-18','350');
INSERT INTO Practicas VALUES ('333-C','41003-C','2002-11-19','300');
INSERT INTO Practicas VALUES ('111-A','41004-D','2002-11-20','400');
INSERT INTO Practicas VALUES ('444-D','41005-E','2002-11-19','400');
INSERT INTO Practicas VALUES ('111-A','41003-C','2002-11-14','300');
INSERT INTO Practicas VALUES ('777-G','41006-F','2002-11-19','400');
INSERT INTO Practicas VALUES ('888-H','41007-G','2002-11-16','500');
INSERT INTO Practicas VALUES ('222-B','41003-C','2002-11-15','400');
INSERT INTO Practicas VALUES ('555-E','41002-B','2002-11-17','400');
INSERT INTO Practicas VALUES ('333-C','41001-A','2002-11-20','400');
INSERT INTO Practicas VALUES ('777-G','41003-C','2002-11-20','500');
