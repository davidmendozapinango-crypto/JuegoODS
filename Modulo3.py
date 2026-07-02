from registrar import *
#Pedir cédula y clave al jugador.
reg = False
while reg == False:
    ced = int(input("Introduce tu cedula:  "))
    clave = input("Introduce tu clave:  ")
    #Ver que la cédula y clave se encuentren registrados en el archivo "JUGADORES"
    archivo_jugadores = open(JUGADORES.bin, 'rb')
    encontrado = False 
    eof = False
    registro = archivo_jugadores.read(JUGADORES.bin)
    while encontrado == False and eof == False:
        if registro == b'':
            eof = True
        else:
            ced_reg, nom, sex, fecha, est, clav = struct.unpack(formatojugador, registro)          
    #Si se encuentra una cédula igual
            if ced_reg == ced:
                encontrado = True
                archivo_jugadores.close()
            else:
                registro = archivo_jugadores.read(JUGADORES.bin)
    if encontrado == False:
        print("La cedula no ha sido registrada... ")
        reg = False
    else:
        reg = True
        eof = False
    registro = archivo_jugadores.read(JUGADORES.bin)
    while encontrado == False and eof == False:
        if registro == b'':
            eof = True
        else:
            ced_reg, nom, sex, fecha, est, clav = struct.unpack(formatojugador, registro)          
    #Si se encuentra una cédula igual
            if ced_reg == ced:
                encontrado = True
                archivo_jugadores.close()
            else:
                registro = archivo_jugadores.read(JUGADORES.bin)